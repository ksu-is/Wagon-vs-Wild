import time 
import random

health_points = 50
enemy_health = 50
rifle = 1

def spear_dino():
    print("With spear in hand, you lunge at the dino!")
    time.sleep(3)
    print("The spear hits the dinosaur!")


def rifle_dino():
    print("You reloaded after the first shot, ramming down another round ball with black powder.")
    print("You shoot wildly at the dinosaur!")
    dice_rollP = random.randint(8,25)
    health_points -= dice_rollP
    dice_rollD = random.randint(10, 20)
    enemy_health -= dice_rollD

def dinosaur_encounter(): # add supply later /, "Unseen", "Animal"
    dino_events = ["Spotted!"]
    enemy_dinos = ["Velociraptor", "Coelophysis", "Microraptor", "T-Rex"]
    print("In the distance, you see something odd.")
    time.sleep(3)
    print("Dinosaurs, some with long green necks, others with sharp tusks on their heads.")
    print("They stand in a densly forested area with ferns and foliage making them nearly invisible.")
    time.sleep(5)
    if dino_events == "Spotted!":
        print("As you stare in amazement at giant creatures that have not been seen before, instinct tells you")
        print("to scan the surronding area for threats, you spot a " + enemy_dinos + " which stares at you with hungry eyes.")
        time.sleep(9)
        print("Three rush at you from the forest, they begin 200 yards away.")
        print("You have enough time to shoot one, then snapshoot another.")
        if rifle > 0:
            print("Your first shot.")
            spear_combat()
            time.sleep(3)
            print("Your second shot.")
            rifle_dino()
            print("after the last shot you grab a spear, but the dino is very fast, you have " + health_points + "HP left.")
            print("The dinosaur health is, " + enemy_health + "currently.")
            if health_points <= 0:
                print("death")
            elif enemy_health >= 1:
                print("The dinosaurs circle around for another attack!")
                spear_dino()
            elif enemy_health <= 1:
                print("Victory!")
            else:
                print("Dino Combat Fail")
    elif dino_events == "Unseen":



