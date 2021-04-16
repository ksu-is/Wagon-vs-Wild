import time 
import random

rifle = 1 
spear = 1

def rifle_combat():
    global rifle
    chance_hitR = ["Head", "Torso", "Miss"]
    randomizerR = random.choice(chance_hitR)
    if randomizerR == "Head":
        print("The target was shot in the head and was killed.")
        time.sleep(4)
    elif randomizerR == "Torso":
        print("The target was shot in the torso and falls over and is dispatched.")
        time.sleep(4)
    elif randomizerR == "Miss":
        print("The target was missed")
        time.sleep(2)
        print("In desperation you swing the rifle at the target, which shatters the wood stock the rifle.")
        print("Yet you are alive")
        rifle -= 1
    else:
        print("Rifle ERROR! ")

def spear_combat():
    global spear
    chance_hitR = ["Head", "Torso", "Torso", "Torso", "Miss"]
    randomizerR = random.choice(chance_hitR)
    if randomizerR == "Head":
        print("The target was stabbed in the head and was killed.")
        time.sleep(4)
    elif randomizerR == "Torso":
        print("The target was stabbed in the torso and falls over and is dispatched.")
        time.sleep(4)
    elif randomizerR == "Miss":
        print("The target was missed")
        time.sleep(2)
        print("In desperation you hurl the spear at the target, which shatters the wooden shaft.")
        print("Yet you are alive")
        spear -= 1
    else:
        print("Spear ERROR")

def combat_z():
    events = ["Bitten!", "Scrached!", "Scrached!", "Notice!", "Notice!", "Notice!", "Notice!"]
    randomizer = random.choice(events)
    user = input("use rifle or spear? 'R/S' ").lower()
    if randomizer == "Bitten!":
        print("The Zombies Overwhelm you!")
        print("Death")
    elif randomizer == "Scrached!":
        if user == "r":
            if rifle > 0:
                print("First Aid Function")
                rifle_combat()
        elif user == "s":
            if spear > 0:
                print("First Aid Function")
                spear_combat()


    elif randomizer == "Notice!":
        print("You notice some movement in the brush up ahead, zombies attack!")
        time.sleep(3)
        if user == "r":
            if rifle > 0:
                print("First Aid Function")
                rifle_combat()
        elif user == "s":
            if spear > 0:
                print("First Aid Function")
                spear_combat()

combat_z()     