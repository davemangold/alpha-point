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
    'intro_text_1': 'Marcus could sense the stillness of his environment -- vacuous and oppressive. Intense sunlight cut sharp-edged lines across the dusty, red rocks at his feet. Above, a high, streaky haze blurred the tawny blue and grey of the sky. In every direction there was more of the same: rocks, dust, and light; repeating, shrinking, and finally vanishing at the horizon.  In this place time itself was like a distant memory and the imperceptibly slow turn of shadows across the landscape was the only reminder that it still existed. There was no movement; no gentle breeze, no flowing water, no bounding life; only a vast, empty exapanse -- in a word, desolation.',
    'intro_text_2': 'The chirp of Marcus\' integrated comm system was followed by the voice of his mission commander: "Marc, we neeed you back at base ASAP! There\'s been an incident in the lab." He shifted his gaze to the top-left corner of his suit\'s heads-up-display and keyed his mic with a blink. "Roger that, Tonia, what kind of incident?". Even as he finished speaking, Marcus began gathering and packing his instruments. "We don\'t know yet, but it doesn\'t look good.", Tonia replied, her Russian accent a little thicker than ususal, "One of the techs made a system-wide call warning everyone to stay away. The airlock is sealed and external control is disabled. We\'re still trying to re-establish contact." As chief science officer, Marcus knew laboratory emergency protocols better than anyone. They hadn\'t been followed. "Alright, I\'m heading back now. ETA twelve minutes. Who was scheduled for the lab today?", Marcus asked. Eleven and a half minutes later, as Marcus brought the rover to a stop in front of the Horizon-1 Mars Base, informally known as Alpha Point, there was still no response...',
    'ui': {
        'width': 60,
        'articles': {
            'default': 'a',
            'mapped': {
                'excursion suit': 'an',
                'excursion suit helmet': 'an'
            }
        }
    }
}

player_config = {
    'name': 'Marcus'
}

