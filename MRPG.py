"""Define player attributes"""
weapons = {'longsword': 1, 'midas': 4, 'black_death': 7, 'terry': 12}
pstats = {'name': '', 'atk': 6, 'def': 40, 'def_cur': 40,
          'spd': 3, 'pnt': 10, 'wep': weapons['longsword']}
training = {'push-ups': 2, 'gym': 7, 'intense_conditioning': 17}
money = {'bal': 0}
skill = int(pstats['atk']) + int(pstats['def']) + int(pstats['spd']) + int(pstats['pnt'])
# Enemies
enemy = ('bunny', 'wolf', 'pang')
bunny = {'name': 'elf', 'atk': 2, 'def': 3, 'spd': 7}
wolf = {'name': 'wolf', 'atk': 4, 'def': 4, 'spd': 5}
pang = {'name': 'pang', 'atk': 15, 'def': 14, 'spd': 9}

loc = {'crowthorne': 1, 'college': 2, 'broadmoor': 3, 'pangs_castle': 4}

def intro():
    print("\n\n\n\n\nWelcome to M-RPG, 'PLAYER'! \n[Press 'Enter]")
    str(input())
    pstats['name'] = str(input("Select name: "))

def stats_upgrade():
    # Beta
    def u_attack():
        print("You have selected attack! You currently have: " + str(pstats['atk'])), " attack\n\n"
        print("How many points would you like to add?")
        a = int(input())
        print(a, " points selected. Checking points...\n\n")
        str(input())
        d = int(pstats['pnt'])
        if a < int(pstats['pnt']):
            print("Success! You have enough points. Adding stats...\n\n")
            print("[Press Enter]")
            str(input())
            c = int(pstats['atk'])
            del pstats['pnt']
            del pstats['atk']
            pstats['pnt'] = d - a
            pstats['atk'] = a + c
            print("New attack: ", int(pstats['atk']))
            print("New points: ", str(pstats['pnt']))
            print("[Press Enter]")
            return()
        else:
            print("You do not have enough points for this! Returning to upgrades...")
            return()

    def u_defence():
        print("You have selected defence! You currently have: " + str(pstats['def'])), " defence\n\n"
        print("Adding points works like a multiplier. How many would you like to add?")
        a = int(input())
        print(a, " points selected. Checking points...\n\n")
        str(input())
        d = int(pstats['pnt'])
        if a < int(pstats['pnt']):
            print("Success! You have enough points. Adding stats...\n\n")
            print("[Press Enter]")
            str(input())
            c = int(pstats['def'])
            del pstats['def']
            del pstats['pnt']
            pstats['pnt'] = d - a
            pstats['def'] = a * (2 ** c)
            print("New defence: ", str(pstats['def']))
            print("New points: ", str(pstats['pnt']))
            print("[Press Enter]")
            return ()
        else:
            print("You do not have enough points for this! Returning to upgrades...")
            return ()

    def u_speed():
        print("You have selected speed! You currently have: " + str(pstats['spd'])), " speed\n\n"
        print("How many points would you like to add?")
        a = int(input())
        print(a, " points selected. Checking points...\n\n")
        d = int(pstats['pnt'])
        if a < int(pstats['pnt']):
            print("Success! You have enough points. Adding stats...\n\n")
            print("[Press Enter]")
            str(input())
            c = int(pstats['spd'])
            del pstats['spd']
            del pstats['pnt']
            pstats['pnt'] = d - a
            pstats['spd'] = a + c
            print("New speed: ", str(pstats['spd']))
            print("New points: ", str(pstats['pnt']))
            print("[Press Enter]")
            return ()
        else:
            print("You do not have enough points for this! Returning to upgrades...")
            return()

    print("\n\n\n\nWelcome to the stats upgrade selection! You will now be guided throughout the upgrade process. \n\n")
    print("[Hit Enter]")
    str(input())
    print("\n\nChecking points...\n[Hit Enter]")
    str(input())
    if int(pstats['pnt']) > 0:
        print("You have ", str(pstats['pnt']), "points to upgrade\n\n[Hit Enter]")
        str(input())
        print("\n\nXXXXXXX\n\nSelect which attribute you would like to upgrade, and enter the corresponding number:\n\n"
              "[1: attack], [2: defence], [3: speed]")
        i = int(input())
        if i == 1:
            u_attack()
        elif i == 2:
            u_defence()
        elif i == 3:
            u_speed()
        print("Stats selection is now complete! \n\n\nIf you would like to change another attribute, hit 1. If not"
              ", hit 2\n\n")
        b = int(input())
        if b == 1:
            stats_upgrade()
        elif b == 2:
            return()
        return()
    else:
        print("Not enough points! You will be returned to the game.\n\n[Hit Enter]")
        str(input())
        return()


