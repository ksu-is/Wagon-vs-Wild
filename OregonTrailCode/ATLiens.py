from pprint import pprint
import random
import time
import math

class hero:
    def __init__(self, Hhealth, Hattack, Hluck, Hrange, Hdefense, Hmagic, Hname):
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.range = Hrange
        self.defense = Hdefense
        self.magic = Hmagic
        self.name = Hname

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getLuck(self):
        return self.luck
    def getrange(self):
        return self.range
    def getdefense(self):
        return self.defense
    def getMagic(self):
        return self.magic
    def getName(self):
        return self.name

    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setLuck(self, newLuck):
        self.luck = newLuck
    def setrange(self, newrange):
        self.range = newrange
    def setdefense(self, newdefense):
        self.defense = newdefense
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setName(self, newName):
        self.name = newName


class enemy:
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename):
        self.health = Ehealth
        self.attack = Eattack
        self.special = Especial
        self.chance = Echance
        self.name = Ename

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getSpecial (self):
        return self.special
    def getChance(self):
        return self.chance
    def getName(self):
        return self.name

    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setSpecial(self, newSpecial):
        self.special = newSpecial
    def setChance(self, newChance):
        self.chance = newChance
    def setName(self, newName):
        self.name = newName



class boss (enemy):
    def __init__(self, Ehealth, Eattack, Especial, Echance, Ename, EsuperMove):
        super().__init__(Ehealth, Eattack, Especial, Echance, Ename)

        self.superMove = EsuperMove

    def getSuper(self):
        return self.superMove
    
    def setSuper(self, newSuperMove):
        self.superMove = newSuperMove

def createClass():
    a = input("An Alien aircraft has appeared over the horizon...\n2  The clouds start to boil and when the craft breaks through them, you realizes it's heading directly to Atlanta\n2.  The alien craft hovers over Atlanta slowly settling into place. Then... Silence\n2.  Suddenly, aliens begin spewing out of the lower deck of the aircraft\n2.  Slowly it dawns on you that it's time to get out of town.  You must save yourself and escape to North Georgia before it's too late\n2!  Before you begin your journey, please select between a ranged (1) or melee class (2)...")
    while a != "1" and a != "2":
        print("Invalid selection...")
        a = input("Before you begin your journey, please select between a ranged (1) or melee based class (2)...")

    if a == "1":
        heroAttack = 5
        herodefense = 10

    elif a == "2":
        heroAttack = 10
        herodefense = 5

    b = input ("Press enter to roll a dice...")
    time.sleep(0.2)
    print("rolling dice...")
    heroLuck = random.randint(0,10)
    print ("you have", heroLuck, "luck out of 10")

    c = input ("Are you more of an archer (1) or magic user (2)?...")
    while c != "1" and c != "2":
        print("Invalid selection...")
        c = input ("Are you more of an archer (1) or magic user (2)?...")

    
    if a == "1":
        herorange = 10
        heroMagic = 5

    elif a == "2":
        herorange = 5
        heroMagic = 10

    heroName = input("What is your name player??")
    print("Welcome", heroName, "!!!!")

    return(heroAttack, heroLuck, herorange, herodefense, heroMagic, heroName)


def enemyGen(levelBoss):
    temp = []
    file = open("adjective.txt","r")
    lines = file.readlines()
    adjective = lines[random.randint(0,len(lines)-1)][:-1]
    file.close
    file = open("aliens.txt","r")
    lines = file.readlines()
    aliens = lines[random.randint(0,len(lines)-1)][:-1]
    file.close

    if levelBoss == False:
        health = random.randint(25,50)
        attack = random.randint(5,7)
        special = random.randint(5,7)
        chance = random.randint(1,10)

        return enemy(health, attack, special, chance, adjective+" "+aliens)

    else:
        health = random.randint(50,55)
        attack = random.randint(5,7)
        special = random.randint(10,12)
        chance = random.randint(1,8)
        superMove = random.randint(13,15)

        return boss(health, attack, special, chance, adjective+" "+aliens, superMove)

def enemyAttack(hitChance, attackValue, name, defense):
    print(name, "is winding up for an attack...")
    hit = random.randint(0,10)
    if hitChance >= hit:
        print("The alien has struck you!!!")
        loss = attackValue - defense
        print("You stagger losing...", loss, "health")
        return math.ceil(loss)
    else:
        print("The alien misses! It bolsters in frustration")
        return 0

def hitChance(luck):
    hit = random.randint(0,4)
    if luck < hit:
        print("MISS!")
        return False

    else:
        print("You hit the alien!")
        return True