level_config = {
    'levels': {
        99: {
            'name': 'Testing',
            'map': {
                'x_dimension': 5,
                'y_dimension': 5,
                'path_cells': [
                    {'coordinates': (0, 4), 'story_text': None},
                    {'coordinates': (0, 3), 'story_text': ('{0} breathed a sigh of relief as the airlock sealed behind him...').format(player_config['name'])},
                    {'coordinates': (0, 2), 'story_text': None},
                    {'coordinates': (1, 2), 'story_text': ('A glow emanated from the left side of the corridor ahead. "Is that a passage?", {0} wondered... ').format(player_config['name'])},
                    {'coordinates': (2, 2), 'story_text': None},
                    {'coordinates': (2, 1), 'story_text': None},
                    {'coordinates': (3, 2), 'story_text': None},
                    {'coordinates': (4, 2), 'story_text': None},
                    {'coordinates': (4, 1), 'story_text': None},
                    {'coordinates': (4, 0), 'story_text': None},
                    {'coordinates': (4, 3), 'story_text': None}
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
                    }
                ],
                'artifacts': []
            },
            'system': {
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
                    },
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
                    },
                    {
                        'id': 2,
                        'name': 'system terminal',
                        'description': 'system terminal',
                        'type': 'terminal',
                        'enabled': True,
                        'x': 4,
                        'y': 4,
                        'orientation': 0,
                        'msg_action_verb': 'use'
                    },
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
                    }
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
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
                    },
                    {
                        'id': 1,
                        'name': 'door circuit switch',
                        'description': 'door circuit',
                        'type': 'switch',
                        'enabled': True,
                        'active': False,
                        'x': 2,
                        'y': 0,
                        'msg_action_true': 'close',
                        'msg_action_false': 'open',
                        'msg_active_true': 'The circuit is closed.',
                        'msg_active_false': 'The circuit is open.',
                        'msg_toggle_active_true': 'Do you hear that? It sounds like electric current.',
                        'msg_toggle_active_false': 'That electric hum went away.',
                        'msg_unmet_dependencies': 'The circuit switch isn\'t responding.',
                        'dependencies': []
                    },
                    {
                        'id': 2,
                        'name': 'exit door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': True,
                        'active': False,
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
                            {'device_id': 1, 'active_state': True}
                        ]
                    },
                    {
                        'id': 3,
                        'name': 'exit door camera',
                        'description': 'security camera',
                        'type': 'camera',
                        'enabled': True,
                        'active': True,
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
                    }
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
        },
        0: {
            'name': 'The Void',
            'map': {
                'x_dimension': 1,
                'y_dimension': 2,
                'path_cells': [
                    {'coordinates': (0, 0), 'story_text': None},
                    {'coordinates': (0, 1), 'story_text': 'This place is not for you. Run along now...'}
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
                'links': [],
                'deaths': []
            }
        },
        1: {
            'name': 'Entrance',
            'map': {
                'x_dimension': 5,
                'y_dimension': 5,
                'path_cells': [
                    {'coordinates': (2, 4), 'story_text': None},
                    {'coordinates': (2, 3), 'story_text': ('Faint clouds of dust fell from his boots as {0} climbed down the rover ladder. "Something is very wrong", he thought, while surveying the environment for any sign of disaster. Everything was in place. There was no evidence of an explosion or collapse. The light over the external airlock door glowed green indicating its pressure matched that of the external environment. According to his suit\'s computer, he still had active comm and telemetry links with Alpha Point but all he could hear was the sound of his own breathing. "What the hell?", Marcus wondered, as he headed toward the airlock.').format(player_config['name'])},
                    {'coordinates': (2, 2), 'story_text': None},
                    {'coordinates': (2, 1), 'story_text': None},
                    {'coordinates': (2, 0), 'story_text': None},
                    {'coordinates': (3, 3), 'story_text': None},
                    {'coordinates': (4, 3), 'story_text': None},
                    {'coordinates': (1, 1), 'story_text': None},
                    {'coordinates': (0, 1), 'story_text': None}
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
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 2,
                        'y': 4
                    },
                    {
                        'type': 'generic',
                        'name': 'solararray',
                        'description': 'solar array',
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 0,
                        'y': 1
                    },
                    {
                        'type': 'generic',
                        'name': 'communicationsarray',
                        'description': 'communications array',
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 4,
                        'y': 3
                    },
                ]
            },
            'system': {
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
                    }
                ],
                'devices': [
                    {
                        'id': 4,
                        'name': 'airlock door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': True,
                        'active': False,
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
                    }
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 4}
                ],
                'deaths': []
            }
        },
        2: {
            'name': 'Airlock',
            'map': {
                'x_dimension': 3,
                'y_dimension': 5,
                'path_cells': [
                    {'coordinates': (1, 0), 'story_text': None},
                    {'coordinates': (1, 1), 'story_text': None},
                    {'coordinates': (1, 2), 'story_text': None},
                    {'coordinates': (1, 3), 'story_text': ('{0} checked his mission clock as the door sealed behind him. He was about thirty minutes ahead of schedule. "Alright, focus.", he thought, "Follow the ingress procedure."').format(player_config['name'])},
                    {'coordinates': (1, 4), 'story_text': None}
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
                        'enabled': True,
                        'x': 2,
                        'y': 2,
                        'orientation': 3,
                        'msg_action_verb': 'push'
                    },
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
                    },
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
                    }
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
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
                    },
                    {
                        'id': 1,
                        'name': 'airlock pressurization valve',
                        'description': 'pressurization valve',
                        'type': 'valve',
                        'enabled': True,
                        'active': False,
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
                    },
                    {
                        'id': 2,
                        'name': 'exit door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': True,
                        'active': False,
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
                            {'device_id': 1, 'active_state': True}
                        ]
                    }
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
        },
        3: {
            'name': 'Equipment',
            'map': {
                'x_dimension': 9,
                'y_dimension': 9,
                'path_cells': [
                    {'coordinates': (4, 0), 'story_text': None},
                    {'coordinates': (4, 1), 'story_text': None},
                    {'coordinates': (4, 2), 'story_text': None},
                    {'coordinates': (4, 3), 'story_text': None},
                    {'coordinates': (4, 4), 'story_text': None},
                    {'coordinates': (4, 5), 'story_text': None},
                    {'coordinates': (4, 6), 'story_text': None},
                    {'coordinates': (4, 7), 'story_text': 'As he removed his helmet, {0} noticed two empty excursion suit alcoves and wondered who else was outside the hab. Ad-hoc departures weren\'t that unusual. Even Martian research stations have fences that need mending. The lights flickered briefly and {0} detected the caustic smell of overheated electronics. "That can\'t be good", he told himself. After stowing his suit in an open alcove {0} headed for the door of the crew meeting area.'.format(player_config['name'])},
                    {'coordinates': (4, 8), 'story_text': None},
                    {'coordinates': (3, 6), 'story_text': None},
                    {'coordinates': (3, 7), 'story_text': None},
                    {'coordinates': (5, 6), 'story_text': None},
                    {'coordinates': (5, 7), 'story_text': None},
                    {'coordinates': (3, 4), 'story_text': None},
                    {'coordinates': (2, 4), 'story_text': None},
                    {'coordinates': (1, 4), 'story_text': None},
                    {'coordinates': (5, 4), 'story_text': None},
                    {'coordinates': (6, 4), 'story_text': None},
                    {'coordinates': (7, 4), 'story_text': None},
                    {'coordinates': (3, 2), 'story_text': None},
                    {'coordinates': (2, 2), 'story_text': None},
                    {'coordinates': (1, 2), 'story_text': None},
                    {'coordinates': (5, 2), 'story_text': None},
                    {'coordinates': (6, 2), 'story_text': None},
                    {'coordinates': (7, 2), 'story_text': None}
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
                    }
                ],
                'parts': [],
                'artifacts': [
                    {
                        'type': 'generic',
                        'name': 'suit_1',
                        'description': 'excursion suit',
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 3,
                        'y': 6
                    },
                    {
                        'type': 'generic',
                        'name': 'suit_2',
                        'description': 'excursion suit',
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 3,
                        'y': 7
                    },
                    {
                        'type': 'generic',
                        'name': 'suit_3',
                        'description': 'excursion suit',
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 5,
                        'y': 7
                    },
                    {
                        'type': 'generic',
                        'name': 'circuit_bundle_1',
                        'description': 'bundle of wires and circuitry',
                        'visible': True,
                        'interactive': True,
                        'blocking': False,
                        'x': 6,
                        'y': 1
                    },
                    {
                        'type': 'generic',
                        'name': 'helmet_1',
                        'description': 'excursion suit helmet',
                        'visible': True,
                        'interactive': True,
                        'blocking': False,
                        'x': 7,
                        'y': 3
                    }
                ]
            },
            'system': {
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
                    },
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
                    },
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
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
                    },
                    {
                        'id': 1,
                        'name': 'exit door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': True,
                        'active': False,
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
                            {'device_id': 2, 'active_state': True}
                        ]
                    },
                    {
                        'id': 2,
                        'name': 'door circuit switch',
                        'description': 'door circuit',
                        'type': 'switch',
                        'enabled': False,
                        'active': False,
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
                    },
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 1}
                ],
                'deaths': []
            }
        },
        4: {  # TODO: add part to fix electrical switch and open door
            'name': 'Crew',
            'map': {
                'x_dimension': 9,
                'y_dimension': 7,
                'path_cells': [
                    {'coordinates': (2, 4), 'story_text': None},
                    {'coordinates': (3, 4), 'story_text': None},
                    {'coordinates': (4, 4), 'story_text': None},
                    {'coordinates': (5, 4), 'story_text': None},
                    {'coordinates': (6, 4), 'story_text': None},
                    {'coordinates': (2, 3), 'story_text': None},
                    {'coordinates': (6, 3), 'story_text': None},
                    {'coordinates': (2, 2), 'story_text': None},
                    {'coordinates': (3, 2), 'story_text': None},
                    {'coordinates': (4, 2), 'story_text': None},
                    {'coordinates': (5, 2), 'story_text': None},
                    {'coordinates': (6, 2), 'story_text': None},
                    {'coordinates': (4, 5), 'story_text': 'Marcus tried again to establish radio contact as he stepped through the broken door, it\'s safety mechanism drawing it closed behind him, "Tonia, this is Marcus. Do you read me? Over."...nothing.'},
                    {'coordinates': (4, 6), 'story_text': None},
                    {'coordinates': (4, 0), 'story_text': None},
                    {'coordinates': (4, 1), 'story_text': None},
                    {'coordinates': (1, 3), 'story_text': 'Marcus looked out the habitat window. He could see the opposing crater rim about a kilometers away. They were lucky, he thought, that The Agency had selected this site. The lake that once filled the crater had escaped eons ago when a portion of the crater wall collapsed, leaving behind a convenient access route. A last remnant of the lake still existed as tons of water ice along the perpetually shaded southern wall while slightly closer to the center of the crater the solar array received plenty of sunlight to generate power for the habitat. The hab itself, nestled along the northeastern wall, adjacent to the subterranean portion of the base, was well protected from the prevailing, dusty winds above.'},
                    {'coordinates': (7, 3), 'story_text': None},
                    {'coordinates': (8, 3), 'story_text': None}
                ],
                'coord_enter': (4, 5),
                'coord_exit': (8, 3),
                'orientation_enter': 0,
                'tools': [],
                'parts': [],
                'artifacts': [
                    {
                        'type': 'generic',  # use non-visible to make blocking debris pile
                        'name': 'debris',
                        'description': 'pile of debris',
                        'visible': False,
                        'interactive': False,
                        'blocking': True,
                        'x': 4,
                        'y': 0
                    },
                    {
                        'type': 'generic',
                        'name': 'table',
                        'description': 'table',
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 3,
                        'y': 3
                    },
                    {
                        'type': 'generic',
                        'name': 'table',
                        'description': 'table',
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 4,
                        'y': 3
                    },
                    {
                        'type': 'generic',
                        'name': 'table',
                        'description': 'table',
                        'visible': True,
                        'interactive': False,
                        'blocking': True,
                        'x': 5,
                        'y': 3
                    }
                ]
            },
            'system': {
                'interfaces': [
                    {
                        'id': 0,  # use interface to make debris pile interactive
                        'name': 'debris',
                        'description': 'pile of debris',
                        'type': 'toggleswitch',
                        'enabled': True,
                        'x': 4,
                        'y': 0,
                        'orientation': 2,
                        'msg_action_verb': 'clear'
                    }
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'door',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
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
                    },
                    {
                        'id': 1,
                        'name': 'ceiling',
                        'description': 'ceiling',
                        'type': 'switch',
                        'enabled': True,
                        'active': False,
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
                    }
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 1}
                ],
                'deaths': [
                    {'configuration': [
                        {'device_id': 1, 'active_state': True}],
                     'description': 'The habitat wall failed catastrophically and you were blown into the frigid near-vacuum of the Martian landscape.',
                     'location': None}  # None if all locations are valid
                ]
            }
        }
    }
}
