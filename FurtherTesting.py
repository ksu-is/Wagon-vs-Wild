import random 
import time
spear = 0
rifle = 1
def rifle_combat():
    global randomizerR
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
        combat_z()
    else:
        print("Rifle ERROR! ")


def combat_z():
    events = ["Bitten!", "Scrached!", "Survived!"]
    randomizer = random.choice(events)
    user = input("use rifle or spear? 'R/S' ").lower()
    if spear >= 1:
        print("you have used the spear to defeat the zombies")
    if user == "r":
        rifle_combat()
        if rifle > 0:
            rifle_combat()
    else:
        if randomizer == "Bitten!":
            print("No matter what you do, the bite festers")
        elif randomizer == "Scrached!":
            print("add first Aid Function")
        elif randomizer == "Survived!":
            print("You have survived the encounter!")
        else:
            print("test")
combat_z()   