import time 
import random

rifle = 1
spear = 1
pick = 0

def rifle_combat():
    global rifle
    chance_hitR = ["Head", "Torso", "Miss", "Head", "Torso"]
    randomizerR = random.choice(chance_hitR)
    if randomizerR == "Head":
        print("The target was shot in the head and was killed.")
        time.sleep(4)
    elif randomizerR == "Torso":
        print("The target was shot in the torso, falls over and is dispatched.")
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

def mountain_pass():
    global rifle, spear
    events_mountain = ["Trader!", "Dangerous Crossing!"] 
    randomizerM = random.choice(events_mountain)
    print("Your wagon moves out of the forest and begins crossing grasslands, the grass moves with the wind like waves in the ocean.")
    time.sleep(10)
    print("After crossing the grassland, you enter the mountains...")
    print("Narrow, winding roads lead into the clouds, if the horses spook then your wagon could drop hundreds of feet!")
    time.sleep(8)
    if randomizerM == "Trader!":
        print("In the distance you spot a camp fire, do you approach it?")
        decision1 = input("Your decision: Y/N").lower()
        if decision1.startswith("y"):
            print("You approach the camp fire...")
            time.sleep(5)
            print("An old man sits by the camp fire, he asks you if there is anything you need.")
            print("He offers to sell a rifle or a spear!")
            time.sleep(5)
            decision2 = input("Your decision: R/S").lower()
            if decision2.startswith("r"):
                print("You look through his selection of rifles and find one that stands out from the rest!")
                time.sleep(7)
                print("This particular kentucky long rifle has a maple wood stock and a blued barrel, it looks reliable.")
                rifle += 1
                print("rifle has been added to inventory!")
                print(rifle)
            else:
                print("You look through the selection of spears and find a boar hunting spear.")
                time.sleep(7)
                print("The shaft is made of hard wood, while the spear itself is razor sharp steel!")
                spear += 1
                print(spear)
        else:
            print("You circumnavigate the camp fire and pass through the mountins safely.")
    elif randomizerM == "Dangerous Crossing!":
        print("you hear a rumbling in the mountains, furthermore, there is a fork in the road.")
        print("Either take an old looking bride OR a narrow path.")
        time.sleep(5)
        decision3 = input("Your decision: B/P").lower()
        if decision3.startswith("b"):
            print("The bridge is old and narrow, fraying sections of rope hold up beams that should be able to hold your wagon.")
            print("Wooden beams look relatively tough and show no signs of rotting.")
            print("Do you go slowly or quickly across the bridge?")
            decision4 = input("Your decision: S/Q")
            if decision4.startswith("q"):
                print("You snap the reigns and the two horses pulling the cart leap into action, \n the ropes go taught and the beams groan under the weight")
                time.sleep(8)
                print("Near the end of the bridge, you hear ropes begin to snap, however the wagon \n safely crosses to the other side as the old bridge collapses into the abyss!")
                print("You move out of the mountains safely.")
            else:
                print("You slowly cross the bridge, halfway through the ropes begin to snap and you feel the entire bridge lurch in one direction.")
                print("Suddenly, the horses spook and take off down the bridge.")
                print("Sadly, the bridge does not hold out, you fall into the abyss.")
        else:
            print("You have chosen the narrow path")
            print("As you travel down the narrow path you encounter a portion of the path blocked by rocks.")
            time.sleep(6)
            print("Do you use a pick axe to clear a path or attempt to go around it?")
            decision5 = input("Your Decision: Pick/Around").lower()
            if decision5.isalpha:
                if pick > 0:
                    print("You begin clearing a path with the pick axe, time work is time consuming and tedious.")
                    print("Eventually the pathway is cleared, you are able to pass through the mountains!")
                else:
                    print("You do not have a pick within inventory, meaning you will need to back track and circumnavigate.")
                    print("During this you run into bandits, do you bribe them OR fight them?")
                    decision6 = input("Your decision: B/F").lower()
                    if decision6.startswith("b"):
                        print("You begin to reason with the bandits.")
                        print("Bandit: We have you surrounded, hand over any weapons along with cash and you can go on your way.")
                        print("You hand over weapons and money, the bandits do not harm you after this, they explain that corpses bring too much attention.")
                        print("Lost Items.")
                        if rifle and spear >= 1:
                            rifle -= 1
                            spear -= 1
                            print(rifle, spear)
                        elif rifle >= 1:
                            rifle -= 1 
                            print(rifle)
                        elif spear >= 1:
                            spear -= 1
                            print(spear)
                        else:
                            print("Bandit decision fail.")
                    else:
                        print("As the bandit opens his mouth to talk you reach for the rifle or spear...")
                        decision7 = input("Your decision: R/S").lower()
                        if decision7.startswith("r"):
                            print("You reach for the rifle!")
                            if rifle >= 1:
                                rifle_combat()
                                print("Another bandit peeks around a rock and shoots as the other bandits run away!")
                                print("After this, you navigate out of the mountains, hopefully that will not happen again!")
                                time.sleep(5)
                            else:
                                print("You do not have a rifle.")
                                time.sleep(5)
                                print("The bandit notices your quick movements and shoots.")
                        else:
                            print("You reach for the spear!")
                            if spear >= 1:
                                spear_combat()
                                time.sleep(5)
                                print("Another bandit peeks around a rock and shoots as the other bandits run away!")
                                time.sleep(5)
                            else:
                                print("You do not have a spear.")
                                time.sleep(5)
                                print("The bandit notices you quick movements and shoots.")
            else:
                print("Mountain Bandits Fail!")


mountain_pass()





