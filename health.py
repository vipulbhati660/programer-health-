

from pygame import mixer
from time import time
from datetime import datetime
import os


def log (filename,activeity):
    if os.path.exists(filename):
        with open(filename,"a") as f:
            f.write(f"you did {activeity} at {datetime.now().ctime()}\n")
    else:
        with open(filename,"w") as f:
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
    if (passed-int_water)>=40*60:
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
