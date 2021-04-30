import time 
import random

rifle = 1
spear = 1

def chuck_norris():
    print("Your traveling through the forest, birds are chirping the wagon rumbles along with its familiar creaks and rattles.")
    time.sleep(7)
    print("Eventually, you come to an intersection, the road your on currently is called 'Peace Maker Trail'.")
    print("It crosses a gravel path that looks almost brand new, you look down at the map, cross the road and keep going.")
    time.sleep(7)
    print("suddenly, you look back at the sign startled by what was read on the map, the street you crossed was called...")
    time.sleep(8)
    print("'Chuck Norris.' Nobody crosses Chuck Norris and lives!")
    time.sleep(7)
    print("Suddenly, Chuck Norris appears infront of the wagon just 20 yards away, glaring at you.")
    print("Time is short, your choice right now will determine life or death!")
    time.sleep(7)
    print("Decision 1, you fight Chuck Norris!")
    time.sleep(5)
    print("Decision 2, you negotiate with Chuck Norris!")
    time.sleep(5)
    print("Decision 3, you run away from Chuck Norris!")
    time.sleep(5)
    user = input("What is your choice? '1', '2', '3'")
    if user == "1":
        print("Quickly, you reach for a weapon, which one do you choose? 'Spear' or 'Rifle'")
        time.sleep(3)
        user2 = input("Choose a weapon.").lower()
        if user2.startswith("s"):
            if spear > 0:
                print("You reach for the spear, chuck is closing in at a calm walk.")
                time.sleep(3)
                print("The spear is thrown, and splinters in mid air from a single roundhouse kick.")
                time.sleep(4)
                print("The sheer force of the kick flips your wagon, your journey is at an end.")
            else:
                print("You reach for a spear, yet do not have one.")
                print("Chuck's boot is the last thing you see.")
                time.sleep(4)
        elif user2.startswith("r"):
            if rifle > 0:
                print("You hesitate for a moment, then dive for the rifle.")
                time.sleep(5)
                print("You take careful aim and fire! But Chuck Norris walks through the smoke unharmed.")
                time.sleep(3)
                print("Chuck says, 'if I were a bullet I'd go around too.' ")
                print("You do not survive his attack.")
            else:
                print("You dive for a rifle, but it isn't there...")
                time.sleep(4)
                print("But Chuck was faster anyways, his mac 10 did all necissary talking.")
    elif user == "2":
        print("You think quickly, and say, 'Lets just talk this through.' Chuck just nods and says, 'Its your lucky day.'")
        time.sleep(6)
        print("You try to think of everything, but one question naggs you, are his accolades fact or fiction?")
        user3 = input("Is there anything you can think of that's fictional about Chuck Norris? 'fact'or 'fiction'" ).lower()
        if user3 == "fact":
            print("Correct, there are only 'facts' when talking about Chuck Norris.")
        else:
            print("Wrong, there are only facts' when talking about Chuck Norris.")
            
        print("Chuck says, 'How many push ups can I do at one time?'")
        user4 = input("Your Answer..." 'No punctuation!').lower()
        if user4 == "all of them":
            print("Correct!")
        else:
            print("Chuck narrows his eyes, and says, I can do 'all of them' ANS: 'all of them'")
            print("Chuck's mac 10 did the rest of the talking that day.")
        print("Chuck says, 'What item do I use in order to donate blood?'")
        user5 = input("You speak nervously and say: ").lower()
        if user5 == "a hand gun":
            print("Correct, All I bring is a hand gun and a bucket to donate blood.")
        else:
            print("Chuck simply glares at you and says, 'I use a hand gun.' ANS: 'a hand gun'")
        print("Next question")
        time.sleep(4)
        print("Chuck says, 'I'll let you go if you can answer this question and the one after it, \n How many times have I counted to infinity?'")
        user6 = input("Your answer: (Type a number)")
        if user6 == "2":
            print("Yea, I've counted to infinity twice.")
        else:
            print("'Wrong, I've counted to infinity twice!' Chucks's boot is the last thing you see.")
        print("Final Question!")
        print("Chuck says, 'What time of year do I go out hunting?'")
        user7 = input("Your Answer: ").lower()
        if user7.startswith("n"):
            print("'Correct, saying I hunt implies a chance of failure.'")
        else:
            print("'Wrong, saying I hunt implies a chance of failure.'")
    elif user == "3":
        print("Nobody runs from Chuck Norris and gets away with it.")
        time.stop(6)


chuck_norris()






