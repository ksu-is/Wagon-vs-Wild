import time 
import random

magic = 0
spear = 1
rifle = 1
food_remaining = 1000
spare_wheel = 0

def forest_encounter():
    global spear, spare_wheel, food_remaining, magic
    events_forest = ["Lost!"]
    randomizerF = random.choice(events_forest)
    print("You have entered a dense forest with winding paths, passing the remains of abandoned towns \n and forelorn signs who's markings have long since eroded.")
    time.sleep(7)
    print("Following these winding paths is difficult enough while paying attention to your surroundings.")
    time.sleep(5)
    if randomizerF == "Scavenge!":
        print("You run into another abandoned town, it looks like everyone left in a hurry, there might be supplies!")
        user1 = input("Your Decision: Search the houses 'H' or town hall 'T'?").lower()
        if user1.startswith("h"):
            print("You begin to search through the houses, nearby you find...")
            time.sleep(4)
            print("A new wagon wheel as well as a spear.")
            spear += 1
            spare_wheel += 1
            print("Spear and wheel have been added to inventory.")
        else: 
            print("You begin to search through the town hall.")
            time.sleep(5)
            print("Something shines in the corner, unlike anything you have seen before.")
            time.sleep(4)
            print("A coin, it shines and glows in your hand, this could be useful to sell one day!")
            print("Magic added to inventory!")
            magic += 1 
    elif randomizerF == "Lost!":
        print("As you walk through the forest, the path becomes difficult to see, the wagon markes in the road have disappeared.")
        time.sleep(8)
        user2 = input("Do you keep going or stop and camp? G/C ").lower()
        if user2.startswith("g"):
            print("You decide to back track and hopefully find a path.")
            print("After 10 hours you have found the path once again, yet used half of your food!")
            food_remaining -= 500
            if food_remaining <= 0:
                print("You have run out of food and died.")
            else:
                print("You navigate out of the forest and continue along your journey!")
        else:
            print("You have decided to camp here for the night, you hear many different wild animals during the night!")
            time.sleep(5)
            print("When you awake the next morning, you notice some items have gone missing, \n -200 food. \n -1 spear.")
            food_remaining -= 200
            spear -= 1 
            if food_remaining <= 0:
                print("You have run out of food and died.")
            else:
                print("You continue the journey.") 


forest_encounter()





