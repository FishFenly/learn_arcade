import random
def app():

    miles_traveled = 0
    water_lvl = 3
    thirst = 0
    native_dist = -20
    camel_tiredness = 0
    won = False
    done = False

    print("")
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great desert.")
    print("The natives want their camel back and are chasing you down! Survive")
    print("your desert trek and out run the natives.")
    print("")
    input("Press any key to start your journey!")
    
    while not done:
        print("")
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print("")
        choice = input("What is your choice? ")
        print("")

        if choice.lower() == "q":
            print("You quit the game.")
            input()
            done = True
        elif choice.lower() == "e":
            print("Miles traveled: {}".format(miles_traveled))
            print("Drinks in canteen: {}".format(water_lvl))
            print(
                "The natives are {} miles behind you.".format(
                    (miles_traveled - native_dist)
                )
            )
            input()
        elif choice.lower() == "d":
            camel_tiredness = 0
            native_dist += random.randint(7,14)
            print("Your camel is fully rested.")
            input()
        elif choice.lower() == "c":
            miles_traveled += random.randint(10,20)
            camel_tiredness += random.randint(1,3)
            thirst += 1
            native_dist += random.randint(7,14)
            print("You urge the camel to press on as fast as it can.")
            input()
        elif choice.lower() == "b":
            miles_traveled += random.randint(5,12)
            camel_tiredness += 1
            thirst += 1
            native_dist += random.randint(7,14)
            print("You ask the camel to press on, but not too hard.")
            input()
        elif choice.lower() == "a":
            if water_lvl != 0:
                water_lvl -= 1
                thirst = 0
                print("You take a drink from your canteen, you feel refreshed.")
                input()
            else:
                print("You cant drink because your canteen is empty!")
                input()
        else:
            print("You didnt enter a valid option, try again.")
            input()

        if thirst >= 4:
            print("You are thirsty, drink something soon.")
            input()
        elif thirst == 5:
            print("You are very thirsty, you are feeling weak.")
            input()
        elif thirst >= 6:
            print("You died of thirst!")
            input()
            done = True

        if not done:
            if camel_tiredness >= 5:
                print("The camel is getting tired, you should rest soon.")
                input()
            elif camel_tiredness == 7:
                print("The camel stumbled, it looks to be really struggling.")
                input()
            elif camel_tiredness >= 8:
                print("The camel fell to the ground, its not breathing.")
                print("You stumble on for a short while, but without the camel")
                print("the natives quickly catch up.")
                input()
                done = True

            if not done:
                if (miles_traveled - native_dist) <= 10 and (miles_traveled - native_dist) != 0:
                    print("The natives are catching up!")
                    print("Hurry!")
                    input()
                elif (miles_traveled - native_dist) == 0:
                    print("The natives have caught you!")
                    input()
                    done = True

                if not done:
                    if miles_traveled >= 160 and miles_traveled < 200:
                        print("You can see the outline of a friendly town in the distance!")
                        print("Keep going!")
                        input()
                    elif miles_traveled >= 200:
                        print("You reached the town!")
                        input()
                        done = True
                        won = True

    if won:
        print("You have escaped the natives and won the game, well done!")
        input()
    else:
        print("GAME OVER!")
        print("Try again....")
        input()
app()