
#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from time import time


def log (filename,activeity):
    from datetime import datetime
    with open(filename,"a") as f:
        f.write(f"you did {activeity} at {datetime.now().ctime()}\n")

def music(file,filename,activeity):
    print(f"did you {activeity} ")
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops=-1)
    action=input("> ").lower()
    if action=="yes":
        mixer.music.stop()
        log(filename,activeity)
        action=""
        return 'successful'
    else:
        print("invald input please retry")
        action=input("> ")


int_water=time()
int_eyes=time()
int_physical=time()



while True:
    passed=time()
    if (passed-int_water)>=10:
        y=music("22.mp3","log/water.txt","drink water")
        if y=='successful':
            int_water=passed

    
    if (passed-int_eyes)>=30*60:
        y=music("23.mp3","log/eye.txt","exercise your eye")
        if y=='successful':
            int_eyes=passed

 

    if (passed-int_physical)>=60*60:
        y=music("24.mp3","log/exercise.txt","exercise")
        if y=='successful':
            int_physical=passed