def trip_gen(n, tr):
    # Defines how many encounters will happen during trip
    # n = trip difficulty
    # import random
    # tr = random.randint(0, 3)
    if tr == 0:
        print("Whew! No enemies in sight.")
        return()
    if tr == 1:
        print("One enemy! Prepare to fight.")
        encounter_gen(n)
        return()
    if tr == 2:
        print("Two enemies! This is gonna be tough...")
        encounter_gen(n)
        encounter_gen(n)
    if tr == 3:
        print("Three enemies! \n\nOH MY GOD PLEASE HELP ME LOR-\n\n*face chewed off*")
        encounter_gen(n)
        encounter_gen(n)
        encounter_gen(n)
        return()


def encounter_gen(n):
    # n = encounter difficulty
    import random
    e = 1
    es = random.randint(0, 2)
    if n > 2:
        e += 1
    f = enemy[es]
    print("Enemy is", f)
    print("Do you wish to [fight/flee]?")
    a1 = str(input())
    if a1 == 'fight':
        combat(f, n)
        return()
    elif a1 == 'flee':
        print("\n\nAttempting to flee...\n\n[Press Enter]")
        str(input())
        if int(pstats['spd']) >= (int(f['spd']) * e):
            print("Success! You have escaped.")
            print("[Enter] to continue")
            str(input())
            return()
        else:
            print("Failure! You have not managed to escape, prepare for combat!!!")
            print("[Press Enter]")
            str(input())
            combat(f, n)
        return()


def combat(f, n):

    def win(x, y):
        print("Crushing victory! Gained 1 upgrade point. Gained ", 10 * y, " money.\n\n[Press Enter]")
        pnts = pstats['pnt']
        del pstats['pnt']
        pstats['pnt'] = pnts + 1
        del pstats['def_cur']
        pstats['def_cur'] = x
        money['bal'] += 10 * y
        str(input())
        return()

    print("Enemy attack: ", str(enemy[f['atk']]), ". Enemy defence: ", str(f['def']), "\n\n")
    print("Your attack: ", str(pstats['atk']), ". Your defence: ", str(['def']), "\n\n")
    print("You attack first!")
    pa = int(pstats['atk'])
    pd = int(pstats['def_cur'])
    ea = int(enemy[f['atk']])
    ed = int(enemy[f['def']])
    if pa >= ed:
        win(pd, n)
        return()
    elif pa < ed:
        print("Enemy on ", pa - ed, " defence. Enemy attacks!\n\n[Hit Enter]")
        str(input())
        ed -= pa
        pd -= ea
        if pd <= 0:
            death()
            return ()
        else:
            print("Enemy is on ", str(ed), "defence.")
            ed -= pa
            if ed <= 0:
                win(pd, n)
                return ()
            else:
                print("Enemy has still survived!"
                      "\nCurrent enemy defence is ", ed)
                print("[Press Enter]")
                str(input())
                pd -= ea
                if pd <= 0:
                    death()
                    return ()
                else:
                    print("Your defence is on ", pd, "\n\n[Press Enter]")
                    ed -= pa
                    if ed <= 0:
                        win(pd, n)
                    else:
                        print("HOW LONG IS THIS GONNA TAKE?!")
                        pd -= ea
                        if pd <= 0:
                            death()
                            return ()
                        else:
                            win(pd, n)
                            return()


def death():
    print("Failure! You have been killed! Press enter to continue\n")
    print("You will be returned to Crowthorne.")
    str(input())
    bal = money['bal']
    del money['bal']
    money['bal'] = bal * 0.8
    location()
    return()


