# I begin coding here. 

import random 
import time


miles_to_travel = 1457
miles_traveled = 0
min_miles = 5
max_miles = 25

food_remaining = 1000

min_food_used = 25
max_food_used = 50
scavenge_food = 70
hunting_food = 100
food_per_day = 15

Diseases_encountered = 0
current_diseases = 0
total_diseases = 10


Months_list = ["test", "January", "Febuary", "March", "April", "May", 
"June", "July", "August", "September", "October", "November", "December"]


month_type1 = [1, 3, 5, 7, 8, 10, 12]
month_type2 = [4, 6, 9, 11]
month_type3 = [2]

# Items within Game

spare_wheel = 0 
shovel = 0 
rifle = 0 
pick_axe = 0 
tent = 0 
fire_wood = 0
shoes = 0
spear = 0 
bow = 0 
lazer_rifle = 0
magic = 0


health_points = 50
enemy_health = 50



checkpoints = iter([" Rothrock Forest PA", " Monongahela Forest VA", " Lexington KY", " Outpost in TN", " Now Entering Arkansas", "Little Rock AK!"])





print("--------------------------------- Wagon Vs Wild ----------------------------------------")

welcome1 = ("The year is 1837, and a new state has been recently admitted to the union.\n Reading the new and exiting prospects of \na life out west, you begin to make preperations to leave the state of Rhode Island.")
welcome2 = ("You are about to begin the journey from Warwick Rhode Island to Hot Springs Arkansas.\n The journey will be perilous,\n but settling out west offers better prospects than Rhode Island could ever offer at this point in your lives.")
general_store = ("An old man welcomes you into a large general store, many customers mill around the various isles of tools and equipment,")
general_store2 = ("Eventually you begin to pick different supplies, ")


def play_game():
    print("--------------------------------- Wagon Vs Wild ----------------------------------------")
    print(welcome1)
    print()
    time.sleep(5)
    print(welcome2)
    print()
    time.sleep(5)
    print(general_store)
    print()
    time.sleep(7)
    print(general_store2)
    time.sleep(5)
    print(" Your choices for the long road ahead are as follows, minimalist Travel package for $300, normal Travel package $500 and Extensive Package $800")
    user = input(" Type 'A' for minimal, 'B for normal and 'c' for extensive")
    if user.upper() == "A":
        supply = "A"
        global spear, rifle
        spear += 1
        rifle += 1
        start()
        pathing(supply)
    elif user.upper() == "B":
        supply = "B"
        spear += 1
        rifle += 1
        start()
        pathing(supply)
    elif user.upper() == "C":
        supply = "C"
        spear += 1
        rifle += 1
        start()
        pathing(supply)
    else:
         play_game()


# Combat Functions 

def spear_dino():
    global health_points, enemy_health
    print("With spear in hand, you lunge at the dino!")
    time.sleep(3)
    print("The spear hits the dinosaur!")
    dice_rollP = random.randint(8,25)
    health_points -= dice_rollP
    dice_rollD = random.randint(10, 20)
    enemy_health -= dice_rollD


def rifle_dino():
    global health_points, enemy_health
    print("You reloaded after the first shot, ramming down another round ball with black powder.")
    print("You shoot wildly at the dinosaur!")
    dice_rollP = random.randint(8,25)
    health_points -= dice_rollP
    dice_rollD = random.randint(10, 20)
    enemy_health -= dice_rollD



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

def combat_z(supply):
    events = ["Bitten!", "Scrached!", "Scrached!", "Notice!", "Notice!", "Notice!", "Notice!"]
    randomizer = random.choice(events)
    user = input("use rifle or spear? 'R/S' ").lower()
    if randomizer == "Bitten!":
        print("The Zombies Overwhelm you!")
        ending_choice()
    elif randomizer == "Scrached!":
        if user == "r":
            if rifle > 0:
                print("First Aid Function")
                rifle_combat()
                continue_journey(supply)
        elif user == "s":
            if spear > 0:
                print("First Aid Function")
                spear_combat()
                continue_journey(supply)


    elif randomizer == "Notice!":
        print("You notice some movement in the brush up ahead, zombies attack!")
        time.sleep(3)
        if user == "r":
            if rifle > 0:
                rifle_combat()
                continue_journey(supply)
        elif user == "s":
            if spear > 0:
                spear_combat()
                continue_journey(supply)


def river_crossing(supply):
    global spare_wheel
    random_event = ["crossed", "crossed", "crossed", "crossed", "crossed", "fail", "fail"]
    event = random.choice(random_event)
    if event.startswith("c"):
        print("You have Forded the river, although rocky and dangerous, the wagon made it across.")
        time.sleep(3)
        continue_journey(supply)
    elif event.startswith("f"):
        print("You have run into trouble on the river, a wagon wheel breaks.")
        spare_wheel -= 1
        if spare_wheel == 0:
            print("You do not have a spare wagon wheel, the wagon begins floating along the river.")
            time.sleep(3)
            print("Eventually, your wagon hits a rock and breaks apart. Your journey has come to an end.")
            ending_choice()


