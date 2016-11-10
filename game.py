import sound
from display import show_strings
from light import get_brightness
from sonar import get_distance
import time
import os

def rand(n=None):
    r = ord(os.urandom(1))
    if n:
        return r % n
    return r

def is_bright():
    return get_brightness() >= 900

def is_present():
    return get_distance() < 100.0

def you_lose():
    sound.falling_sound()
    show_strings(['miss', '', '', 'you lose'])
    time.sleep(2)

def you_got_point():
    sound.rising_sound()
    show_strings(['nice work', '', '', 'you got point'])
    time.sleep(2)

def do_session():
    show_strings(['', 'ready', '', ''])
    sound.rising_sound()
    for c in range(5+rand(5),0,-1):
        if not is_present() or is_bright():
            you_lose()
            return 0
        time.sleep(1)
        sound.sound_loop([220])
    time.sleep(1)
    should_attack = (rand(3) == 0)
    if should_attack:
        show_strings(['attack the enemy', '!!!!!!', '!!!!!!', '!!!!!!'])
        sound.sound_loop([220,0,220,0,220],tick=0.5)
        for c in range(100,0,-1):
            if is_present() and is_bright():
                you_got_point()
                return 1
            time.sleep(0.01)
        you_lose()
        return 0
    else:
        show_strings(['supply capsule', '!!!!!!', '!!!!!!', '!!!!!!'])
        sound.sound_loop([110],tick=3.0)
        for c in range(100,0,-1):
            if not is_present() or is_bright():
                you_lose()
                return 0
            time.sleep(0.01)
        you_got_point()
        return 1
    return 0

def main():
    while is_bright():
        show_strings(['warning', '', '', 'too bright'])
        time.sleep(0.5)
    while not is_present():
        show_strings(['warning', '', '', 'come close'])
        time.sleep(0.5)
    show_strings(['shooting game', '', '', 'shoot to start'])
    while not is_bright():
        time.sleep(0.5)
    score = 0
    for _ in range(5):
        score += do_session()
    show_strings(['game end', 'score:%d' % score, '', ''])
