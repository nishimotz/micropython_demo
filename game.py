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
    return any([get_distance() < 80, get_distance() < 80, get_distance() < 80])

def warn(mes=''):
    print(mes)
    show_strings(['warning', '', '', mes])

def you_lose(mes='miss'):
    print(mes)
    sound.falling_sound()
    show_strings([mes, '', '', 'you lose'])
    time.sleep(2)

def you_got_point(mes='nice work'):
    print(mes)
    sound.rising_sound()
    show_strings([mes, '', '', 'you got point'])
    time.sleep(2)

def shoot_sound():
    sound.sound_loop(range(440,110,-5),tick=0.01)

def do_session():
    while is_bright():
        time.sleep(0.5)
    show_strings(['', 'ready', '', ''])
    sound.rising_sound()
    for c in range(5+rand(5),0,-1):
        if not is_present():
            you_lose('stay here')
            return 0
        if is_bright():
            you_lose('too early')
            return 0
        time.sleep(1)
        sound.sound_loop([220])
    time.sleep(1)
    should_attack = (rand(2) == 0)
    if should_attack:
        show_strings(['attack the enemy', '!!!!!!', '!!!!!!', '!!!!!!'])
        sound.sound_loop([0,220,0,220,0,220],tick=0.5)
        for c in range(100,0,-1):
            if is_bright():
                shoot_sound()
                you_got_point('nice shot')
                return 1
            if is_present():
                sound.sound_loop([110],tick=3.0)
                you_lose('attacked')
                return 0
            time.sleep(0.01)
        you_lose('enemy is gone')
        return 0
    else:
        show_strings(['supply capsule', '!!!!!!', '!!!!!!', '!!!!!!'])
        sound.sound_loop([261],tick=3.0)
        for c in range(100,0,-1):
            if not is_present():
                you_lose('capsule is gone')
                return 0
            if is_bright():
                shoot_sound()
                you_lose('do not shoot')
                return 0
            time.sleep(0.01)
        you_got_point('nice capture')
        return 1
    return 0

def main():
    while is_bright():
        warning('too bright')
        time.sleep(0.5)
    while not is_present():
        warning('come close')
        time.sleep(0.5)
    show_strings(['shooting game', '', '', 'shoot to start'])
    while not is_bright():
        time.sleep(0.5)
    show_strings(['start', '', '', ''])
    shoot_sound()
    while is_bright():
        time.sleep(0.5)
    point = 0
    for _ in range(5):
        point += do_session()
        print('point: %d' % point)
    show_strings(['game end', 'point: %d' % point, '', ''])
