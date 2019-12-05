player_config = {
    'name': 'Marcus'
}

game_config = {
    'splash_text': ''' 
 _____   _       ____    _    _   _____ 
|  _  | | |     |  _ \  | |  | | |  _  |
| |_| | | |     | |_| | | |__| | | |_| |
|  _  | | |___  |  __/  |  __  | |  _  |
|_| |_| |_____| |_|     |_|  |_| |_| |_|
 ____    _____    _    __   _   _______ 
|  _ \  |  _  |  | |  |  \ | | |__   __|
| |_| | | | | |  | |  |   \| |    | |   
|  __/  | |_| |  | |  | |\   |    | |   
|_|     |_____|  |_|  |_| \__|    |_|   

''',
    'gameover_text': 'Congratulations! You completed the game',
    'intro_text_1': '{0} could sense the stillness of his environment -- vacuous and oppressive. Intense sunlight cut sharp-edged lines across the dusty, red rocks at his feet. Above, a high, streaky haze blurred the tawny blue and grey of the sky. In every direction there was more of the same: rocks, dust, and light; repeating, shrinking, and finally vanishing at the horizon.  In this place time itself was like a distant memory and the slow turn of shadows across the landscape was the only reminder that it still existed. There was no movement; no gentle breeze, no flowing water, no bounding life; only a vast, empty expanse -- in a word, desolation.'.format(player_config['name']),
    'intro_text_2': '{0}\' integrated comm system chirped. "Marc, we need you back at base ASAP! There\'s been an incident in the lab", said his mission commander. He shifted his gaze to the top-left corner of his suit\'s heads-up-display and keyed his mic with a blink. "Roger that, Tonia, what kind of incident?" Even as he finished speaking, {0} began gathering and packing his instruments. "We don\'t know yet, but it doesn\'t look good", Tonia replied, her Russian accent a little thicker than usual. "One of the techs made a system-wide call warning everyone to stay away. They\'ve sealed the airlock and disabled external control. We\'re still trying to re-establish contact." As chief science officer, {0} knew laboratory emergency protocols better than anyone. Things were not happening by the book. "Alright, I\'m heading back now. ETA twelve minutes. Who\'s scheduled for the lab today?", {0} asked. Eleven and a half minutes later, {0} brought his rover to a stop in front of the Horizon-1 Mars Base, informally known as Alpha Point. There was still no response...'.format(player_config['name']),
    'ui': {
        'width': 60,
        'articles': {
            'default': 'a',
            'mapped': {
                'excursion suit': 'an',
                'excursion suit helmet': 'an',
                'airlock door': 'an',
                'open door': 'an',
                'open airlock door': 'an'
            }
        }
    }
}