def mountain_pass(supply):
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
                continue_journey(supply)
            else:
                print("You look through the selection of spears and find a boar hunting spear.")
                time.sleep(7)
                print("The shaft is made of hard wood, while the spear itself is razor sharp steel!")
                spear += 1
                print(spear)
                continue_journey(supply)
        else:
            print("You circumnavigate the camp fire and pass through the mountins safely.")
            continue_journey(supply)
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
                continue_journey(supply)
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
                if pick_axe > 0:
                    print("You begin clearing a path with the pick axe, time work is time consuming and tedious.")
                    print("Eventually the pathway is cleared, you are able to pass through the mountains!")
                    time.sleep(6)
                    continue_journey(supply)
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
                            continue_journey(supply)
                        elif rifle >= 1:
                            rifle -= 1 
                            print(rifle)
                            continue_journey(supply)
                        elif spear >= 1:
                            spear -= 1
                            print(spear)
                            continue_journey(supply)
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
                                continue_journey(supply)
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
                                continue_journey(supply)
                            else:
                                print("You do not have a spear.")
                                time.sleep(5)
                                print("The bandit notices you quick movements and shoots.")
            else:
                print("Mountain Bandits Fail!")

def dinosaur_encounter(supply): # add supply later /, "Unseen", "Animal"
    dino_events = ["Spotted!"]
    enemy_dinos = ["Velociraptor", "Coelophysis", "Microraptor", "T-Rex"]
    randomizer = random.choice(dino_events)
    randomizer1 = random.choice(enemy_dinos)
    print("In the distance, you see something odd.")
    time.sleep(3)
    print("Dinosaurs, some with long green necks, others with sharp tusks on their heads.")
    print("They stand in a densly forested area with ferns and foliage making them nearly invisible.")
    time.sleep(5)
    if randomizer == "Spotted!":
        print("As you stare in amazement at giant creatures that have not been seen before, instinct tells you")
        print("to scan the surronding area for threats, you spot a " + randomizer1 + " which stares at you with hungry eyes.")
        time.sleep(9)
        print("Three rush at you from the forest, they begin 200 yards away.")
        print("You have enough time to shoot one, then snapshoot another.")
        if rifle > 0:
            print("Your first shot.")
            rifle_combat()
            time.sleep(3)
            print("Your second shot.")
            rifle_dino()
            print("after the last shot you grab a spear, but the dino is very fast, you have " + str(health_points) + "HP left.")
            print("The dinosaur health is, " + str(enemy_health) + " HP currently.")
            time.sleep(5)
            while enemy_health >= 1: 
                spear_dino()
                if enemy_health >= 1:
                    print("Victory")
                    continue_journey(supply)
                    break
                elif health_points >= 0:
                    print("Death")
                    break
                else:
                    print("End Combat Fail")
    else:
        print("test")

def wizard_encounter(supply):
    color_ans = ["red", "orange", "yellow", "green", "violet", "indigo", "blue"]
    print("In the distance you see a few robed men in pointy hats, they sit atop a wagon riding towards you.") 
    time.sleep(3)
    print("One wears leather hides, the next wears long silk robes, the last is dressed similar to other travilers you have seen along the road.")
    time.sleep(7)
    print("The normally dressed Wizard introduces himslef as: Tim the Terrible!")  
    print("He says, 'In order to pass you must answer me these questions three, lest we strike you with magic!'")
    time.sleep(7)
    print("What, is your favorite Color?")
    print("What, is the air speed velocity of an unlaiden swallow?")
    print("What, is the capital of Syria?")
    time.sleep(8)
    print("At this point you are fairly bemused, until one of them strikes a tree with lightning nearby.")
    user = input("Your response to the first question.").lower()
    if user in color_ans:
        
        print("Correct on the first question.")
    else:
        print("Wrong, says the wizard in long silk robes, he strikes you with lightning.")
        ending_choice()
    user1 = input("Enter a numeric Value").lower()
    if user1 == "24":
        
        print(str(user1) + " miles per hour is correct, now answer the final answer.")
    else:
        print("Wrong, says the wizard in long silk robes, he strikes you with lightning.")
        ending_choice()
    user2 = input("Your response to the third question.").lower()
    if user2 == "damascus":
        
        print("Correct, you have answered all our questions and may go in peace!")
        time.sleep(4)
        print("You quickly gather the reins of the horse atop the wagon and continue along the path")
        time.sleep(3)
        continue_journey(supply)
    else:
        print("Wrong, says the wizard in long silk robes, he strikes you with lightning.")
        ending_choice()

# More Events will be added in the future! 

def pathing(supply):
    random_events = [" Zombies!", "Wizards!", "River!", "Dinosaurs!", "Mountains!"]
    time.sleep(3)
    events = random.choice(random_events)
    print("You seem to have encounterd, " + events)
    if events == " Zombies!":
        combat_z(supply)
        print("test")
    elif events == "Wizards!":
        wizard_encounter(supply)
    elif events == "River!":
        river_crossing(supply)
    elif events == "Dinosaurs!":
        dinosaur_encounter(supply)
    elif events == "Mountains!":
        mountain_pass(supply)



# Ambience for game world 
def days_traveled():
    global miles_traveled, miles_to_travel
    distance_miles = random.randint(10, 30)
    distance_days = random.randint(1,7)
    distance_miles += miles_traveled
    print("You have traveled for, " + str(distance_miles) + " miles.")
    print("You have traveled for," + str(distance_days) + " days.")

 


# Victory, Start and ending functions.

def continue_journey(supply):
    journey = next(checkpoints)
    print("The sign on the road says" + journey)
    if journey != "Little Rock AK!":
        question = input("input 'Y' or 'N'" + "The journey has been long and difficult, do you continue from, " + journey + "?")
        if question.lower() == "y":
            days_traveled()
            time.sleep(4)
            pathing(supply)
        elif question.lower() == "n":
            ending_choice()
        else:
            pathing(supply)
    else:
        Victory()



def Victory():
    print("Enter Better game Victory note")

def ending_choice():
    print("Your Journey comes to an end at")

def start():
    print("                                      Good choice! Let's hit the trail...")
    
    print("You are now leaving Rhode Island!")
    

play_game()



