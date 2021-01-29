from action import PlayerAction
from action import InterfaceAction
from action import ItemAction
from error import ConfigError


class Death(object):
    """Defines a death scenario."""

    def __init__(self, level, *args, **kwargs):
        self.level = level
        self.device_states = []
        self.action = None
        self.location = None
        self.description = 'You died.'

    def is_valid(self):

        return len(self.device_states) > 0 or self.action is not None or self.location is not None

    def add_device_state(self, config_id, active_state):
        """Add a device state to the death scenario."""

        if config_id in [i for device in self.device_states for i in device.keys()]:
            raise ValueError("The device with config_id {0} has already been added.".format(config_id))

        device = self.level.system.get_device(config_id=config_id)
        self.device_states.append({'device': device, 'active_state': active_state})

    def remove_device_state(self, config_id):
        """Remove a device state from the death scenario."""

        for device_config in self.device_states:
            if device_config['device'].config_id == config_id:
                self.device_states.remove(device_config['device'])

    def add_device_states(self, device_states_config):
        """Add device states from config."""

        for config in device_states_config:
            self.add_device_state(config['device_id'], config['active_state'])

    def set_action_player(self, verb, target_type, target_config_id):
        """Add a player action to the death scenario."""

        if target_type == 'interface':
            target = self.level.system.get_interface(config_id=target_config_id)
        elif target_type == 'tool':
            target = self.level.map.inventory.get_tool(config_id=target_config_id)
        elif target_type == 'part':
            target = self.level.map.inventory.get_part(config_id=target_config_id)
        elif target_type == 'artifact':
            target = self.level.map.inventory.get_artifact(config_id=target_config_id)
        else:
            raise ValueError("Argument target_type {0} must be one of: interface, tool, part, artifact.".format(target_type))

        if verb == 'use':
            player_action = PlayerAction(
                game=self.level.game,
                function=target.use,
                description=target.action_text(),
                target=target)
        elif verb == 'examine':
            player_action = PlayerAction(
                game=self.level.game,
                function=target.examine,
                description=target.examine_action_text(),
                target=target)
        elif verb == 'take':
            player_action = PlayerAction(
                game=self.level.game,
                function=target.map_to_player,
                description=target.take_action_text(),
                target=target)
        else:
            raise ValueError("Argument verb must be one of: use, examine, take.")

        self.action = player_action

    def set_action_interface(self, origin_config_id, target_config_id):
        """Add a player action to the death scenario."""

        interface = self.level.system.get_interface(config_id=origin_config_id)
        device = self.level.system.get_device(config_id=target_config_id)

        interface_action = InterfaceAction(
            game=self.system.level.game,
            function=device.use,
            description=device.action_text(),
            interface=interface,
            device=device)

        self.action = interface_action

    def set_action_item(self, origin_type, origin_config_id, target_config_id):
        """Add an item action to the death scenario."""

        target = self.level.system.get_device(config_id=target_config_id)

        if origin_type == 'tool':
            origin = self.level.map.inventory.get_tool(config_id=origin_config_id)
        elif origin_type == 'part':
            origin = self.level.map.inventory.get_part(config_id=origin_config_id)
        else:
            raise ValueError("Argument origin_type {0} must be one of: tool, part.".format(origin_type))

        item_action = ItemAction(
            game=self.level.game,
            function=origin.get_use_function(target),
            description=origin.use_action_text(target),
            item=origin,
            device=target)

        self.action = item_action

    def set_action(self, action_config):
        """Set action from config."""

        origin_type = action_config['origin']['type']
        target_config_id = action_config['target']['id']

        if origin_type == 'player':
            verb = action_config['origin']['verb']
            target_type = action_config['target']['type']
            self.set_action_player(verb, target_type, target_config_id)
        elif origin_type == 'interface':
            origin_config_id = action_config['origin']['id']
            self.set_action_interface(origin_config_id, target_config_id)
        elif origin_type in ('tool', 'part'):
            origin_config_id = action_config['origin']['id']
            self.set_action_item(origin_type, origin_config_id, target_config_id)
        else:
            raise ValueError("Configuration origin_type {0} must be one of: player, interface, tool, part.".format(origin_type))

    def scenario_satisfied(self):
        """Returns True if current game conditions match the death scenario, otherwise False."""

        devices_match = True
        action_match = True
        location_match = True

        # check device states
        if len(self.device_states) > 0:
            for device_state in self.device_states:
                device = device_state['device']
                expected_state = device_state['active_state']

                if device.active != expected_state:
                    devices_match = False
                    break

        # check action
        if self.action is not None:
            if self.action != self.level.game.player.last_action:
                action_match = False

        # check location
        if self.location is not None:
            if self.location != self.level.game.player.location:
                location_match = False

        return devices_match and action_match and location_match


class DeathFactory(object):
    """Create death type instances."""

    @staticmethod
    def make_from_config(level, death_config):

        device_states_config = death_config['device_states']
        action_config = death_config['action']
        death = Death(level=level)

        if device_states_config is not None:
            death.add_device_states(device_states_config)

        if action_config is not None:
            death.set_action(action_config)

        death.location = death_config['location']
        death.description = death_config['description']

        if not death.is_valid():
            raise ConfigError("The provided death configuration is invalid.")

        return death
