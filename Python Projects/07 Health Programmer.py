""""""
"""
Healthy Programmer
9am - 5pm
Water - water.mp3 (3.5 litres) - Drank - log - Every 40 minutes
Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 minutes
Physical activity - physical.mp3 every - 45 min - ExDone - log

Rules
Pygame module to play audio
"""

from pygame import mixer
from datetime import datetime
from time import time


def musicOnLoop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        inputOfUser = input()
        if inputOfUser == stopper:
            mixer.music.stop()
            break


def logNow(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_secs = 40 * 60
    exercise_secs = 45 * 60
    eyes_secs = 30 * 60

    while True:
        if time() - init_water > water_secs:
            print("Water Drinking time. Enter 'drank' to stop the alarm")
            musicOnLoop("water.mp3", "drank")
            init_water = time()
            logNow("Drank water at")

        if time() - init_eyes > eyes_secs:
            print("Eye Exercise time. Enter 'doneEyes' to stop the alarm")
            musicOnLoop("eyes.mp3", "doneEyes")
            init_eyes = time()
            logNow("Eyes relaxed at")

        if time() - init_exercise > exercise_secs:
            print("Physical Activity time. Enter 'donePhy' to stop the alarm")
            musicOnLoop("physical.mp3", "donePhy")
            init_exercise = time()
            logNow("Physical Activity done at")
