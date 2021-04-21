import time 
import random

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
    user1 = input("Enter a numeric Value").lower()
    if user1 == "24":
        
        print(str(user1) + " miles per hour is correct, now answer the final answer.")
    else:
        print("Wrong, says the wizard in long silk robes, he strikes you with lightning.")
    user2 = input("Your response to the third question.").lower()
    if user2 == "damascus":
        
        print("Correct, you have answered all our questions and may go in peace!")
        time.sleep(4)
        print("You quickly gather the reins of the horse atop the wagon and continue along the path")
        time.sleep(3)
    else:
        print("Wrong, says the wizard in long silk robes, he strikes you with lightning.")


wizard_encounter()