level_config = {
    'level': {
        99: {
            'name': 'Testing',
            'map': {
                'x_dimension': 5,
                'y_dimension': 5,
                'path_cells': [
                    {'coordinates': (0, 4), 'story': None},
                    {'coordinates': (0, 3), 'story': {'title': 'Testing', 'text': ('{0} breathed a sigh of relief as the airlock sealed behind him...').format(player_config['name'])}},
                    {'coordinates': (0, 2), 'story': None},
                    {'coordinates': (1, 2), 'story': {'title': None, 'text': ('A glow emanated from the left side of the corridor ahead. "Is that a passage?", {0} wondered... ').format(player_config['name'])}},
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
                        'visible': True,
                        'interactive': True,
                        'blocking': False,
                        'x': 3,
                        'y': 2
                    }  # wire bundle
                ],
                'artifacts': []
            },
            'system': {
                'corrupt': True,
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'entrance door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
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
                        'enabled': True,
                        'x': 2,
                        'y': 0,
                        'orientation': 2,
                        'msg_action_verb': 'flip'
                    },  # door circuit toggleswitch
                    {
                        'id': 2,
                        'name': 'system',
                        'description': 'system terminal',
                        'type': 'terminal',
                        'enabled': True,
                        'x': 4,
                        'y': 4,
                        'orientation': 0,
                        'msg_action_verb': 'use'
                    },  # system terminal
                    {
                        'id': 3,
                        'name': 'exit door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
                        'x': 4,
                        'y': 0,
                        'orientation': 2,
                        'msg_action_verb': 'push'
                    }   # exit door button
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'door',
                        'type': 'door',
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
                        'enabled': False,
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
                    }   # security camera
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 0},
                    {'interface_id': 1, 'device_id': 1},
                    {'interface_id': 2, 'device_id': 1},
                    {'interface_id': 2, 'device_id': 2},
                    {'interface_id': 2, 'device_id': 3},
                    {'interface_id': 3, 'device_id': 2}
                ],
                'deaths': [
                    {'configuration': [
                        {'device_id': 1, 'active_state': True},
                        {'device_id': 3, 'active_state': True}],
                     'description': 'The camera caused a short circuit and you were electrocuted.',
                     'location': (2, 1)}  # None if all locations are valid
                ]
            }
        },  # testing
        0: {
            'name': 'Void',
            'map': {
                'x_dimension': 1,
                'y_dimension': 2,
                'path_cells': [
                    {'coordinates': (0, 0), 'story': None},
                    {'coordinates': (0, 1), 'story': {'title': 'Void', 'text': 'This place is not for you. Run along now...'}}
                ],
                'coord_enter': (0, 1),  # begin
                'coord_exit': (0, 0),  # end
                'orientation_enter': 0,
                'tools': [],
                'parts': [],
                'artifacts': []
            },
            'system': {
                'corrupt': False,
                'interfaces': [],
                'devices': [],
                'links': [],
                'deaths': []
            }
        },  # void
        1: {
            'name': 'Approach',
            'map': {
                'x_dimension': 5,
                'y_dimension': 5,
                'path_cells': [
                    {'coordinates': (2, 4), 'story': None},
                    {'coordinates': (2, 3), 'story': {'title': None, 'text': 'Faint clouds of dust fell from his boots as {0} climbed down the rover ladder. "Something is very wrong", he thought, while surveying his surroundings for any sign of disaster. Everything was in place. There was no evidence of an explosion or collapse. The light over the external airlock door glowed green indicating its pressure matched that of the external environment. According to his suit\'s computer, he still had active comm and telemetry links with Alpha Point but all he could hear was the sound of his own breathing. "What the hell?", {0} wondered, as he headed toward the airlock.'.format(player_config['name'])}},
                    {'coordinates': (2, 2), 'story': None},
                    {'coordinates': (2, 1), 'story': None},
                    {'coordinates': (2, 0), 'story': None},
                    {'coordinates': (3, 3), 'story': None},
                    {'coordinates': (4, 3), 'story': None},
                    {'coordinates': (1, 1), 'story': None},
                    {'coordinates': (0, 1), 'story': None}
                ],
                'coord_enter': (2, 3),  # begin
                'coord_exit': (2, 0),  # end
                'orientation_enter': 0,
                'tools': [],
                'parts': [],
                'artifacts': [
                    {
                        'type': 'generic',
                        'name': 'rover',
                        'description': 'rover',
                        'report': '',
                        'inspectable': False,
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 2,
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
                        'x': 4,
                        'y': 3
                    },  # communications array
                ]
            },
            'system': {
                'corrupt': False,
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'airlock door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
                        'x': 2,
                        'y': 0,
                        'orientation': 2,
                        'msg_action_verb': 'push'
                    }  # airlock door button
                ],
                'devices': [
                    {
                        'id': 1,
                        'name': 'airlock door',
                        'description': 'airlock door',
                        'type': 'door',
                        'enabled': True,
                        'active': False,
                        'visible': True,
                        'x': 2,
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
                'links': [
                    {'interface_id': 0, 'device_id': 1}
                ],
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
                    {'coordinates': (1, 3), 'story': {'title': None, 'text': ('{0} checked his mission clock as the door sealed behind him. He was about thirty minutes ahead of his scheduled return time. "Alright, focus.", he thought, "Follow the ingress procedure."').format(player_config['name'])}},
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
                'corrupt': False,
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'airlock pressurization button',
                        'description': 'button labeled "Pressure Control"',
                        'type': 'button',
                        'enabled': True,
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
                        'enabled': True,
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
                        'enabled': True,
                        'x': 1,
                        'y': 0,
                        'orientation': 2,
                        'msg_action_verb': 'push'
                    }   # 2 - exit door button
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'airlock door',
                        'type': 'door',
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
                    }   # 2 - exit door
                ],
                'links': [
                    {'interface_id': 1, 'device_id': 1},
                    {'interface_id': 2, 'device_id': 2}
                ],
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
                    {'coordinates': (4, 7), 'story': {'title': None, 'text': 'As he removed his helmet, {0} noticed two empty excursion suit alcoves and wondered who else was outside the hab. Ad-hoc departures weren\'t that unusual. Even Martian research stations have fences that need mending. The lights flickered briefly and {0} detected the caustic smell of overheated electronics. "That can\'t be good", he told himself. After stowing his suit in an open alcove {0} headed for the door of the crew meeting area at the far end of the equipment bay.'.format(player_config['name'])}},
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
                        'report': '',
                        'inspectable': False,
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
                        'report': '',
                        'inspectable': False,
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
                        'report': '',
                        'inspectable': False,
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
                        'report': '',
                        'inspectable': False,
                        'visible': True,
                        'interactive': True,
                        'blocking': False,
                        'x': 7,
                        'y': 3
                    }   # excursion suit helmet
                ]
            },
            'system': {
                'corrupt': False,
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'exit door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
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
                        'enabled': True,
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
                'links': [
                    {'interface_id': 0, 'device_id': 1}
                ],
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
                    {'coordinates': (4, 5), 'story': {'title': None, 'text': '{0} tried again to establish radio contact as he stepped through the broken door, it\'s safety mechanism drawing it closed behind him, "Tonia, this is {0}. Do you read me? Over."...nothing. There was grey-blue smoke lingering in the air and the lights were out on the opposite side of the crew room. {0} considered getting his suit but realized there was no way back. The door couldn\'t be forced from this side. "Looks like there\'s no way out but through", he thougt as he cautiously stepped toward the meeting table.'.format(player_config['name'])}},
                    {'coordinates': (4, 6), 'story': None},
                    {'coordinates': (4, 0), 'story': None},
                    {'coordinates': (4, 1), 'story': None},
                    {'coordinates': (1, 3), 'story': {'title': None, 'text': '{0} looked out the habitat window. He could see the opposing crater rim about a kilometer away. They were lucky, he thought, that The Agency had selected this site. The lake that once filled the crater had escaped eons ago when a portion of the crater wall collapsed, leaving behind a passable access route. A last remnant of the lake still existed as tons of water ice along the perpetually shaded southern wall while near to the center of crater the stirling reactors produced power for the habitat at a safe distance. The hab itself, nestled along the northeastern wall, adjacent to the subterranean portion of the base, was well protected from the prevailing, dusty winds above.'.format(player_config['name'])}},
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
                        'description': 'bundle of wires on the floor',
                        'visible': True,
                        'interactive': True,
                        'blocking': False,
                        'x': 4,
                        'y': 1
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
                    {   # use artifact to make debris pile blocking
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
                        'report': '',
                        'inspectable': False,
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
                    }   # coffee
                ]
            },
            'system': {
                'corrupt': False,
                'interfaces': [
                    {   # use interface to make debris pile interactive
                        'id': 0,
                        'name': 'debris',
                        'description': 'pile of debris',
                        'type': 'toggleswitch',
                        'enabled': True,
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
                        'enabled': True,
                        'x': 7,
                        'y': 2,
                        'orientation': 2,
                        'msg_action_verb': 'push'
                    }   # 1 - exit door button
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'door',
                        'type': 'door',
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
                    {   # use device to model wall that fails when debris pile is used
                        'id': 2,
                        'name': 'wall',
                        'description': 'wall',
                        'type': 'switch',
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
                        'description': 'damaged switchbox',
                        'type': 'switch',
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
                    }   # 3 - damaged switchbox
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 2},
                    {'interface_id': 1, 'device_id': 1}
                ],
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
                    {'coordinates': (1, 4), 'story': {'title': None, 'text': 'Galley story...'}},
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
                        'description': 'steel counter',
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
                        'description': 'steel counter',
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
                        'description': 'steel counter',
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
                        'description': 'steel counter',
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
                        'description': 'steel counter',
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
                        'description': 'steel counter',
                        'report': '',
                        'inspectable': False,
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 0,
                        'y': 2
                    }  # counter
                ]
            },
            'system': {
                'corrupt': False,
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'exit door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
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
                        'enabled': True,
                        'x': 4,
                        'y': 8,
                        'orientation': 0,
                        'msg_action_verb': 'use'
                    }  # system terminal
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'door',
                        'type': 'door',
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
                    }   # 1 - exit door
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 1},
                    {'interface_id': 1, 'device_id': 1}
                ],
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
                'corrupt': False,
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'exit door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
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
                    }   # 1 - exit door
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 1}
                ],
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
                'corrupt': False,
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'exit door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
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
                    }   # 1 - exit door
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 1}
                ],
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
                'corrupt': False,
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'exit door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
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
                    }   # 1 - exit door
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 1}
                ],
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
                'corrupt': False,
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'exit door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
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
                    }   # 1 - exit door
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 1}
                ],
                'deaths': []
            }
        }   # excavation
    }
}
