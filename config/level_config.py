from config.player_config import player_config

level_config = {
    0: {
        'name': 'Void',
        'map': {
            'x_dimension': 1,
            'y_dimension': 2,
            'path_cells': [
                {'coordinates': (0, 0), 'story': None},
                {'coordinates': (0, 1),
                 'story': {'title': 'Void', 'text': 'This place is not for you. Run along now...'}}
            ],
            'coord_enter': (0, 1),  # begin
            'coord_exit': (0, 0),  # end
            'orientation_enter': 0,
            'tools': [],
            'parts': [],
            'artifacts': []
        },
        'system': {
            'interfaces': [],
            'devices': [],
            'properties': [],
            'links': [],
            'relates': [],
            'deaths': []
        }
    },  # void
    1: {
        'name': 'Approach',
        'map': {
            'x_dimension': 7,
            'y_dimension': 5,
            'path_cells': [
                {'coordinates': (3, 4), 'story': None},
                {'coordinates': (3, 3), 'story': {'title': None,
                                                  'text': 'Faint clouds of dust fell from his boots as {0} climbed down the rover ladder. "Something is very wrong", he thought, while surveying his surroundings for any sign of disaster. Everything was in place. There was no evidence of an explosion or collapse. The light over the external airlock door glowed green indicating its pressure matched that of the external environment. According to his suit\'s computer, he still had active comm and telemetry links with Alpha Point but all he could hear was the sound of his own breathing. "What the hell?", {0} wondered, as he headed toward the airlock.'.format(
                                                      player_config['name'])}},
                {'coordinates': (3, 2), 'story': None},
                {'coordinates': (3, 1), 'story': None},
                {'coordinates': (3, 0), 'story': None},
                {'coordinates': (4, 3), 'story': None},
                {'coordinates': (5, 3), 'story': None},
                {'coordinates': (2, 1), 'story': None},
                {'coordinates': (1, 1), 'story': None}
            ],
            'coord_enter': (3, 3),  # begin
            'coord_exit': (3, 0),  # end
            'orientation_enter': 0,
            'tools': [],
            'parts': [],
            'artifacts': [
                {
                    'type': 'generic',
                    'name': 'rover',
                    'description': 'rover',
                    'report': 'It\'s a medium range rover with a small Apex Initiative logo on the side.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 3,
                    'y': 4
                },  # rover
                {
                    'type': 'generic',
                    'name': 'generator',
                    'description': 'generator cluster in the distance',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 0,
                    'y': 1
                },  # generator array
                {
                    'type': 'generic',
                    'name': 'communicationsarray',
                    'description': 'communications array on top of the crater wall',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 6,
                    'y': 3
                },  # communications array
            ]
        },
        'system': {
            'interfaces': [
                {
                    'id': 0,
                    'type': 'button',
                    'name': 'airlock door button',
                    'description': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 3,
                    'y': 0,
                    'orientation': 2,
                    'msg_action_verb': 'push'
                }  # airlock door button
            ],
            'devices': [
                {
                    'id': 1,
                    'type': 'door',
                    'name': 'airlock door',
                    'description': 'airlock door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': True,
                    'x': 3,
                    'y': 0,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                }  # airlock door
            ],
            'properties': [],
            'links': [
                {'interface_id': 0, 'device_id': 1}
            ],
            'relates': [],
            'deaths': []
        }
    },  # approach
    2: {
        'name': 'Airlock',
        'map': {
            'x_dimension': 3,
            'y_dimension': 5,
            'path_cells': [
                {'coordinates': (1, 0), 'story': None},
                {'coordinates': (1, 1), 'story': None},
                {'coordinates': (1, 2), 'story': None},
                {'coordinates': (1, 3), 'story': {'title': None, 'text': (
                    '{0} checked his mission clock as the door sealed behind him. He was about thirty minutes ahead of his scheduled return time. "Alright, focus.", he thought, "Follow the ingress procedure."').format(
                    player_config['name'])}},
                {'coordinates': (1, 4), 'story': None}
            ],
            'coord_enter': (1, 3),  # begin
            'coord_exit': (1, 0),  # end
            'orientation_enter': 0,
            'tools': [],
            'parts': [],
            'artifacts': []
        },
        'system': {
            'interfaces': [
                {
                    'id': 0,
                    'name': 'airlock pressurization button',
                    'description': 'button labeled "Pressure Control"',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 2,
                    'y': 2,
                    'orientation': 3,
                    'msg_action_verb': 'push'
                },  # 0 - airlock pressurization button
                {
                    'id': 1,
                    'name': 'airlock pressurization handwheel',
                    'description': 'yellow handwheel labeled "Pressure Control - Manual Override"',
                    'type': 'handwheel',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 0,
                    'y': 1,
                    'orientation': 1,
                    'msg_action_verb': 'turn'
                },  # 1 - airlock pressurization handwheel
                {
                    'id': 2,
                    'name': 'exit door button',
                    'description': 'button',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 1,
                    'y': 0,
                    'orientation': 2,
                    'msg_action_verb': 'push'
                },  # 2 - exit door button
                {
                    'id': 3,
                    'name': 'weather',
                    'description': 'weather station console',
                    'type': 'weatherstation',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 2,
                    'y': 3,
                    'orientation': 3,
                    'msg_action_verb': 'use'
                }  # 3 weather station
            ],
            'devices': [
                {
                    'id': 0,
                    'name': 'entrance door',
                    'description': 'airlock door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': True,
                    'x': 1,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # 0 - entrance door
                {
                    'id': 1,
                    'name': 'airlock pressurization valve',
                    'description': 'pressurization valve',
                    'type': 'valve',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': False,
                    'x': 0,
                    'y': 1,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The valve is open.',
                    'msg_active_false': 'The valve is closed.',
                    'msg_toggle_active_true': 'My suit collapsed and the green internal door indicator reads "Airlock Pressurized".',
                    'msg_toggle_active_false': 'My suit expanded and the red internal door indicator reads "Airlock Purged".',
                    'msg_unmet_dependencies': 'The valve isn\'t responding.',
                    'dependencies': []
                },  # 1 - airlock pressurization valve
                {
                    'id': 2,
                    'name': 'exit door',
                    'description': 'airlock door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': True,
                    'x': 1,
                    'y': 0,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': [
                        {'device_id': 1, 'enabled_state': True, 'active_state': True}
                    ]
                }  # 2 - exit door
            ],
            'properties': [],
            'links': [
                {'interface_id': 1, 'device_id': 1},
                {'interface_id': 2, 'device_id': 2}
            ],
            'relates': [],
            'deaths': [
                {'configuration': [
                    {'device_id': 1, 'active_state': False},
                    {'device_id': 2, 'active_state': True}],
                    'description': 'You just depressurized the entire habitat and probably killed all your friends.',
                    'location': None}  # None if all locations are valid
            ]
        }
    },  # airlock
    3: {
        'name': 'Equipment',
        'map': {
            'x_dimension': 9,
            'y_dimension': 9,
            'path_cells': [
                {'coordinates': (4, 0), 'story': None},
                {'coordinates': (4, 1), 'story': None},
                {'coordinates': (4, 2), 'story': None},
                {'coordinates': (4, 3), 'story': None},
                {'coordinates': (4, 4), 'story': None},
                {'coordinates': (4, 5), 'story': None},
                {'coordinates': (4, 6), 'story': None},
                {'coordinates': (4, 7), 'story': {'title': None,
                                                  'text': 'As he removed his helmet, {0} noticed three empty excursion suit alcoves and wondered who else was outside the hab. Ad-hoc departures weren\'t that unusual. Even Martian research stations have fences that need mending. The lights flickered briefly and {0} detected the caustic smell of overheated electronics. "That can\'t be good", he told himself. After stowing his suit in an open alcove {0} headed for the door of the crew meeting area at the far end of the equipment bay.'.format(
                                                      player_config['name'])}},
                {'coordinates': (4, 8), 'story': None},
                {'coordinates': (3, 6), 'story': None},
                {'coordinates': (3, 7), 'story': None},
                {'coordinates': (5, 6), 'story': None},
                {'coordinates': (5, 7), 'story': None},
                {'coordinates': (3, 4), 'story': None},
                {'coordinates': (2, 4), 'story': None},
                {'coordinates': (1, 4), 'story': None},
                {'coordinates': (5, 4), 'story': None},
                {'coordinates': (6, 4), 'story': None},
                {'coordinates': (7, 4), 'story': None},
                {'coordinates': (3, 2), 'story': None},
                {'coordinates': (2, 2), 'story': None},
                {'coordinates': (1, 2), 'story': None},
                {'coordinates': (5, 2), 'story': None},
                {'coordinates': (6, 2), 'story': None},
                {'coordinates': (7, 2), 'story': None}
            ],
            'coord_enter': (4, 7),  # begin
            'coord_exit': (4, 0),  # end
            'orientation_enter': 0,
            'tools': [
                {
                    'type': 'prybar',
                    'name': 'prybar',
                    'description': 'prybar',
                    'report': 'A steel-tipped titanium prybar.',
                    'inspectable': False,
                    'visible': True,
                    'interactive': True,
                    'blocking': False,
                    'x': 1,
                    'y': 4
                }  # prybar
            ],
            'parts': [
                {
                    'type': 'wires',
                    'name': 'wire_bundle',
                    'description': 'bundle of wires and circuitry',
                    'report': 'Multi-colored wires and a small circuit board.',
                    'inspectable': False,
                    'visible': True,
                    'interactive': True,
                    'blocking': False,
                    'x': 6,
                    'y': 1
                }  # bundle of wires and circuitry
            ],
            'artifacts': [
                {
                    'type': 'generic',
                    'name': 'suit_1',
                    'description': 'excursion suit',
                    'report': 'A standard excursion suit with a name plate that reads "Tonia Cherneyev - Mission Commander".',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 3,
                    'y': 6
                },  # excursion suit
                {
                    'type': 'generic',
                    'name': 'suit_2',
                    'description': 'excursion suit',
                    'report': 'A standard excursion suit with a name plate that reads "James O\'Reilly - Systems Engineer".',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 3,
                    'y': 7
                },  # excursion suit
                {
                    'type': 'generic',
                    'name': 'suit_3',
                    'description': 'excursion suit',
                    'report': 'A standard excursion suit with a name plate that reads "Marcus LeMaire - Science Officer".',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 5,
                    'y': 7
                },  # excursion suit
                {
                    'type': 'generic',
                    'name': 'helmet_1',
                    'description': 'excursion suit helmet',
                    'report': 'A standard excursion suit helmet.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': True,
                    'blocking': False,
                    'x': 7,
                    'y': 3
                }  # excursion suit helmet
            ]
        },
        'system': {
            'interfaces': [
                {
                    'id': 0,
                    'name': 'exit door button',
                    'description': 'button',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 5,
                    'y': 1,
                    'orientation': 3,
                    'msg_action_verb': 'push'
                },  # 0 - exit door button
                {
                    'id': 1,
                    'name': 'door circuit toggleswitch',
                    'description': 'switch',
                    'type': 'toggleswitch',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 0,
                    'y': 2,
                    'orientation': 1,
                    'msg_action_verb': 'flip'
                },  # 1 - door circuit toggleswitch
            ],
            'devices': [
                {
                    'id': 0,
                    'name': 'entrance door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': True,
                    'x': 4,
                    'y': 8,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # 0 - entrance door
                {
                    'id': 1,
                    'name': 'exit door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': True,
                    'x': 4,
                    'y': 0,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': [
                        {'device_id': 2, 'enabled_state': True, 'active_state': True}
                    ]
                },  # 1 - exit door
                {
                    'id': 2,
                    'name': 'door circuit switch',
                    'description': 'door circuit',
                    'type': 'switch',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': False,
                    'x': 0,
                    'y': 2,
                    'msg_action_true': 'close',
                    'msg_action_false': 'open',
                    'msg_active_true': 'The circuit is closed.',
                    'msg_active_false': 'The circuit is open.',
                    'msg_toggle_active_true': 'Do you hear that? It sounds like electric current.',
                    'msg_toggle_active_false': 'That electric hum went away.',
                    'msg_unmet_dependencies': 'The circuit switch isn\'t responding.',
                    'dependencies': []
                },  # 2 - door circuit
            ],
            'properties': [],
            'links': [
                {'interface_id': 0, 'device_id': 1}
            ],
            'relates': [],
            'deaths': []
        }
    },  # equipment
    4: {
        'name': 'Crew',
        'map': {
            'x_dimension': 9,
            'y_dimension': 7,
            'path_cells': [
                {'coordinates': (2, 4), 'story': None},
                {'coordinates': (3, 4), 'story': None},
                {'coordinates': (4, 4), 'story': None},
                {'coordinates': (5, 4), 'story': None},
                {'coordinates': (6, 4), 'story': None},
                {'coordinates': (2, 3), 'story': None},
                {'coordinates': (6, 3), 'story': None},
                {'coordinates': (2, 2), 'story': None},
                {'coordinates': (3, 2), 'story': None},
                {'coordinates': (4, 2), 'story': None},
                {'coordinates': (5, 2), 'story': None},
                {'coordinates': (6, 2), 'story': None},
                {'coordinates': (4, 5), 'story': {
                    'title': None,
                    'text': ('{0} called out as he stepped through the broken door, it\'s safety mechanism drawing it '
                             'closed behind him, "Hello? Tonia, Jim, is there anybody here?" Nothing. There was '
                             'grey-blue smoke lingering in the air and the lights were out on the opposite side of the '
                             'crew room. {0} considered getting his suit but realized there was no way back. The door '
                             'couldn\'t be forced from this side. He stepped toward the meeting table cautiously, '
                             'scanning for any clue that might explain what was happening.').format(
                        player_config['name'])}},  # level entrance
                {'coordinates': (4, 6), 'story': None},
                {'coordinates': (4, 0), 'story': None},
                {'coordinates': (4, 1), 'story': None},
                {'coordinates': (1, 3), 'story': {
                    'title': None,
                    'text': '{0} looked out the habitat window. He could see the opposing crater rim about a kilometer '
                            'away. He often thought they were lucky that The Agency selected this site. The lake that '
                            'once filled the crater had escaped eons ago when a portion of the crater wall collapsed, '
                            'leaving behind a passable access route. A last remnant of the lake still existed as tons '
                            'of water ice along the perpetually shaded southern wall while near the center of the '
                            'crater the stirling reactors produced power for the habitat at a safe distance. The hab '
                            'itself, nestled along the northeastern wall, adjacent to the subterranean portion of the '
                            'base, was well protected from the prevailing, dusty winds above.'.format(
                        player_config['name'])}},  # window view
                {'coordinates': (7, 3), 'story': None},
                {'coordinates': (8, 3), 'story': None}
            ],
            'coord_enter': (4, 5),
            'coord_exit': (8, 3),
            'orientation_enter': 0,
            'tools': [],
            'parts': [
                {
                    'type': 'wires',
                    'name': 'wires',
                    'description': 'bundle of wires',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': True,
                    'blocking': False,
                    'x': 4,
                    'y': 0
                }  # bundle of wires
            ],
            'artifacts': [
                {
                    'type': 'generic',
                    'name': 'window',
                    'description': 'window',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 0,
                    'y': 3
                },  # window
                {  # use artifact to make debris pile blocking
                    'type': 'generic',
                    'name': 'debris',
                    'description': 'pile of debris',
                    'report': '',
                    'inspectable': False,
                    'visible': False,
                    'interactive': False,
                    'blocking': True,
                    'x': 4,
                    'y': 0
                },  # pile of debris
                {
                    'type': 'generic',
                    'name': 'blood',
                    'description': 'red stain on the wall',
                    'report': 'There are several dark red streaks running around the corner and fading as they run along the wall.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 5,
                    'y': 1
                },  # blood stain
                {
                    'type': 'generic',
                    'name': 'table',
                    'description': 'table',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 4,
                    'y': 3
                },  # table
                {
                    'type': 'generic',
                    'name': 'table',
                    'description': 'table',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 5,
                    'y': 3
                },  # table
                {
                    'type': 'generic',
                    'name': 'coffee',
                    'description': 'cup of coffee spilled on the table',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 3,
                    'y': 3
                }  # coffee
            ]
        },
        'system': {
            'interfaces': [
                {  # use interface to make debris pile interactive
                    'id': 0,
                    'name': 'debris',
                    'description': 'pile of debris',
                    'type': 'toggleswitch',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 4,
                    'y': 0,
                    'orientation': 2,
                    'msg_action_verb': 'clear'
                },  # 0 - pile of debris
                {
                    'id': 1,
                    'name': 'exit door button',
                    'description': 'button',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 7,
                    'y': 2,
                    'orientation': 2,
                    'msg_action_verb': 'push'
                }  # 1 - exit door button
            ],
            'devices': [
                {
                    'id': 0,
                    'name': 'entrance door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': True,
                    'x': 4,
                    'y': 6,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # 0 - entrance door
                {
                    'id': 1,
                    'name': 'exit door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': True,
                    'x': 8,
                    'y': 3,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': [
                        {'device_id': 3, 'enabled_state': True, 'active_state': True}
                    ]
                },  # 1 - exit door
                {  # use device to model wall that fails when debris pile is used
                    'id': 2,
                    'name': 'wall',
                    'description': 'wall',
                    'type': 'switch',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': False,
                    'x': 0,
                    'y': 0,
                    'msg_action_true': 'close',
                    'msg_action_false': 'open',
                    'msg_active_true': 'The switch is closed.',
                    'msg_active_false': 'The switch is open.',
                    'msg_toggle_active_true': 'The switch closed.',
                    'msg_toggle_active_false': 'The switch opened.',
                    'msg_unmet_dependencies': 'The switch is unresponsive.',
                    'dependencies': []
                },  # 2 - wall
                {
                    'id': 3,
                    'name': 'switchbox',
                    'description': 'exposed switchbox',
                    'type': 'switch',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': True,
                    'visible': True,
                    'x': 6,
                    'y': 1,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The switch is open.',
                    'msg_active_false': 'The switch is closed.',
                    'msg_toggle_active_true': 'The switch opened.',
                    'msg_toggle_active_false': 'The switch closed.',
                    'msg_unmet_dependencies': 'The switch is unresponsive.',
                    'dependencies': []
                }  # 3 - exposed switchbox
            ],
            'properties': [],
            'links': [
                {'interface_id': 0, 'device_id': 2},
                {'interface_id': 1, 'device_id': 1}
            ],
            'relates': [],
            'deaths': [
                {
                    'configuration': [
                        {'device_id': 2, 'active_state': True}
                    ],
                    'description': 'The habitat wall failed catastrophically and you were blown into the frigid near-vacuum of the Martian landscape.',
                    'location': None  # None if all locations are valid
                }
            ]
        }
    },  # crew
    5: {
        'name': 'Galley',
        'map': {
            'x_dimension': 9,
            'y_dimension': 9,
            'path_cells': [
                {'coordinates': (0, 4), 'story': None},
                {'coordinates': (1, 1), 'story': None},
                {'coordinates': (1, 2), 'story': None},
                {'coordinates': (1, 3), 'story': None},
                {'coordinates': (1, 4), 'story': {'title': None, 'text': 'As he entered Alpha Point\'s modest galley, Marcus suddenly felt like he\'d stepped over a ledge. He instinctively swung his arms forward in a desparate attempt to regain solid ground but his reaction had little effect and he grasped wildly at the air as he fell to the floor. Marcus flattened himself against the floor and spread his extremities in search of stability. After a few moments, the feeling evaporated as quickly as it had come on and Marcus found himself staring in adrenaline-spiked confusion at the shifting, contorted door at the opposite end of the module. A shimmering, translucent surface passed away from him, through the wall, and out of sight. Marcus carefully picked himself up, wondering what in the world had just happened.'}},
                {'coordinates': (1, 5), 'story': None},
                {'coordinates': (1, 6), 'story': None},
                {'coordinates': (1, 7), 'story': None},
                {'coordinates': (2, 1), 'story': None},
                {'coordinates': (2, 3), 'story': None},
                {'coordinates': (2, 4), 'story': None},
                {'coordinates': (2, 5), 'story': None},
                {'coordinates': (2, 7), 'story': None},
                {'coordinates': (3, 1), 'story': None},
                {'coordinates': (3, 3), 'story': None},
                {'coordinates': (3, 4), 'story': None},
                {'coordinates': (3, 5), 'story': None},
                {'coordinates': (3, 7), 'story': None},
                {'coordinates': (4, 1), 'story': None},
                {'coordinates': (4, 2), 'story': None},
                {'coordinates': (4, 3), 'story': None},
                {'coordinates': (4, 4), 'story': None},
                {'coordinates': (4, 5), 'story': None},
                {'coordinates': (4, 6), 'story': None},
                {'coordinates': (4, 7), 'story': None},
                {'coordinates': (5, 1), 'story': None},
                {'coordinates': (5, 3), 'story': None},
                {'coordinates': (5, 4), 'story': None},
                {'coordinates': (5, 5), 'story': None},
                {'coordinates': (5, 7), 'story': None},
                {'coordinates': (6, 1), 'story': None},
                {'coordinates': (6, 3), 'story': None},
                {'coordinates': (6, 4), 'story': None},
                {'coordinates': (6, 5), 'story': None},
                {'coordinates': (6, 7), 'story': None},
                {'coordinates': (7, 1), 'story': None},
                {'coordinates': (7, 2), 'story': None},
                {'coordinates': (7, 3), 'story': None},
                {'coordinates': (7, 4), 'story': None},
                {'coordinates': (7, 5), 'story': None},
                {'coordinates': (7, 6), 'story': None},
                {'coordinates': (7, 7), 'story': None},
                {'coordinates': (8, 4), 'story': None}
            ],
            'coord_enter': (1, 4),
            'coord_exit': (8, 4),
            'orientation_enter': 1,
            'tools': [],
            'parts': [],
            'artifacts': [
                {
                    'type': 'generic',
                    'name': 'table',
                    'description': 'table',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 2,
                    'y': 6
                },  # table
                {
                    'type': 'generic',
                    'name': 'table',
                    'description': 'table',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 3,
                    'y': 6
                },  # table
                {
                    'type': 'generic',
                    'name': 'table',
                    'description': 'table',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 5,
                    'y': 6
                },  # table
                {
                    'type': 'generic',
                    'name': 'table',
                    'description': 'table',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 6,
                    'y': 6
                },  # table
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 2,
                    'y': 2
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 3,
                    'y': 2
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 5,
                    'y': 2
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 6,
                    'y': 2
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 0,
                    'y': 1
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 0,
                    'y': 2
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 1,
                    'y': 0
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 2,
                    'y': 0
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 3,
                    'y': 0
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 4,
                    'y': 0
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 5,
                    'y': 0
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 6,
                    'y': 0
                },  # counter
                {
                    'type': 'generic',
                    'name': 'counter',
                    'description': 'metal counter',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': True,
                    'x': 7,
                    'y': 0
                },  # counter
                {
                    'type': 'generic',
                    'name': 'knife',
                    'description': 'knife',
                    'report': 'A stainless steel kitchen knife.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': True,
                    'blocking': False,
                    'x': 2,
                    'y': 2
                },  # knife
                {
                    'type': 'generic',
                    'name': 'microwave',
                    'description': 'microwave',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 4,
                    'y': 0
                },  # microwave
                {
                    'type': 'generic',
                    'name': 'handprint',
                    'description': 'bloody hand print',
                    'report': 'It looks like a partial, bloody hand print at the edge of the table and there are a few drops of what looks like dried blood on the floor.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 5,
                    'y': 6
                }  # bloody hand print
            ]
        },
        'system': {
            'interfaces': [
                {
                    'id': 0,
                    'name': 'exit door button',
                    'description': 'button',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 8,
                    'y': 4,
                    'orientation': 3,
                    'msg_action_verb': 'push'
                },  # 0 - exit door button
                {
                    'id': 1,
                    'name': 'system',
                    'description': 'system terminal',
                    'type': 'terminal',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': True,
                    'x': 4,
                    'y': 8,
                    'orientation': 0,
                    'msg_action_verb': 'log in to'
                }  # system terminal
            ],
            'devices': [
                {
                    'id': 0,
                    'name': 'entrance door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': True,
                    'x': 0,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # 0 - entrance door
                {
                    'id': 1,
                    'name': 'exit door',
                    'description': 'exit door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': True,
                    'x': 8,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                }  # 1 - exit door
            ],
            'properties': [],
            'links': [
                {'interface_id': 0, 'device_id': 1},
                {'interface_id': 1, 'device_id': 1}
            ],
            'relates': [],
            'deaths': []
        }
    },  # galley
    6: {
        'name': 'Quarters',
        'map': {
            'x_dimension': 9,
            'y_dimension': 9,
            'path_cells': [
                {'coordinates': (0, 4), 'story': None},
                {'coordinates': (1, 4), 'story': {'title': None, 'text': 'Quarters story...'}},
                {'coordinates': (2, 4), 'story': None},
            ],
            'coord_enter': (1, 4),
            'coord_exit': (2, 4),
            'orientation_enter': 1,
            'tools': [],
            'parts': [],
            'artifacts': []
        },
        'system': {
            'interfaces': [
                {
                    'id': 0,
                    'name': 'exit door button',
                    'description': 'button',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 1,
                    'y': 3,
                    'orientation': 2,
                    'msg_action_verb': 'push'
                }  # 0 - exit door button
            ],
            'devices': [
                {
                    'id': 0,
                    'name': 'entrance door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': True,
                    'x': 0,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # 0 - entrance door
                {
                    'id': 1,
                    'name': 'exit door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': True,
                    'x': 2,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                }  # 1 - exit door
            ],
            'properties': [],
            'links': [
                {'interface_id': 0, 'device_id': 1}
            ],
            'relates': [],
            'deaths': []
        }
    },  # quarters
    7: {
        'name': 'Wet Lab',
        'map': {
            'x_dimension': 9,
            'y_dimension': 9,
            'path_cells': [
                {'coordinates': (0, 4), 'story': None},
                {'coordinates': (1, 4), 'story': {'title': None, 'text': 'Wet lab story...'}},
                {'coordinates': (2, 4), 'story': None},
            ],
            'coord_enter': (1, 4),
            'coord_exit': (2, 4),
            'orientation_enter': 1,
            'tools': [],
            'parts': [],
            'artifacts': []
        },
        'system': {
            'interfaces': [
                {
                    'id': 0,
                    'name': 'exit door button',
                    'description': 'button',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 1,
                    'y': 3,
                    'orientation': 2,
                    'msg_action_verb': 'push'
                }  # 0 - exit door button
            ],
            'devices': [
                {
                    'id': 0,
                    'name': 'entrance door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': True,
                    'x': 0,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # 0 - entrance door
                {
                    'id': 1,
                    'name': 'exit door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': True,
                    'x': 2,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                }  # 1 - exit door
            ],
            'properties': [],
            'links': [
                {'interface_id': 0, 'device_id': 1}
            ],
            'relates': [],
            'deaths': []
        }
    },  # wet lab
    8: {
        'name': 'Dry Lab',
        'map': {
            'x_dimension': 9,
            'y_dimension': 9,
            'path_cells': [
                {'coordinates': (0, 4), 'story': None},
                {'coordinates': (1, 4), 'story': {'title': None, 'text': 'Dry lab story...'}},
                {'coordinates': (2, 4), 'story': None},
            ],
            'coord_enter': (1, 4),
            'coord_exit': (2, 4),
            'orientation_enter': 1,
            'tools': [],
            'parts': [],
            'artifacts': []
        },
        'system': {
            'interfaces': [
                {
                    'id': 0,
                    'name': 'exit door button',
                    'description': 'button',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 1,
                    'y': 3,
                    'orientation': 2,
                    'msg_action_verb': 'push'
                }  # 0 - exit door button
            ],
            'devices': [
                {
                    'id': 0,
                    'name': 'entrance door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': True,
                    'x': 0,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # 0 - entrance door
                {
                    'id': 1,
                    'name': 'exit door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': True,
                    'x': 2,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                }  # 1 - exit door
            ],
            'properties': [],
            'links': [
                {'interface_id': 0, 'device_id': 1}
            ],
            'relates': [],
            'deaths': []
        }
    },  # dry lab
    9: {
        'name': 'Excavation',
        'map': {
            'x_dimension': 9,
            'y_dimension': 9,
            'path_cells': [
                {'coordinates': (0, 4), 'story': None},
                {'coordinates': (1, 4), 'story': {'title': None, 'text': 'Excavation story...'}},
                {'coordinates': (2, 4), 'story': None},
            ],
            'coord_enter': (1, 4),
            'coord_exit': (2, 4),
            'orientation_enter': 1,
            'tools': [],
            'parts': [],
            'artifacts': []
        },
        'system': {
            'interfaces': [
                {
                    'id': 0,
                    'name': 'exit door button',
                    'description': 'button',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 1,
                    'y': 3,
                    'orientation': 2,
                    'msg_action_verb': 'push'
                }  # 0 - exit door button
            ],
            'devices': [
                {
                    'id': 0,
                    'name': 'entrance door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': True,
                    'x': 0,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # 0 - entrance door
                {
                    'id': 1,
                    'name': 'exit door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': True,
                    'x': 2,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                }  # 1 - exit door
            ],
            'properties': [],
            'links': [
                {'interface_id': 0, 'device_id': 1}
            ],
            'relates': [],
            'deaths': []
        }
    },  # excavation
    99: {
        'name': 'Testing',
        'map': {
            'x_dimension': 5,
            'y_dimension': 5,
            'path_cells': [
                {'coordinates': (0, 4), 'story': None},
                {'coordinates': (0, 3), 'story': {'title': 'Testing', 'text': (
                    '{0} breathed a sigh of relief as the airlock sealed behind him...').format(
                    player_config['name'])}},
                {'coordinates': (0, 2), 'story': None},
                {'coordinates': (1, 2), 'story': {'title': None, 'text': (
                    'A glow emanated from the left side of the corridor ahead. "Is that a passage?", {0} wondered... ').format(
                    player_config['name'])}},
                {'coordinates': (2, 2), 'story': None},
                {'coordinates': (2, 1), 'story': None},
                {'coordinates': (3, 2), 'story': None},
                {'coordinates': (4, 2), 'story': None},
                {'coordinates': (4, 1), 'story': None},
                {'coordinates': (4, 0), 'story': None},
                {'coordinates': (4, 3), 'story': None}
            ],
            'coord_enter': (0, 3),  # begin
            'coord_exit': (4, 0),  # end
            'orientation_enter': 0,
            'tools': [],
            'parts': [
                {
                    'type': 'wires',
                    'name': 'wires',
                    'description': 'wire bundle',
                    'report': '',
                    'inspectable': False,
                    'visible': True,
                    'interactive': True,
                    'blocking': False,
                    'x': 3,
                    'y': 2
                }  # wire bundle
            ],
            'artifacts': [
                {
                    'type': 'generic',
                    'name': 'helmet_1',
                    'description': 'excursion suit helmet',
                    'report': 'It\'s a standard-issue excursion suit helmet with the name Tonia Cherneyev on the side.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': True,
                    'blocking': False,
                    'x': 0,
                    'y': 2
                }  # excursion suit helmet
            ]
        },
        'system': {
            'interfaces': [
                {
                    'id': 0,
                    'name': 'entrance door button',
                    'description': 'button',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 0,
                    'y': 4,
                    'orientation': 0,
                    'msg_action_verb': 'push'
                },  # entrance door button
                {
                    'id': 1,
                    'name': 'door circuit toggleswitch',
                    'description': 'switch',
                    'type': 'toggleswitch',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 2,
                    'y': 0,
                    'orientation': 2,
                    'msg_action_verb': 'flip'
                },  # door circuit toggleswitch
                {
                    'id': 2,
                    'name': 'console',
                    'description': 'sensor console',
                    'type': 'console',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 0,
                    'y': 1,
                    'orientation': 2,
                    'msg_action_verb': 'use'
                },  # sensor console
                {
                    'id': 3,
                    'name': 'system',
                    'description': 'system terminal',
                    'type': 'terminal',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': True,
                    'x': 4,
                    'y': 4,
                    'orientation': 0,
                    'msg_action_verb': 'use'
                },  # system terminal
                {
                    'id': 4,
                    'name': 'exit door button',
                    'description': 'button',
                    'type': 'button',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'corrupt': False,
                    'x': 4,
                    'y': 0,
                    'orientation': 2,
                    'msg_action_verb': 'push'
                }  # exit door button
            ],
            'devices': [
                {
                    'id': 0,
                    'name': 'entrance door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': True,
                    'x': 0,
                    'y': 4,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # entrance door
                {
                    'id': 1,
                    'name': 'door circuit switch',
                    'description': 'door circuit',
                    'type': 'switch',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': False,
                    'x': 3,
                    'y': 1,
                    'msg_action_true': 'close',
                    'msg_action_false': 'open',
                    'msg_active_true': 'The circuit is closed.',
                    'msg_active_false': 'The circuit is open.',
                    'msg_toggle_active_true': 'Do you hear that? It sounds like electric current.',
                    'msg_toggle_active_false': 'That electric hum went away.',
                    'msg_unmet_dependencies': 'The circuit switch isn\'t responding.',
                    'dependencies': []
                },  # door circuit switch
                {
                    'id': 2,
                    'name': 'exit door',
                    'description': 'door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': True,
                    'x': 4,
                    'y': 0,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'The door is open.',
                    'msg_active_false': 'The door is closed.',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'An indicator shows the door is locked.',
                    'dependencies': [
                        {'device_id': 1, 'enabled_state': True, 'active_state': True}
                    ]
                },  # exit door
                {
                    'id': 3,
                    'name': 'exit door camera',
                    'description': 'security camera',
                    'type': 'camera',
                    'report': 'It\'s a small visible-band security camera.',
                    'inspectable': True,
                    'enabled': True,
                    'active': True,
                    'visible': True,
                    'x': 4,
                    'y': 0,
                    'msg_action_true': 'turn on',
                    'msg_action_false': 'turn off',
                    'msg_active_true': 'The camera is on.',
                    'msg_active_false': 'The camera is off.',
                    'msg_toggle_active_true': 'The camera viewer flashed on and I see a man standing at a terminal.',
                    'msg_toggle_active_false': 'The camera viewer went dark.',
                    'msg_unmet_dependencies': 'The camera isn\'t responding.',
                    'dependencies': []
                },  # security camera
                {
                    'id': 4,
                    'name': 'door circuit switch',
                    'description': 'door circuit',
                    'type': 'switch',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': False,
                    'x': 3,
                    'y': 1,
                    'msg_action_true': 'close',
                    'msg_action_false': 'open',
                    'msg_active_true': 'The circuit is closed.',
                    'msg_active_false': 'The circuit is open.',
                    'msg_toggle_active_true': 'Do you hear that? It sounds like electric current.',
                    'msg_toggle_active_false': 'That electric hum went away.',
                    'msg_unmet_dependencies': 'The circuit switch isn\'t responding.',
                    'dependencies': []
                },  # door circuit switch
                {
                    'id': 5,
                    'name': 'voltage sensor',
                    'description': 'circuit voltage sensor',
                    'type': 'sensor',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': True,
                    'visible': False,
                    'x': 3,
                    'y': 1,
                    'msg_action_true': 'turn on',
                    'msg_action_false': 'turn off',
                    'msg_active_true': 'The sensor is on.',
                    'msg_active_false': 'The sensor is off.',
                    'msg_toggle_active_true': 'The sensor turned on.',
                    'msg_toggle_active_false': 'THe sensor turned off.',
                    'msg_unmet_dependencies': 'The sensor is inoperable.',
                    'dependencies': []
                },  # voltage sensor
                {
                    'id': 6,
                    'name': 'pressure sensor',
                    'description': 'outside pressure sensor',
                    'type': 'sensor',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': True,
                    'visible': False,
                    'x': 3,
                    'y': 1,
                    'msg_action_true': 'turn on',
                    'msg_action_false': 'turn off',
                    'msg_active_true': 'The sensor is on.',
                    'msg_active_false': 'The sensor is off.',
                    'msg_toggle_active_true': 'The sensor turned on.',
                    'msg_toggle_active_false': 'THe sensor turned off.',
                    'msg_unmet_dependencies': 'The sensor is inoperable.',
                    'dependencies': []
                },  # pressure sensor
            ],
            'properties': [
                {
                    'id': 0,
                    'name': 'voltage',
                    'description': 'door circuit voltage',
                    'type': 'voltage',
                    'value': 5,
                    'min_value': 0,
                    'max_value': 10,
                    'units': 'V',
                    'increment': 2,
                },  # voltage
                {
                    'id': 1,
                    'name': 'pressure',
                    'description': 'outside pressure',
                    'type': 'pressure',
                    'value': 40,
                    'min_value': 0,
                    'max_value': 50,
                    'units': 'Pa',
                    'increment': 0,
                }  # pressure
            ],
            'links': [
                {'interface_id': 0, 'device_id': 0},
                {'interface_id': 1, 'device_id': 1},
                {'interface_id': 1, 'device_id': 4},
                {'interface_id': 2, 'device_id': 5},
                {'interface_id': 2, 'device_id': 6},
                {'interface_id': 3, 'device_id': 1},
                {'interface_id': 3, 'device_id': 2},
                {'interface_id': 3, 'device_id': 3},
                {'interface_id': 4, 'device_id': 2}
            ],
            'relates': [
                {'device_id': 1, 'property_id': 0},
                {'device_id': 2, 'property_id': 1},
                {'device_id': 4, 'property_id': 0},
                {'device_id': 5, 'property_id': 0},
                {'device_id': 6, 'property_id': 1}
            ],
            'deaths': []
        }
    },  # testing
}