import time 
import random

def river_crossing():
    global spare_wheel
    random_event = ["crossed", "crossed", "crossed", "crossed", "crossed", "fail", "fail"]
    event = random.choice(random_event)
    if event.startswith("c"):
        print("You have Forded the river, although rocky and dangerous, the wagon made it across.")
        time.sleep(3)
    elif event.startswith("f"):
        print("You have run into trouble on the river, a wagon wheel breaks.")
        spare_wheel -= 1
        if spare_wheel == 0:
            print("You do not have a spare wagon wheel, the wagon begins floating along the river.")
            time.sleep(3)
            print("Eventually, your wagon hits a rock and breaks apart. Your journey has come to an end.")

river_crossing()