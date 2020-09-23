from config.player_config import player_config

level_config = {
    1: {
        'name': 'Approach',
        'map': {
            'x_dimension': 7,
            'y_dimension': 5,
            'path_cells': [
                {'coordinates': (3, 4), 'story': None},
                {'coordinates': (3, 3), 'story': {'title': None,
                                                  'text': 'Faint clouds of dust fell from his boots as {0} climbed down the rover ladder. "Something\'s wrong", he thought, while surveying his surroundings for any sign of a problem. Everything was in place. There was no evidence of an explosion or collapse. The light over the external airlock door glowed green indicating its pressure matched that of the outside environment. According to his suit\'s computer, he still had active comm and telemetry links with Alpha Point but all he could hear was the sound of his own breathing. "What the hell?", {0} wondered, as he headed toward the airlock.'.format(
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
        },
        'weather': {
            'sol': '609',
            'time': '12:05:41',
            'temperature': {
                'value': -59.957,
                'units': 'C'},
            'wind': {
                'speed': {
                    'value': 7.958,
                    'units': 'KPH'},
                'direction': {
                    'value': 292.5,
                    'units': 'Deg'}},
            'pressure': {
                'value': 789.166,
                'units': 'Pa'}
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
                    '{0} checked his mission clock as the door sealed behind him and noticed that he was about ten minutes ahead of schedule. His fledgling concerns had matured into real worry over the past half hour and he could feel his heart pounding in his chest. "Alright, focus.", he thought, "Follow the ingress procedure."').format(
                    player_config['name'])}},
                {'coordinates': (1, 4), 'story': None}
            ],
            'coord_enter': (1, 3),  # begin
            'coord_exit': (1, 0),  # end
            'orientation_enter': 0,
            'tools': [],
            'parts': [],
            'artifacts': [
                {
                    'type': 'generic',
                    'name': 'placard',
                    'description': 'warning placard',
                    'report': 'WARNING - Use manual override only in emergency. If automated environment management system is not functional, contact base control for assistance.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 0,
                    'y': 2
                }
            ]
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
                    'x': 0,
                    'y': 3,
                    'orientation': 1,
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
                    'y': 2,
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'description': 'Alarms sound in the attached module as air rushes out of the open valve. The gravity of your mistake hits you hard. You just depressurized the habitat. As a fog of panic envelopes your mind you desparately wish you could go back and make a different choice.',
                    'location': None}  # None if all locations are valid
            ]
        },
        'weather': {
            'sol': '609',
            'time': '12:05:41',
            'temperature': {
                'value': -59.957,
                'units': 'C'},
            'wind': {
                'speed': {
                    'value': 7.958,
                    'units': 'KPH'},
                'direction': {
                    'value': 292.5,
                    'units': 'Deg'}},
            'pressure': {
                'value': 789.166,
                'units': 'Pa'}
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
                                                  'text': 'As he removed his helmet, {0} noticed an empty excursion suit alcove and wondered who else was outside the hab. Ad-hoc departures weren\'t that unusual. Even Martian research stations have fences that need mending. The lights flickered briefly and {0} detected the caustic smell of overheated electronics. "That can\'t be good", he told himself. After stowing his suit in an open alcove {0} headed past rows of storage shelves toward the door of the crew meeting area at the far end of the equipment module.'.format(
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
                    'inspectable': True,
                    'visible': True,
                    'interactive': True,
                    'blocking': False,
                    'x': 2,
                    'y': 3
                }  # prybar
            ],
            'parts': [
                {
                    'type': 'wires',
                    'name': 'wire_bundle',
                    'description': 'bundle of wires and circuitry',
                    'report': 'A small circuit board with multi-colored wires attached.',
                    'inspectable': True,
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
                },  # excursion suit helmet
                {
                    'type': 'generic',
                    'name': 'sticky_note',
                    'description': 'sticky note on the terminal',
                    'report': 'Not sure why we changed them but just type "help" if you forget the manual commands. At least we don\'t have to type full device IDs anymore. To all the other non-comps, you\'re welcome.\n\n-Emilia',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 1,
                    'y': 1
                },  # sticky note
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
                    'name': 'maintenance terminal',
                    'description': 'system terminal',
                    'type': 'terminal',
                    'report': 'A system terminal labeled "Maintenance Bay - Remote".',
                    'inspectable': True,
                    'enabled': True,
                    'corrupt': False,
                    'x': 1,
                    'y': 1,
                    'orientation': 2,
                    'msg_action_verb': 'use'
                },  # 1 - maintenance bay terminal
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': [
                        {'device_id': 2, 'enabled_state': True, 'active_state': True}
                    ]
                },  # 1 - exit door
                {
                    'id': 2,
                    'name': 'exit door circuit',
                    'description': 'exit door circuit',
                    'type': 'switch',
                    'report': '',
                    'inspectable': False,
                    'enabled': False,
                    'active': False,
                    'visible': False,
                    'x': 5,
                    'y': 1,
                    'msg_action_true': 'close',
                    'msg_action_false': 'open',
                    'msg_active_true': 'closed',
                    'msg_active_false': 'open',
                    'msg_toggle_active_true': 'The switch closed.',
                    'msg_toggle_active_false': 'The switch opened.',
                    'msg_unmet_dependencies': 'The switch is unresponsive.',
                    'dependencies': []
                },  # 2 - exit door switch
                {
                    'id': 3,
                    'name': 'maintenance bay access door',
                    'description': 'door',
                    'type': 'door',
                    'report': 'The door is labeled "Maintenance Bay Access". There\'s a rover and [device-4] visible on the other side.',
                    'inspectable': True,
                    'enabled': False,
                    'active': False,
                    'visible': True,
                    'x': 0,
                    'y': 2,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # 3 - maintenance bay access door
                {
                    'id': 4,
                    'name': 'maintenance bay main door',
                    'description': 'bay door',
                    'type': 'door',
                    'report': '',
                    'inspectable': False,
                    'enabled': True,
                    'active': False,
                    'visible': False,
                    'x': 0,
                    'y': 0,
                    'msg_action_true': 'open',
                    'msg_action_false': 'close',
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
                    'msg_toggle_active_true': 'The large bay door opened.',
                    'msg_toggle_active_false': 'The large bay door closed.',
                    'msg_unmet_dependencies': 'The bay door is unresponsive.',
                    'dependencies': []
                }   # 4 - maintenance bay main doors
            ],
            'properties': [],
            'links': [
                {'interface_id': 0, 'device_id': 1},
                {'interface_id': 1, 'device_id': 3},
                {'interface_id': 1, 'device_id': 4}
            ],
            'relates': [],
            'deaths': []
        },
        'weather': {
            'sol': '609',
            'time': '12:05:41',
            'temperature': {
                'value': -59.957,
                'units': 'C'},
            'wind': {
                'speed': {
                    'value': 7.958,
                    'units': 'KPH'},
                'direction': {
                    'value': 292.5,
                    'units': 'Deg'}},
            'pressure': {
                'value': 789.166,
                'units': 'Pa'}
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
                             'looking for any clue that might explain what was happening.').format(
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
                    'description': 'wiring',
                    'report': 'Some wires attached to a light that looks like it was pulled from the ceiling.',
                    'inspectable': True,
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
                    'report': 'A pile of various equipment and furniture, including some lighting that was mounted to the ceiling.',
                    'inspectable': True,
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'msg_active_true': 'closed',
                    'msg_active_false': 'open',
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
                    'report': 'The box panel is missing, and you can see some electrical components and wiring.',
                    'inspectable': True,
                    'enabled': False,
                    'active': True,
                    'visible': True,
                    'x': 6,
                    'y': 1,
                    'msg_action_true': 'close',
                    'msg_action_false': 'open',
                    'msg_active_true': 'closed',
                    'msg_active_false': 'open',
                    'msg_toggle_active_true': 'The switch closed.',
                    'msg_toggle_active_false': 'The switch opened.',
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
                    'description': 'As you strain to move a large piece of debris there is a sudden bang that sends you tumbling out of a gaping hole in the habitat wall. Your vision fades to red and then black as you claw in agony at the rusty red grit of the crater floor. Perhaps in another life you made a wiser choice.',
                    'location': None  # None if all locations are valid
                }
            ]
        },
        'weather': {
            'sol': '609',
            'time': '12:05:41',
            'temperature': {
                'value': -59.957,
                'units': 'C'},
            'wind': {
                'speed': {
                    'value': 7.958,
                    'units': 'KPH'},
                'direction': {
                    'value': 292.5,
                    'units': 'Deg'}},
            'pressure': {
                'value': 789.166,
                'units': 'Pa'}
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
                {'coordinates': (1, 4), 'story': {'title': None, 'text': 'As he entered Alpha Point\'s modest galley, Marcus suddenly felt like he\'d stepped over a ledge. He instinctively swung his arms forward in a desparate attempt to regain solid ground but his reaction had little effect and he grasped wildly at the air as he fell to the floor. Marcus flattened himself against the cold, sulfur-concrete tiles, spreading his arms and legs in search of stability. After a few moments, his disorientation evaporated as quickly as it had come on and Marcus found himself staring in adrenaline-spiked confusion at the shifting, contorted door at the opposite end of the module. A shimmering surface passed away from him, through the wall, and out of sight. Marcus carefully picked himself up, wondering what in the world had just happened.'}},
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
                    'name': 'cutting_board',
                    'description': 'cutting board',
                    'report': 'A cutting board with some chopped water cress on it.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 2,
                    'y': 2
                },  # cutting board
                {
                    'type': 'generic',
                    'name': 'microwave',
                    'description': 'microwave oven',
                    'report': 'A small microwave oven with a bowl inside.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 4,
                    'y': 0
                },  # microwave
                {
                    'type': 'generic',
                    'name': 'cook_surface',
                    'description': 'cook surface',
                    'report': 'A slightly dirty glass cook surface.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 4,
                    'y': 0
                },  # cook surface
                {
                    'type': 'generic',
                    'name': 'handprint',
                    'description': 'bloody hand print',
                    'report': 'It looks like a partial, bloody hand print at the edge of the table and there are a few drops of dried blood on the floor.',
                    'inspectable': True,
                    'visible': True,
                    'interactive': False,
                    'blocking': False,
                    'x': 5,
                    'y': 6
                },  # bloody hand print
                {
                    'type': 'generic',
                    'name': 'tablet',
                    'description': 'unlocked tablet',
                    'report': 'A tablet computer with a partially written email on screen.\n\nFrom: Emilia Perez\nTo: James O\'Reilly\n\nHey Jim,\n\nQuantum gravimeter readings from the bore site suggest denser material than we were expecting from our geological surveys. Tonia gave the go ahead to continue but we expect progress to slow soon. It\'s unfortunate but it\'s not like we have an',
                    'inspectable': True,
                    'visible': True,
                    'interactive': True,
                    'blocking': False,
                    'x': 2,
                    'y': 6
                }  # tablet
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
                    'x': 8,
                    'y': 5,
                    'orientation': 3,
                    'msg_action_verb': 'log in to'
                }  # 1 system terminal
            ],
            'devices': [
                {
                    'id': 0,
                    'name': 'crew planning door',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                },  # 0 - entrance door
                {
                    'id': 1,
                    'name': 'crew quarters door',
                    'description': 'door',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
                    'msg_toggle_active_true': 'The door opened.',
                    'msg_toggle_active_false': 'The door closed.',
                    'msg_unmet_dependencies': 'The door is unresponsive.',
                    'dependencies': []
                }  # 1 - exit door
            ],
            'properties': [],
            'links': [
                # {'interface_id': 0, 'device_id': 1},
                {'interface_id': 1, 'device_id': 1}
            ],
            'relates': [],
            'deaths': []
        },
        'weather': {
            'sol': '609',
            'time': '12:05:41',
            'temperature': {
                'value': -59.957,
                'units': 'C'},
            'wind': {
                'speed': {
                    'value': 7.958,
                    'units': 'KPH'},
                'direction': {
                    'value': 292.5,
                    'units': 'Deg'}},
            'pressure': {
                'value': 789.166,
                'units': 'Pa'}
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
        },
        'weather': {
            'sol': '609',
            'time': '12:05:41',
            'temperature': {
                'value': -59.957,
                'units': 'C'},
            'wind': {
                'speed': {
                    'value': 7.958,
                    'units': 'KPH'},
                'direction': {
                    'value': 292.5,
                    'units': 'Deg'}},
            'pressure': {
                'value': 789.166,
                'units': 'Pa'}
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
        },
        'weather': {
            'sol': '609',
            'time': '12:05:41',
            'temperature': {
                'value': -59.957,
                'units': 'C'},
            'wind': {
                'speed': {
                    'value': 7.958,
                    'units': 'KPH'},
                'direction': {
                    'value': 292.5,
                    'units': 'Deg'}},
            'pressure': {
                'value': 789.166,
                'units': 'Pa'}
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
        },
        'weather': {
            'sol': '609',
            'time': '12:05:41',
            'temperature': {
                'value': -59.957,
                'units': 'C'},
            'wind': {
                'speed': {
                    'value': 7.958,
                    'units': 'KPH'},
                'direction': {
                    'value': 292.5,
                    'units': 'Deg'}},
            'pressure': {
                'value': 789.166,
                'units': 'Pa'}
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
        },
        'weather': {
            'sol': '609',
            'time': '12:05:41',
            'temperature': {
                'value': -59.957,
                'units': 'C'},
            'wind': {
                'speed': {
                    'value': 7.958,
                    'units': 'KPH'},
                'direction': {
                    'value': 292.5,
                    'units': 'Deg'}},
            'pressure': {
                'value': 789.166,
                'units': 'Pa'}
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
                    'report': 'A standard-issue excursion suit helmet with the name Tonia Cherneyev on the side.',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'msg_active_true': 'closed',
                    'msg_active_false': 'open',
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
                    'msg_active_true': 'open',
                    'msg_active_false': 'closed',
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
                    'report': 'A small visible-band security camera.',
                    'inspectable': True,
                    'enabled': True,
                    'active': True,
                    'visible': True,
                    'x': 4,
                    'y': 0,
                    'msg_action_true': 'turn on',
                    'msg_action_false': 'turn off',
                    'msg_active_true': 'on',
                    'msg_active_false': 'off',
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
                    'msg_active_true': 'closed',
                    'msg_active_false': 'open',
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
                    'msg_active_true': 'on',
                    'msg_active_false': 'off',
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
                    'msg_active_true': 'on',
                    'msg_active_false': 'off',
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
        },
        'weather': {
            'sol': '609',
            'time': '12:05:41',
            'temperature': {
                'value': -59.957,
                'units': 'C'},
            'wind': {
                'speed': {
                    'value': 7.958,
                    'units': 'KPH'},
                'direction': {
                    'value': 292.5,
                    'units': 'Deg'}},
            'pressure': {
                'value': 789.166,
                'units': 'Pa'}
        }
    }  # testing
}
