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
    'story_text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel diam ut lorem tincidunt vehicula malesuada at leo. Donec iaculis iaculis lectus at tristique. Donec diam magna, interdum ac tristique vitae, blandit et risus. Suspendisse facilisis enim aliquam erat posuere, ac blandit mi aliquam. Cras iaculis neque vel turpis auctor, sed faucibus turpis pulvinar. Donec orci nisl, auctor eget libero at, mollis tristique tellus. Curabitur finibus ligula vel arcu lacinia vehicula. In quis sapien id nibh tempus pretium ut id ipsum. Cras mollis ultricies nisi non venenatis. Phasellus quam eros, blandit eget velit vitae, rutrum luctus magna. Curabitur rutrum finibus mi, a interdum velit. In sed lectus nisi. In leo nulla, bibendum ac ligula eu, luctus pharetra elit. Etiam placerat massa erat, et convallis dolor faucibus eu...'
}

player_config = {
    'name': 'Marcus'
}


levels_config = {
    'levels': {
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
                'orientation_enter': 0
            },
            'system': {
                'interfaces': [],
                'devices': [],
                'links': []
            }
        },
        1: {
            'name': 'Airlock',
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
                'orientation_enter': 0
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
                        'msg_unmet_dependencies': 'The door is locked.',
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
                ]
            }
        }
    }
}
