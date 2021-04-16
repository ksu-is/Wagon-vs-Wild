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
kentucky_rifle = 0 
pick_axe = 0 
tent = 0 
fire_wood = 0
shoes = 0
spear = 0 
bow = 0 
lazer_rifle = 0
magic = 0






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
    print(welcome2)
    print()
    print(general_store)
    print()
    print(general_store2)
    print(" Your choices for the long road ahead are as follows, minimalist Travel package for $300, normal Travel package $500 and Extensive Package $800")
    user = input(" Type 'A' for minimal, 'B for normal and 'c' for extensive")
    if user.upper() == "A":
        supply = "A"
        start()
        pathing(supply)
    elif user.upper() == "B":
        supply = "B"
        start()
        pathing(supply)
    elif user.upper() == "C":
        supply = "C"
        global spear
        spear += 1
        start()
        pathing(supply)
    else:
         play_game()


# Combat Functions 

def combat_z():
    events = ["Bitten!", "Scrached!", "Survived!"]
    randomizer = random.choice(events)
    if spear >= 1:
        print("you have used the spear to defeat the zombies")
    else:
        if randomizer == "Bitten!":
            print("No matter what you do, the bite festers")
        elif randomizer == "Scrached!":
            print("add first Aid Function")
        elif randomizer == "Survived!":
            print("You have survived the encounter!")
        else:
            print("test")


# More Events will be added in the future! 

def pathing(supply):
    random_events = [" Zombies!"]
    time.sleep(3)
    events = random.choice(random_events)
    print("You seem to have encounterd, " + events)
    if events == " Zombies!":
        combat_z()
        continue_journey(supply)
        print("test")


# Ambience for game world 
def days_traveled():
    global miles_traveled, miles_to_travel
    distance_miles = random.randint(10, 30)
    distance_days = random.randint(1,7)
    distance_miles += miles_traveled
    print("You have traveled for, " + str(distance_miles) + "many miles.")
    print("You have traveled for," + str(distance_days) + "many days.")

 


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



