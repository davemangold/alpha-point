from config.player_config import player_config

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
    'intro_text_2': '{0} shifted his gaze to the upper corner of his suit\'s heads-up-display and keyed his mic with a blink. "Hey, Tonia. I\'m wrapping up out here on the eastern plain. How\'d my Astros do in the finals? Old man Dieter said he\'d send us an update." As he finished speaking, {0} began gathering and packing his instruments. He knew how his team had done. It was always the same. But "Hope", he thought, "is a wonderful thing". {0} keyed his mic again, "Tonia, Marcus. Do you read? Over." It was unlike his mission commander to be lazy on the comms. Her Russian accent usually carried a tone of strict professionalism girded by unwavering respect for protocol. {0} finished packing his equipment, careful to keep dust out of the cases. "Why is it", he wondered, "that the folks at Apex could coordinate a multi-national effort to send humans ninety million miles across space to another planet but they couldn\'t build radios that worked over a few kilometers?" After loading his equipment and re-pressurizing the rover cabin, {0} took off his helmet and tried the more powerful vehicle communications array. Eleven and a half minutes later, {0} brought his rover to a stop in front of the Horizon-1 Mars Base, informally known as Alpha Point. There was still no response.'.format(player_config['name']),
    'ui': {
        'width': 60,
        'articles': {
            'default': 'a',
            'mapped': {
                'excursion suit': 'an',
                'excursion suit helmet': 'an',
                'airlock door': 'an',
                'open door': 'an',
                'open airlock door': 'an',
                'exposed switchbox': 'an',
                'open bay door': 'an',
                'wiring': 'some',
                'unlocked tablet': 'an',
                'open wall panel': 'an'
            }
        }
    }
}