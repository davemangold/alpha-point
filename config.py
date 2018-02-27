game_config = {}

player_config = {}


levels_config = {
    'levels': {
        1: {
            'name': 'Airlock',
            'map': {
                'x_dimension': 5,
                'y_dimension': 5,
                'path_cells': [
                    {'coordinates': (0, 4), 'story_text': None},
                    {'coordinates': (0, 3), 'story_text': 'Marcus breathed a sigh of relief as the airlock sealed behind him...'},
                    {'coordinates': (0, 2), 'story_text': None},
                    {'coordinates': (1, 2), 'story_text': None},
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
                'msg_enter': 'Welcome to Airlock.',
                'msg_exit': 'Congratulations! You completed the level.'
            },
            'system': {
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'entrance door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': False,
                        'x': 0,
                        'y': 0,
                        'orientation': 0
                    },
                    {
                        'id': 1,
                        'name': 'door circuit toggleswitch',
                        'description': 'switch',
                        'type': 'toggleswitch',
                        'enabled': True,
                        'x': 2,
                        'y': 0,
                        'orientation': 2
                    },
                    {  # TEST
                        'id': 4,
                        'name': 'test',
                        'description': 'handwheel',
                        'type': 'handwheel',
                        'enabled': True,
                        'x': 2,
                        'y': 0,
                        'orientation': 2
                    },
                    {  # TEST
                        'id': 5,
                        'name': 'subsystem terminal',
                        'description': 'subsystem terminal',
                        'type': 'terminal',
                        'enabled': True,
                        'x': 3,
                        'y': 1,
                        'orientation': 2
                    },
                    {
                        'id': 2,
                        'name': 'system terminal',
                        'description': 'system terminal',
                        'type': 'terminal',
                        'enabled': True,
                        'x': 4,
                        'y': 4,
                        'orientation': 0
                    },
                    {
                        'id': 3,
                        'name': 'exit door button',
                        'description': 'button',
                        'type': 'button',
                        'enabled': True,
                        'x': 4,
                        'y': 0,
                        'orientation': 2
                    }
                ],
                'devices': [
                    {
                        'id': 0,
                        'name': 'entrance door',
                        'description': 'entrance door',
                        'type': 'door',
                        'enabled': False,
                        'active': False,
                        'x': 0,
                        'y': 4,
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
                        'dependencies': [
                            {'device_id': 1, 'active_state': True}
                        ]
                    }
                ],
                'links': [
                    {'interface_id': 0, 'device_id': 0},
                    {'interface_id': 1, 'device_id': 1},
                    {'interface_id': 2, 'device_id': 1},
                    {'interface_id': 2, 'device_id': 2},
                    {'interface_id': 3, 'device_id': 2}
                ]
            }
        }
    }
}