def isDead(health):
    if health < 1:
        return True
    else:
        return False

def loot(luck, genCharacter):
    lootChance = random.randint(0,4)
    if luck < lootChance:
        print("NO LOOT FOR YOU!")

    else:
        tableNum = random.randint(0,4)
        lootTableList = ["items","range","defense","magic","attack"]
        itemType = lootTableList[tableNum]
        file = open(itemType+".txt","r")
        lines = file.readlines()

        print("The alien dropped a....")

        item = random.randint(0,len(lines)-1)

        itemLine = lines[item]
        splitItemLine = itemLine.split(",")

        name = splitItemLine[0]
        value = int(splitItemLine[1])

        print(name)

        if itemType == "attack":
            genCharacter.setAttack(genCharacter.getAttack()+value)
            print("Your new attack is...")
            print(genCharacter.getAttack())

        elif itemType == "range":
            genCharacter.setrange(genCharacter.getrange()+value)
            print("Your new range Attack is...")
            print(genCharacter.getrange())

        elif itemType == "defense":
            genCharacter.setdefense(genCharacter.getdefense()+value)
            print("Your new attack is...")
            print(genCharacter.getdefense())

        elif itemType == "magic":
            genCharacter.setMagic(genCharacter.getMagic()+value)
            print("Your new Magic attack is...")
            print(genCharacter.getMagic())

        else:
            
            if splitItemLine[2] == "luck":
                genCharacter.setLuck(genCharacter.getLuck()+value)
                print("Your new Luck  is...")
                print(genCharacter.getLuck())

            elif splitItemLine[2] == "health":
                genCharacter.setHealth(genCharacter.getLuck()+value)
                print("Your new Health  is...")
                print(genCharacter.getHealth())

                                     
def gameOver(enemyDead):
    if enemyDead == True:
        print("Oh no!  Another alien appears from the craft!!!")

    else:
        print("You are out health")
        print("Better luck next time!!")
        exit()

def battle(genEnemy, genCharacter):
    print("You hear an Alien craft land just beyond the ridge ahead.  Over the hill the alien appears.")
    print("Its a...", genEnemy.getName(), "Looking for a fight!")
    print("Check out its stats....")
    pprint(vars(genEnemy))

    battle = True

    while battle == True:
        
        print("1. Sword Attack\n2. Range Attack \n3. Magic Attack")
        choice = input()

        while choice != "1" and choice != "2" and choice != "3":
            print("OOPS....Only enter 1, 2 or 3...")
            print("1. Sword Attack\n2. Range Attack\n3. Magic Attack")
            choice = input()

        if choice == "1":
            damage = genCharacter.getAttack()

        elif choice == "2":
            damage = genCharacter.getrange()

        else:
            damage = genCharacter.getMagic()

        print("You wind up for the attack!!!...")
        hit = hitChance(genCharacter.getLuck())

        if hit == True:
            genEnemy.setHealth(genEnemy.getHealth() - damage)
            print("You've hit the alien!!!")
            print("The aliens health is now....", genEnemy.getHealth())

        else:
            print("Your attack missed!")

        enemyDead = isDead(genEnemy.getHealth())

        if enemyDead == False:
            genCharacter.setHealth(genCharacter.getHealth() - enemyAttack(genEnemy.getChance(), genEnemy.getAttack(), genEnemy.getName(), genCharacter.getdefense()))
            
            characterDead = isDead(genCharacter.getHealth())

            if characterDead == True:
                battle = False
                return False

            else:
                print("Your characters remaining health is....", genCharacter.getHealth())

        else:
            battle = False
            print("You have defeated the alien!")
            print("Did it drop any loot?.....")
            loot(genCharacter.getLuck(), genCharacter)

            return True


def levelGenerator(character, level):

    maxNumberOfEnemies = math.ceil(level*5)
    for x in range(0, maxNumberOfEnemies):
        bossChance = random.randint(1,10)
        if bossChance > 7:
            levelBoss = True

        else:
            levelBoss = False

        characterDead = battle(enemyGen(levelBoss), character)
        gameOver(characterDead)


def main():
    classData = createClass()
    character = hero(100, classData[0], classData[1], classData[2], classData[3], classData[4], classData[5])
    pprint(vars(character))
    print("Level 1...Midtown")
    levelGenerator(character, 1)
    print("Level 2...Marietta")
    levelGenerator(character, 2)
    print("Level 3...Kennesaw")
    levelGenerator(character, 3)
    print("Level 4...Woodstock")
    levelGenerator(character, 4)
    print("You've escaped the ALien invastion and have made it to Canton!")
    pprint(vars(character))
    
    
main()

    
