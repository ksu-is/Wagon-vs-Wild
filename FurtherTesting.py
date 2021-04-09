def pathing(supply):
    random_events = [" Zombies!"]
    time.sleep(3)
    events = random.choice(random_events)
    print("You seem to have encounterd, " + events)
    if events == " Zombies!":
        combat_z()
        print("Test")

def combat_z():
    events = ["Bitten!", "Scrached!", "Survived!"]
    randomizer = random.choice(events)
    if spear >= 1:
        print("you have used the spear to defeat the zombies")
    else:
        if randomizer == "Bitten!":
            print("No matter what you do, the bite festers")
        elif randomizer == "Scrached!":
            print("add first Aid Functino")
        elif randomizer == "Survived!":
            print("You have survived the encounter!")
        else:
            print("test")