def app():
    room_list = []
    room_list.append(
        ["It's raining, you are standing on the exit platform in the shuttleport.\n You can see the exit onto the street ahead of you.",
        1,None,None,None])
    room_list.append(
        ["The main street is deserted. Around you, you can see abandoned shop fronts and street stalls.",
        2,None,0,None])
    room_list.append(
        ["This part of the main street is steaming as the rain hits the freshly scored ground.\n It looks like violence has happened here",
        6,3,1,None])
    room_list.append(
        ["You notice a hole in the ground. On closer inspection, it appears to lead into a man made cavern",
        None,None,4,2])
    room_list.append(["There doesnt seem to be anything interesting in this room.",3,5,None,None])
    room_list.append(
            ["The room looks like a horror scene, blood and bodies everywhere.\n At the end of the room a pedestal with something shimmering in the light.",
            None,None,None,4])
    room_list.append(
        ["The end of the street is blocked by rubble and debris. You cannot go any further this way.",
        None,None,2,None])

    current_room = 0
    done = False

    ## Game Loop ##

    while not done:
        print(room_list[current_room][0])
        print()
        interaction = input("What do you want to do now? ")
        print()

        if interaction == "go north":
            next_room = room_list[current_room][1]
            if next_room == None:
                print("You cannot go that way.")
                print()
            else:
                current_room = next_room
        elif interaction == "go east":
            next_room = room_list[current_room][2]
            if next_room == None:
                print("You cannot go that way.")
                print()
            else:
                current_room = next_room
        elif interaction == "go south":
            next_room = room_list[current_room][3]
            if next_room == None:
                print("You cannot go that way.")
                print()
            else:
                current_room = next_room
        elif interaction == "go west":
            next_room = room_list[current_room][4]
            if next_room == None:
                print("You cannot go that way.")
                print()
            else:
                current_room = next_room
        elif interaction == "quit" or interaction == "q":
            quit()

        else:
            print("You cant do that, try typing 'go north' or 'go south' etc.")
            print()

app()