def location():
    print("You arrive at the town of Crowthorne!\n\n[Hit Enter]")
    str(input())

    def choices():
        print("You have a variety of options available to you:\n"
              "\n[1]: Tavern"
              "\n[2]: Inn"
              "\n[3]: Market."
              "\n[4]: Library"
              "\n[5]: Proceed with game"
              "\n\n\nPick one, and hit Enter.")
        v = int(input())
        if v == 1:
            print("Welcome to the tavern! You will now be led through the trait upgrade menu.\n\n[Hit Enter]")
            str(input())
            stats_upgrade()
            choices()
        if v == 2:
            print("Welcome to the inn! Here your defence will be regained, for the small cost of $10!\n\n"
                  "[1: yes][2: no")
            inp = int(input())
            if inp == 1:
                print("defence regenerated!")
                del pstats['def_cur']
                temp = pstats['def']
                pstats['def_cur'] = temp
            if inp == 2:
                print("Returned to town!")
            print("Thanks for visiting the inn!")
            choices()
        if v == 3:
            print("Welcome to the market! You will now be guided through the purchase menu. [WIP")
            print("[Hit Enter to continue]")
            str(input())
            choices()
        if v == 4:
            print("Welcome to the library! Here you can find out more about the storyline, and what is going on!")
            print("[Press Enter]")
            str(input())
            print("You have several choices for how to obtain information, try them out and see what happens!"
                  "\n[1] Research tome"
                  "\n[2] Town encyclopedia"
                  "\n[3] Talk to librarian"
                  "\n[4] Snoop around library"
                  "\n[5] Leave library")
            lib_choice = str(input())
            if lib_choice == 1:
                print("\n\n\n\nYou pick up the heavy tome. It feels like it hasn't been used in years")
                print("[Press Enter]")
                print("It reads:\n\n")
                print('"The town of Crowthorne used to be a bustling hub of commerce and creativity.'
                      'Many years ago, there was a great ruler of the township. His name was Pang. He was kind, '
                      'generous and good hearted. All of the citizens loved him.')
                print("Press Enter")
                str(input())
                print('"\n\nOne day, Bance, the owner of the tavern, became addicted to local milkshakes from the inn, '
                      'owned by Pang. Upon seeing the interest in his product, Pang raised prices fifteenfold. '
                      'Bance was outraged, and declared war on Pang. He had the funds, and he had the support, '
                      'because everyone loved his tavern. And so Pang was exiled from Crowthorne.\n\n')
                print("[Press Enter]")
                str(input())
                print("After many years of absence, Bance eventually became the ruler of Crowthorne. He was a tyrant: "
                      "he constantly demanded his 'subjects' bring him milkshakes. He was never happy. Pang decided "
                      "to spite him, and he returned with some men to lay waste to the old milkshake factory.")
                print("\n\n[Press Enter]\n\n")
                str(input())
                print("And so, the history of Crowthorne has been a sad and turbulent time in the lives of many. "
                      "This brings us to where we are today. (pretty much...)\n\n\n\n")
                print("[Press Enter]")
                str(input())
                print("You put down the Tome, and return to town.")
                choices()
                return()
            elif lib_choice == 2:
                print("You do not have enough skills for this!")
                print("[Press Enter] to return to town")
                str(input())
                choices()
            elif lib_choice == 3:
                print("You do not have enough skills for this!")
                print("[Press Enter] to return to town")
                str(input())
                choices()
            elif lib_choice == 4:
                print("You do not have enough skills for this!")
                print("[Press Enter] to return to town")
                str(input())
                choices()
            elif lib_choice == 5:
                print("Returning to town! [Press Enter]")
                str(input())
                choices()
            choices()
        if v == 5:
            print("You have selected to leave town. [story/quest] ")
            selection = str(input())
            if selection == 'story':
                import random
                diff = random.randint(0, 3)
                trip_gen(diff, 2)
                location()
            elif selection == 'quest':
                print("WIP")
                str(input())
                return()
    choices()
    return()


def story():
    print("Welcome to the story! To find out more about the prologue and intro, go to town and visit the library")


#########################################
location()

