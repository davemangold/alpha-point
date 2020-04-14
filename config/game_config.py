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
    'intro_text_2': '{0}\' integrated comm system chirped. "Marc, we need you back at base ASAP! There\'s been an incident in the lab", said his mission commander. He shifted his gaze to the top-left corner of his suit\'s heads-up-display and keyed his mic with a blink. "Roger that, Tonia, what kind of incident?" Even as he finished speaking, {0} began gathering and packing his instruments. "We don\'t know yet, but it doesn\'t look good", Tonia replied, her Russian accent a little thicker than usual. "One of the techs made a system-wide call warning everyone to stay away. They\'ve sealed the airlock and disabled external control. We\'re still trying to re-establish contact." As chief science officer, {0} knew laboratory emergency protocols better than anyone. Things were not happening by the book. "Alright, I\'m heading back now. ETA twelve minutes. Who\'s scheduled for the lab today?", {0} asked. Eleven and a half minutes later, {0} brought his rover to a stop in front of the Horizon-1 Mars Base, informally known as Alpha Point. There was still no response.'.format(player_config['name']),
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
                'exposed switchbox': 'an'
            }
        }
    }
}