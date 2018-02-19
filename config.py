game_config = {}

player_config = {}


levels_config = {
    'levels': {
        '0': {
            'map': {
                'x_dimension': 5,
                'y_dimension': 5,
                'path_coordinates': [  # path may include doors and valves which are visible
                    (0, 4),
                    (0, 3),
                    (0, 2),
                    (1, 2),
                    (2, 2),
                    (2, 1),
                    (3, 2),
                    (4, 2),
                    (4, 1),
                    (4, 0),
                    (4, 3)
                ],
                'coord_enter': (0, 3),  # begin
                'coord_exit': (4, 0),  # end
                'orientation_enter': 0,
                'msg_enter': 'Welcome to Level 0.',
                'msg_exit': 'Congratulations! You completed the level.'
            },
            'system': {
                'interfaces': [
                    {
                        'id': 0,
                        'name': 'entrance door button',
                        'type': 'button',
                        'enabled': False,
                        'x': 0,
                        'y': 0,
                        'orientation': 0
                    },
                    {
                        'id': 1,
                        'name': 'door circuit toggleswitch',
                        'type': 'toggleswitch',
                        'enabled': True,
                        'x': 2,
                        'y': 0,
                        'orientation': 2
                    },
                    {  # TEST
                        'id': 4,
                        'name': 'test',
                        'type': 'handwheel',
                        'enabled': True,
                        'x': 2,
                        'y': 0,
                        'orientation': 2
                    },
                    {  # TEST
                        'id': 5,
                        'name': 'test',
                        'type': 'terminal',
                        'enabled': True,
                        'x': 3,
                        'y': 1,
                        'orientation': 2
                    },
                    {
                        'id': 2,
                        'name': 'system terminal',
                        'type': 'terminal',
                        'enabled': True,
                        'x': 4,
                        'y': 4,
                        'orientation': 0
                    },
                    {
                        'id': 3,
                        'name': 'exit door button',
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
