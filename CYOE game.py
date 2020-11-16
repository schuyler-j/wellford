import random
import time

intro = input("Hello, welcome to the 'Game', would you like to play? y/n ")

if intro == "y":
    begin = input("Okay!, Let's Begin, Press Enter!" )
    print (begin)
    quest1 = input ("You see a door, do you enter? y/n ")

    if quest1 == "y":
        quest2 = input ("Door is locked, Find key? y/n ")

        if quest2 == "y":
            quest3 = input ("You fiddle through your pockets and find a brass key, try it on the door? y/n ")
            print (begin)
        else:
            print ("You're out of luck then, buddy")
            pass

        if quest3 == "y":
            items = []
            print ("*Click*, the door unlocks, you enter, a voice asks you for three wishes...")

            wish1a = input("Your first wish? - I wish for... ")
            print ("*Woosh!* A magical energy engulfs you...")
            print ("Suddenly", wish1a.upper(), "appears in your pocket.")
            items.append(wish1a)
            print (begin)

            wish2a = input("Your second wish? - I wish for... ")
            print ("*Twang*! A magical prowess entices you...")
            print ("Suddenly", wish2a.upper(), "appears in your pocket.")
            items.append(wish2a)
            print (begin)

            wish3a = input("Your third and final wish? - I wish for... ")
            print ("Zlirp*! A magical will devours you...")
            print ("Suddenly", wish3a.upper(), "appears in your pocket.")
            items.append(wish3a)
            print (begin)

            print ("Now in possession of", wish1a.upper(), "," ,wish2a.upper(), "and", wish3a.upper(), "-", "nothing can stop you!")
            print(begin)
            new1 = input("Will you use your powers for Good or Evil? ")
            moral = new1
#follow the good path
            if moral == "good":
                print ("With good will in your heart you walk down an enlightened path.")
                time.sleep(2)
                print ("You arrive at a noisy tavern and inside you see three loud dwarfs arguing")
                time.sleep(2)
                print ("The smallest one turns to you with a mischievous grin and asks...")
                time.sleep(2)
                better = input("Which is better, filthy humans(a), yummy spiders (b) or icky squids(c)? ")
                print (begin)
                if better == "b":
                    result = "big bad doodadys"
                    print ("Well, put it there partner! Let me buy you a beer!")
                elif better == "a":
                    result = "stranded souls"
                    print ("Ewwww! Should have known, by the looks of ya!")
                elif better == "c":
                    result = "flying octopi"
                    print ("Yuck! You make me sick...")

                print("..."), time.sleep(3)
                print (begin)
                print ("You black out and wake up in a barn.")
                print (begin)
                print("..."), time.sleep(3)
                

                dice_roll = random.randint(1, 6)
                if dice_roll >= 1:
                    print ("Your", wish1a, "has fallen down a well!")
                    print ("You wrap your", wish2a, "around your", wish3a, "and pray for sweet release")
                    print ("An unruly group of", result, "fall from the sky - killing you instantly")
                    print ("GAME OVER!")

        #didnt die by the dice
                else:
                    print ("You check your pockets and find nothing missing...")
                    print ("You get up and find a nearby bucket do you...")
                    print ("(a) - Wash your face?")
                    print ("(b) - Stare at yourself?")
                    print ("(c) - Have a drink?")
                    good_path = input("What is your choice? a/b/c ")
                    if good_path == "a":
                        fate = 1
                        print ("")
                    elif good_path == "b":
                        fate = 2
                    elif good_path == "c":
                        fate = 3


#follow the evil path
            elif moral == "evil":
                print ("With evil in your blood you travel down a dark path.")
                print("..."), time.sleep(3)
                input("Roll the dice to decide your fate! - Press Enter... ")
                dice_roll_evil = random.randint(1, 6)
                print (dice_roll_evil)
                if dice_roll_evil >= 2:
                    print ("You are the most unlucky fool to ever exist!")
                    print ("You traverse a nearby bridge and break every evil bone in your body")

                else:
                    print ("Congratulations!")










#didn't use the key
        else:
            print ("You feel a strange energy come over you and find your hand raised to the door with the key inside.")
            print ("*Click*, the door unlocks, you enter, a voice asks you for three wishes...")
            wish1b = input("Your first wish? - I wish for a... ")

            print ("*Woosh!*, A resistence is felt deep within your bones...")
            print ("Suddenly a", wish1b, "appears in front of you")
            print (begin)


#didn't pass through the door
    else:
        print ("A gust of wind blows you into the door, you smash through to the other side...")
        questa = input("You are cut and bleeding, bandage the wound? y/n ")

        if questa == "y":
            print ("You tear the sleeve off your shirt and wrap your wound, the bleeding subsides, for now...")
            questb = input("You feel hungry, what's for lunch? ")

            def func():
                lunch = ["ham", "apple", "twix"]
                if questb in lunch:
                    print ("You enjoy a delicious", questb)
                    print ("Feeling so nourished, you feel like a winner!")
                    print ("GAME OVER!")


                else:
                    print ("You have none of those, you starve to death")
                    print ("GAME OVER!")


            print (func())

        else:
            print ("You bleed to death...")
            print ("Game Over!")


else:
    print ("Goodbye then...")




print (intro)
