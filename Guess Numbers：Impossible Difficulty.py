#The file size is only about 17.8KB.😀

#I created this when I was √196 years old.🧐

#I know I didn't do a good job with this,:|
#    --but you can do it better.:)

#Share your work with your friends!;)

import random
import time

def play_game():
    exit_game = "no"
    level = 1
    chance = 14
    highest_number = 99
    lowest_number = 0
    chance_last = chance
    while True:
        print (" " * (74 - int((len("1.Easy.") / 2))),"|    1.Easy.","     |    2.Normal.    |\n\n"
                 ," " * (76 - int((len("3.Difficult.") / 2))),"|    3.Difficult.","|    4.Impossible.|\n\n"
                 ," " * (88 - int((len("Which code do you want?:" ) / 2))),end="")
        difficulty_mode = input("Which code do you want?: ")
        if str(difficulty_mode) not in ["1","Easy","easy","2","Normal","normal","3","Difficult","difficult","4","Impossible","impossible"]:
            r = random.randint(1,2)
            if r == 1:
                print ("\n"," " * (88 - int((len("Sorry,I can't understand. Please input again.") / 2))),"Sorry,I can't understand. Please input again.")
            else:
                print ("\n"," " * (88 - int((len("???") / 2))),"???")
            continue
        else:
            if difficulty_mode in ["1", "Easy", "easy"]:
                difficulty_mode = 1
                difficulty_print = "Easy"
            elif difficulty_mode in ["2", "Normal", "normal"]:
                difficulty_mode = 2
                difficulty_print = "Normal"
            elif difficulty_mode in ["3", "Difficult", "difficult"]:
                difficulty_mode = 3
                difficulty_print = "Difficult"
            elif difficulty_mode in ["4", "Impossible", "impossible"]:
                difficulty_mode = 4
                difficulty_print = "Impossible"
        break
    print ("\n\n<","-" * (88 - int((len("Game Start") / 2))),"Game Start","-" * (88 - int((len("Game Start") / 2))),">\n\n"," " * (88 - int((len("---------loading--------") / 2))),"---------loading--------\n")
    time.sleep(0.5)
    print (" " * (89 - int((len("|loading>            0%|") / 2))),"|loading>            0%|\n")
    time.sleep(0.1)
    print (" " * (89 - int((len("|loading..>         25%|") / 2))),"|loading..>         25%|\n")
    time.sleep(0.1)
    print (" " * (89 - int((len("|loading.....>      50%|") / 2))),"|loading.....>      50%|\n")
    time.sleep(0.1)
    print (" " * (89 - int((len("|loading.......>    75%|") / 2))),"|loading.......>    75%|\n")
    time.sleep(0.1)
    print (" " * (89 - int((len("|loading..........>100%|") / 2))),"|loading..........>100%|\n")
    print (" " * (89 - int((len("------loading over------") / 2))),"------loading over------\n")
    time.sleep(0.1)
    print (" " * (89 - int((len("--------------------------Game Rules-------------------------") / 2))),"--------------------------Game Rules-------------------------\n"
             ," " * (88 - int((len("|1.You need to input right number;                          |") / 2))),"|1.You need to input right number;                          |\n"
             ," " * (88 - int((len("|2.You'd better not make any input errors;                  |") / 2))),"|2.You'd better not make any input errors;                  |\n"
             ," " * (88 - int((len("|3.Select the Appropriate Difficulty;                       |") / 2))),"|3.Select the Appropriate Difficulty;                       |\n"
             ," " * (89 - int((len("|4.Lowest_number some time will be negative number.          |") / 2))),"|4.Lowest_number some time will be negative number.         |\n"
             ," " * (89 - int((len("-------------------------Game Rules--------------------------") / 2))),"-------------------------Game Rules--------------------------\n\n"
             ," " * (87 - int((len("Welcome to my second Python program, which I created when I was  √196  years old.") / 2))),"Welcome to my second Python program, which I created when I was  √196  years old.\n\n"
             ," " * (87 - int((len("Let's see how many times you can guess correctly.") / 2))),"Let's see how many times you can guess correctly.\n\n"
             ," " * (87 - int((len("The number well start from '0~99'.") / 2))),"The number well start from '0~99'.\n"
             ," " * (76 - int((len("For every correct guess--") / 2))),"For every correct guess--\n"," " * (112 - int((len("--The (H/L) Number well change higher and lower.") / 2))),"--The (H/L) Number well change higher and lower.\n\n"
             ," " * (90 - int((len("Let's start!!!") / 2))),"Let's start!!!\n\n"
             ," " * (90 - int((len("If you want EXIT--") / 2))),"If you want EXIT--\n"," " * (98 - int((len("--Please input 'EXIT'.") / 2))),"--Please input 'EXIT'.\n\n"
             ," " * (74 - int((len("And if you want Change Mode--") / 2))),"And if you want Change Mode--\n"," " * (102 - int((len("--Please input 'Change mode.'") / 2))),"--Please input 'Change mode.'\n\n\n")
    time.sleep(0.25)
    for i in range(difficulty_mode):
        chance -= random.randint(2,3)
    random_number = random.randint(lowest_number,highest_number)
    print ("\n\n<","-" * int(78 - (len(difficulty_print))),"Mode -",difficulty_print
           ," | Level -",level,"-" * int(83 - (len(difficulty_print))),">\n"
           ," " * (82 - int((len("Random Number: ") / 2))),"Random Number: ",lowest_number,"~",highest_number,"\n"
           ," " * (85 - int((len("Chance:") / 2))),"Chance: ",chance)
    while chance != 0:
        time.sleep(0.5)
        print ("\n\n"," " * (88 - int((len("Please set your Answer here: ") / 2))),end="")
        player_guess = input("Please set your Answer here: ")
        if player_guess.lower() == "exit":
            print ("\n"," " * (88 - int((len("Do you want exit?: ") / 2))),end="")
            exit_game = input("Do you want exit?: ")
            if exit_game.lower() == "yes":
                break
            else:
                random_choice = random.randint(1,2)
                if random_choice == 1:
                    print ("\n"," " * (88 - int((len("Maybe you input wrong.") / 2))),"Maybe you input wrong.")
                else:
                    print ("\n"," " * (88 - int((len("Let's continue.") / 2))),"Let's continue.")
                exit_game = "no"
                continue
        if player_guess.lower() == "change mode":
            exit_game = "no"
            level = 1
            chance = 14
            highest_number = 99
            lowest_number = 0
            while True:
                print (" " * (74 - int((len("1.Easy.") / 2))),"|    1.Easy.","     |    2.Normal.    |\n\n"
                         ," " * (76 - int((len("3.Difficult.") / 2))),"|    3.Difficult.","|    4.Impossible.|\n\n"
                         ," " * (88 - int((len("Which code do you want?:" ) / 2))),end="")
                difficulty_mode = input("Which code do you want?: ")
                if difficulty_mode not in ["1","Easy","easy","2","Normal","normal","3","Difficult","difficult","4","Impossible","impossible"]:
                    random_choice = random.randint(1,2)
                    if random_choice == 1:
                        print ("\n"," " * (88 - int((len("Sorry,I can't understand. Please input again.") / 2))),"Sorry,I can't understand. Please input again.")
                    else:
                        print ("\n"," " * (88 - int((len("???") / 2))),"???")
                    continue
                else:
                    if difficulty_mode in ["1", "Easy", "easy"]:
                        difficulty_mode = 1
                        difficulty_print = "Easy"
                    elif difficulty_mode in ["2", "Normal", "normal"]:
                        difficulty_mode = 2
                        difficulty_print = "Normal"
                    elif difficulty_mode in ["3", "Difficult", "difficult"]:
                        difficulty_mode = 3
                        difficulty_print = "Difficult"
                    elif difficulty_mode in ["4", "Impossible", "impossible"]:
                        difficulty_mode = 4
                        difficulty_print = "Impossible"
                break
            for i in range(difficulty_mode):
                chance -= random.randint(2,3)
            random_number = random.randint(lowest_number,highest_number)
        try:
            guess = int(player_guess)
        except ValueError:
            random_choice = random.randint(1,3)
            if random_choice == 1:
                print ("\n"," " * (88 - int((len("Sorry-What did you say?") / 2))),"Sorry-What did you say?")
            elif random_choice == 2:
                print ("\n"," " * (88 - int((len("What's this???") / 2))),"What's this???")
            else:
                print ("\n"," " * (88 - int((len("???") / 2))),"???")
            continue
        if guess > highest_number or guess < lowest_number:
            print ("\n"," " * (88 - int((len("Outside the random range!!") / 2))),"Outside the random range!!")
            continue
        if guess == random_number:
            random_choice = random.randint(1,3)
            if random_choice == 1:
                print ("\n"," " * (88 - int((len("High five!👋 Your guess is Right!") / 2))),"High five! Your guess is Right!")
            elif random_choice == 2:
                print ("\n"," " * (88 - int((len("Your guess is Right!!!") / 2))),"You get This answer!!!")
            else:
                print ("\n"," " * (88 - int((len("Celebrate For You!") / 2))),"Celebrate For You!")
            level += 1
            chance_last = chance
            if difficulty_mode == 1:
                highest_number = int(highest_number * 1.2 + 5)
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.02)))
                range_size = highest_number - lowest_number + 1
                chance += max(random.randint(3,5), int(range_size ** 0.35) + level)
            elif difficulty_mode == 2:
                highest_number = int(highest_number * 1.5 + 10)
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.05)))
                range_size = highest_number - lowest_number + 1
                chance += max(random.randint(3,4), int(range_size ** 0.3) + level)
            elif difficulty_mode == 3:
                highest_number = int(highest_number * 2.0 + 15)
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.10)))
                range_size = highest_number - lowest_number + 1
                chance += max(random.randint(2,3), int(range_size ** 0.25) + level // 2)
            else:
                highest_number = int(highest_number * (2.5 + level * 0.1))
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.20)))
                range_size = highest_number - lowest_number + 1
                chance = max(random.randint(1,2), int(range_size ** 0.2) + level // 3)
            time.sleep(0.25)
            print ("\n\n<","-" * int(78 - (len(difficulty_print))),"Mode:",difficulty_print," | Level:",level - 1," - Cleared","-" * int(73 - (len(difficulty_print))),">\n")
            time.sleep(0.25)
            random_choice = random.randint(0,1)
            if random_choice == 0:
                print ("\n"," " * (88 - int((len("Let's proceed to the next' guess....") / 2))),"Let's proceed to the next' guess....")
            else:
                print ("\n"," " * (87 - int((len("Level Up!") / 2))),"Level Up!")
            time.sleep(0.25)
            print ("\n"," " * (86 - int((len("Level:") / 2))),"Level:",level - 1,"-->",level)
            random_number = int(random.randint(lowest_number, highest_number))
            time.sleep(0.5)
            if difficulty_mode == 1:
                difficulty_print = "Easy"
            elif difficulty_mode == 2:
                difficulty_print = "Normal"
            elif difficulty_mode == 3:
                difficulty_print = "Difficult"
            elif difficulty_mode == 4:
                difficulty_print = "Impossible"
            print ("\n\n<","-" * int(78 - (len(difficulty_print))),"Mode:",difficulty_print," | Level -",level,"-" * int(84 - (len(difficulty_print))),">\n"
                     ," " * (82 - int((len("Random Number: ") / 2))),"Random Number: "
                      ,lowest_number,"~",highest_number,"\n"
                     ," " * (85 - int((len("Chance:") / 2))),"Chance: ",chance_last,"-->",chance)
            print ("\n\n<","-" * int(78 - (len(difficulty_print))),"Mode:", difficulty_print
                     ," | Level -",level,"-" * int(84 - (len(difficulty_print))),">\n"
                     ," " * (82 - int((len("Random Number: ") / 2))),"Random Number: ", lowest_number, "~", highest_number
                     ,"\n"," " * (85 - int((len("Chance:") / 2))),"Chance: ", chance)
            continue
        else:
            if guess > random_number:
                if guess - random_number <= int((highest_number + 1) * 0.05 / level + level * random.randint(0,5)):
                    random_choice = random.randint(1,2)
                    if random_choice == 1:
                        print ("\n"," " * (88 - int((len("It's very Close.       (your guess)A little higher.") / 2))),"It's very Close.       (your guess)A little higher.")
                    else:
                        print ("\n"," " * (88 - int((len("(your guess is higher)Very Close.") / 2))),"(your guess is higher)Very Close.")
                elif guess - random_number <= int((highest_number + 1) * 0.1 / level + level * random.randint(0,10)):
                    random_choice = random.randint (1,2)
                    if random_choice == 1:
                        print ("\n"," " * (88 - int((len("Bit higher...        Your guess is higher.") / 2))),"Bit higher...        Your guess is higher.")
                    else:
                        print ("\n"," " * (88 - int((len("(your guess is higher)Close....") / 2))),"(your guess is higher)Close....")
                elif guess - random_number <= int((highest_number + 1) * 0.1):
                    print ("\n"," " * (88 - int((len("(your guess)Some higher?         (High for 0~...)") / 2))),"(your guess)Some higher?         (High for 0~",int((highest_number + 1) * 0.1),")")
                else:
                    random_choice = random.randint(1,2)
                    if random_choice == 1:
                        print ("\n"," " * (88 - int((len("Your guess is higher.") / 2))),"Your guess is higher.")
                    else:
                        print ("\n"," " * (88 - int((len("Your guess is not lower.") / 2))),"Your guess is not lower.")
            elif guess < random_number:
                if random_number - guess <= int((highest_number + 1) * 0.05 / level + level * random.randint(0,5)):
                    random_choice = random.randint(1,2)
                    if random_choice == 1:
                        print("\n"," " * (88 - int((len("It's very Close.        A bit lower.(your guess)") / 2))),"It's very Close.        A bit lower.(your guess)")
                    else:
                        print ("\n"," " * (88 - int((len("Very Close.(your guess is lower)") / 2))),"Very Close.(your guess is lower)")
                elif random_number -guess <= int((highest_number + 1) * 0.1 / level + level * random.randint(0,10)):
                    random_choice = random.randint(1,2)
                    if random_choice == 1:
                        print ("\n"," " * (88 - int((len("Bit lower...        Your guess is lower.") / 2))),"Bit lower...        Your guess is lower.")
                    else:
                        print ("\n"," " * (88 - int((len("Close....(your guess is lower)") / 2))),"Close....(your guess is lower)")
                elif random_number - guess <= int((highest_number + 1) * 0.1):
                    print ("\n"," " * (88 - int((len("Some lower?(your guess)          (Low for 0~...)") / 2))),"Some lower?(your guess)          (Low for 0~",int((highest_number + 1) * 0.1),")")
                else:
                    print ("\n"," " * (87 - int((len("It's higher.") / 2))),"It's higher.")
        chance -= 1
        if chance < 1:
            break
        if chance >= level * 3:
            print ("\n"," " * (82 - int((len("You have") / 2))),"You have",chance,"chance left.")
        else:
            print ("\n"," " * (80 - int((len("You only have") / 2))),"You only have",chance,"chance left.")
    if exit_game in ["no", "No"]:
        time.sleep(0.25)
        print ("\n"," " * (87 - int((len("Ohh,no!") / 2))),"Ohh,no!")
        time.sleep(0.5)
        print ("\n"," " * (87 - int((len("Chance over!") / 2))),"Chance over!")
    time.sleep(0.5)
    print ("\n\n<","-" * (87 - int((len("Game Start") / 2))),"Game Start","-" * (89 - int((len("Game Start") / 2))),">\n\n")
    if level > 1:
        if difficulty_mode == 4:
            print ("\nWait..")
            time.sleep(0.5)
            print (" " * (80 - int((len("You win Levels - ") / 2))),"You win Levels - ", level - 1, "in the Impossible!?\n")
            time.sleep(0.5)
            random_choice = random.randint(1,2)
            if random_choice == 1:
                print (" " * (87 - int((len("Wow!") / 2))),"Wow!\n")
            else:
                print (" " * (87 - int((len("So Good!") / 2))),"So Good!\n")
        print (" " * (87 - int((len("Your win levels is - ") / 2))),"Your win levels is - ", level, "!\n")
    time.sleep(0.5)
    print (" " * (87 - int((len("Thank you open my project!") / 2))),"Thank you open my project!\n")
    time.sleep(0.5)
    print (" " * (87 - int((len("Please rest your eyes for 10 minutes.") / 2))),"Please rest your eyes for 10 minutes.\n")
    time.sleep(0.5)
    print (" " * (87 - int((len("Bye~bye.: )") / 2))),"Bye~bye.: )")  # Bye: )
    time.sleep(3)

play_game()
