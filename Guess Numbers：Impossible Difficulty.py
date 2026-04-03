#The file size is only about 12KB.😀

#I created this when I was √196 years old.🧐

#I know I didn't do a good job with this,:|
#    --but you can do it better.:)

#Share your work with your friends!;)

import random
import time

def play_game():
    exit_game = "no"
    level = 1
    highest_number = 99
    lowest_number = 0
    while True:
        difficulty_mode = input("Which code do you want?\n1.Easy;\n2.Normal;\n3.Difficult;\n4.Impossible.\n: ")
        if difficulty_mode not in ["1","Easy","easy","2","Normal","normal","3","Difficult","difficult","4","Impossible","impossible"]:
            print (random.choice(["Sorry,I can't understand.😓\nPlease input again.","???😦"]))
        else:
            if difficulty_mode in ["Easy", "easy"]:
                difficulty_mode = "1"
            elif difficulty_mode in ["Normal", "normal"]:
                difficulty_mode = "2"
            elif difficulty_mode in ["Difficult","difficult"]:
                difficulty_mode = "3"
            elif difficulty_mode in ["Impossible","impossible"]:
                difficulty_mode = "4"
        break
    print ("\n\n<----------------------------------------Game Start---------------------------------------->\n\n                                  ---------loading--------")
    time.sleep(0.5)
    print ("                                  |loading>            0%|")
    time.sleep(0.1)
    print ("                                  |loading..>         25%|")
    time.sleep(0.1)
    print ("                                  |loading.....>      50%|")
    time.sleep(0.1)
    print ("                                  |loading.......>    75%|")
    time.sleep(0.1)
    print ("                                  |loading..........>100%|")
    print ("                                  ------loading over------")
    time.sleep(0.1)
    print ("\n                    ---------------------Game Rules--------------------"
           "\n                    |1.You need to input right number;                |"
           "\n                    |2.You'd better not make any input errors;        |"
           "\n                    |3.Select the Appropriate Difficulty.             |"
           "\n                    |4.Lowest_number some time will be negative number|"
           "\n                    ---------------------Game Rules--------------------"
           "\n\n       Welcome to my second Python program, which I created when I was  14  years old."
           "\n\n                   Let's see how many times you can guess correctly."
           "\n                              The number well start from '0~99(n)"
           "\n\n                              For every correct guess--\n                              n increases by one digit."
           "\n\n                                   Let's start!!!!)"
           "\n\n                              If you want EXIT--\n                                             --Please input 'EXIT'"
           "\n\n                  And if you want Change Mode--\n                                             --Please input 'Change mode'\n")
    time.sleep(0.25)
    chance = 14 - random.randint(2,3) * int(difficulty_mode)
    random_number = random.randint(lowest_number,highest_number)
    print ("\n\n<-----------------------------------Mode:",difficulty_mode," | Level:",level,"----------------------------------->","\n                                Random Number: ",lowest_number,"~",highest_number,"\n                                       Chance:",chance)
    while chance != 0:
        time.sleep(0.5)
        player_guess = input('\n\n                              Please set your Answer here: ')
        if player_guess.lower() == "exit":
            exit_game = input("\n           Do you want exit?: ")
            if exit_game.lower() == "yes":
                break
            else:
                print (random.choice(["                      Maybe you input wrong.","You don't Quit?  So...    Let's continue!"]))
                exit_game = "no"
                continue
        if player_guess.lower() == "change mode":
            level = 1
            highest_number = 99
            lowest_number = 0
            while True:
                difficulty_mode = input("Which code do you want?\n1.Easy;\n2.Normal;\n3.Difficult;\n4.Impossible.\n: ")
                if difficulty_mode not in ["1", "Easy", "easy", "2", "Normal", "normal", "3", "Difficult", "difficult",
                                           "4", "Impossible", "impossible"]:
                    print(random.choice(["Sorry,I can't understand.😓\nPlease input again.", "???😦"]))
                else:
                    if difficulty_mode in ["Easy", "easy"]:
                        difficulty_mode = "1"
                    elif difficulty_mode in ["Normal", "normal"]:
                        difficulty_mode = "2"
                    elif difficulty_mode in ["Difficult", "difficult"]:
                        difficulty_mode = "3"
                    elif difficulty_mode in ["Impossible", "impossible"]:
                        difficulty_mode = "4"
                break
            chance = 14 - random.randint(2, 3) * int(difficulty_mode)
            random_number = random.randint(highest_number,lowest_number + 1)
            player_guess = ""
            continue

        try:
            guess = int(player_guess)
        except ValueError:
            print(random.choice(["\n                                  Sorry-What did you say?","\n                            I can't understand..    Please say again.","\n                                    ???    What's this?"]))
            continue
        if guess > highest_number or guess < lowest_number:
            print ("\n                                  Outside the random range!!")
            continue
        if guess == random_number:
            print (random.choice(["\n                              High five!👋 You guessed Right!","                                      You guessed Right.","                                   Celebrate For You!"]))
            level += 1
            if difficulty_mode == "1":
                highest_number = int(highest_number * 1.2 + 5)
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.02)))
                range_size = highest_number - lowest_number + 1
                chance = max(random.randint(6,8), int(range_size ** 0.35) + level)

            elif difficulty_mode == "2":
                highest_number = int(highest_number * 1.5 + 10)
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.05)))
                range_size = highest_number - lowest_number + 1
                chance = max(random.randint(5,7), int(range_size ** 0.3) + level)

            elif difficulty_mode == "3":
                highest_number = int(highest_number * 2.0 + 15)
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.10)))
                range_size = highest_number - lowest_number + 1
                chance = max(random.randint(4,6), int(range_size ** 0.25) + level // 2)

            else:
                highest_number = int(highest_number * (2.5 + level * 0.1))
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.20)))
                range_size = highest_number - lowest_number + 1
                chance = max(random.randint(3,6), int(range_size ** 0.2) + level // 3)

            time.sleep(0.25)
            print ("\n<-----------------------------------Mode:",difficulty_mode," | Level:",level - 1," - Cleared------------------------->\n")
            time.sleep(0.25)
            print (random.choice(["\n                          Let's proceed to the next' guess....","\n                                        Level Up!"]))
            time.sleep(0.25)
            print ("\n                                        Level: ",level - 1,"-->",level)
            random_number = int(random.randint(lowest_number, highest_number))
            time.sleep(0.5)
            print ("\n\n<-----------------------------------Mode:",difficulty_mode," | Level:",level,"----------------------------------->""\n                                Random Number: ",lowest_number,"~",highest_number,"\n                                       Chance:",chance)
            continue
        else:
            if guess > random_number:
                if guess - random_number <= int((highest_number + 1) * 0.05 / level + level * random.randint(0,5)):
                    print (random.choice(["\n                         It's very Close.       (you guess)A little higher.","\n                             (you guess higher)Very Close."]))
                elif guess - random_number <= int((highest_number + 1) * 0.1 / level + level * random.randint(0,10)):
                    print (random.choice(["\n                              Bit higher...        You guess higher.","\n                                       (you guess higher)Close...."]))
                elif guess - random_number <= int((highest_number + 1) * 0.1):
                    print ("\n                         (you guess)Some higher?         (High for 0~",int((highest_number + 1) * 0.1),")")
                else:
                    print(random.choice(["\n                                    You guess higher.","\n                                    You guess not lower."]))
            elif guess < random_number:
                if random_number - guess <= int((highest_number + 1) * 0.05 / level + level * random.randint(0,5)):
                    print(random.choice(["\n                         It's very Close.        A bit lower.(you guess)","\n                                Very Close.(you guess lower)"]))
                elif random_number -guess <= int((highest_number + 1) * 0.1 / level + level * random.randint(0,10)):
                    print (random.choice(["\n                             Bit lower...        You guess lower.","\n                                     Close....(you gues lower)"]))
                elif random_number - guess <= int((highest_number + 1) * 0.1):
                    print ("\n              Some lower?(you guess)          (Low for 0~",int((highest_number + 1) * 0.1),")")
                else:
                    print ("\n                                       It's higher.")
        chance -= 1
        if chance < 1:
            break
        if chance >= level * 3:
            print ("\n                                    You have",chance,"chance left.")
        else:
            print ("\n                                   You only have",chance,"chance left.")
    if exit_game in ["no", "No"]:
        time.sleep(0.25)
        print("\n                                          Ohh,no!")
        time.sleep(0.5)
        print("\n                                       Chance over!")
    time.sleep(0.5)
    print("\n\n<----------------------------------------Game Over---------------------------------------->\n\n")
    if difficulty_mode in ["4","Impossible","impossible"]:
        if level > 1:
            print("\nWait..")
            time.sleep(0.5)
            print("You win Levels - ", level - 1, "in the Impossible!?")
            time.sleep(0.5)
            print(random.choice(["Wow!", "So Good!"]))
    if level > 1:
        print('Your win levels is - ', level, "!")
    time.sleep(0.5)
    print('Thank you open my project!')
    time.sleep(0.5)
    print('Please rest your eyes for 10 minutes.')
    time.sleep(0.5)
    print('Bye~bye.: )')  # Bye: )
    time.sleep(3)

play_game()
