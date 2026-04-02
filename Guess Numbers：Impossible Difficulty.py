#I created this when I was √196.
#I know I didn't do a good job with this,🙁
#   but you can make it better.😁
#Share your work with your friends!

import random
import time

def play_game():
    should_exit = "no"
    chance = 10
    level = 1
    highest_number = 99
    lowest_number = 0
    while True:
        difficulty_mode = input("Which code do you want?\n1.Easy;\n2.Normal;\n3.Difficult;\n4.Impossible.\n: ")
        if difficulty_mode not in ["1","Easy","easy","2","Normal","normal","3","Difficult","difficult","4","Impossible","impossible"]:
            print (random.choice(["Sorry,I can't understand.😓\nPlease input again.","???😦"]))
        else:
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
           "\n                                  If you want exit--\n                                  --Please input 'exit' or 'Exit'")
    time.sleep(0.25)
    random_number = random.randint(lowest_number, highest_number)
    print ("\n                                        Level: 1","\n                                Random Number: ",lowest_number,"~",highest_number)
    while chance != 0:
        time.sleep(0.5)
        player_guess = input('\n\n                              Please set your Answer here: ')
        if player_guess in ["exit","Exit"]:
            should_exit = input("\n           Do you want exit?: ")
            if should_exit in ["yes","Yes"]:
                break
            else:
                print (random.choice(["                      Maybe you input wrong.","You don't Quit?  So...    Let's continue!"]))
                should_exit = "no"
                continue
        try:
            guess = int(player_guess)
        except ValueError:
            print(random.choice(["                                  Sorry-What did you say?", "                            I can't understand..    Please say again.", "                                    ???    What's this?"]))
            continue
        if guess > highest_number or guess < lowest_number:
            print ("                                  Outside the random range!!")
            continue
        if guess == random_number:
            print (random.choice(["                              High five!👋 You guessed Right!","                                      You guessed Right.","                                   Celebrate For You!"]))
            level += 1
            if difficulty_mode in ["1","Easy","easy"]:
                highest_number = highest_number * 1.2 + 5
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.1)))
                chance = max(random.choice([5, 8]) + level,int((highest_number - lowest_number + 1) ** 0.4) + level // 2)
            elif difficulty_mode in ["2","Normal","normal"]:
                highest_number = highest_number * 1.5 + 10
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.2)))
                chance = max(random.choice([4, 6]) * level, int((highest_number - lowest_number + 1) ** 0.3) + level)
            elif difficulty_mode in ["3","Difficult","difficult"]:
                highest_number = highest_number * 2 + 15
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.3)))
                chance = max(random.choice([3, 5]) * level,int((highest_number - lowest_number + 1) ** 0.25) + level // 2)
            else :
                highest_number = int(highest_number * (2.5 + level * 0.1))
                lowest_number = lowest_number - random.randint(0, max(1, int(highest_number * 0.5)))
                chance = max(random.choice([3, 4]) * level,int((highest_number - lowest_number + 1) ** 0.2) + level // 3)
            time.sleep(0.25)
            print (random.choice(["\n                          Let's proceed to the next' guess....","\n                                       Level Up!"]))
            random_number = int(random.randint(lowest_number, highest_number))
            time.sleep(0.25)
            print ("\n                                        Level: 1","\n                                Random Number: ",lowest_number,"~",highest_number)
            continue
        else:
            if guess > random_number:
                if guess - random_number <= int((highest_number + 1) * 0.05 / level + level * random.randint(0,5)):
                    print (random.choice(["\n                It's very Close.       (you guess)A little higher.","\n                             (you guess)Very Close."]))
                elif guess - random_number <= int((highest_number + 1) * 0.1 / level + level * random.randint(0,10)):
                    print (random.choice(["\n                              Bit higher...        You guess Higher.","                                            Close...."]))
                elif guess - random_number <= int((highest_number + 1) * 0.1):
                    print ("\n                         (you guess)Some higher?         (High for 0~",int((highest_number + 1) * 0.1),")")
                else:
                    print(random.choice(["\n                                    You guess higher.","\n                                    You guess not lower."]))
            elif guess < random_number:
                if random_number - guess <= int((highest_number + 1) * 0.05 / level + level * random.randint(0,5)):
                    print(random.choice(["\n                         It's very Close.        A bit lower.(you guess)","\n                                   Very Close.(you guess)"]))
                elif random_number -guess <= int((highest_number + 1) * 0.1 / level + level * random.randint(0,10)):
                    print (random.choice(["\nBit lower...        You guess lower.","Close...."]))
                elif random_number - guess <= int((highest_number + 1) * 0.1):
                    print ("\n              Some lower?(you guess)          (Low for 0~",int((highest_number + 1) * 0.1),")")
                else:
                    print ("\n                                       It's higher.")
        chance -= 1
        if chance < 1:
            break
        if chance >= level * 3:
            print ("\n                                    You have",chance,"chance.")
        else:
            print ("\n                                   You only have",chance,"chance.")
    if should_exit in ["no", "No"]:
        time.sleep(0.25)
        print("                                          \nOhh,no!")
        time.sleep(0.5)
        print("\n                                       Chance over!")
    time.sleep(0.5)
    print("\n\n<----------------------------------------Game Over---------------------------------------->\n\n")
    if difficulty_mode in ["4","Impossible","impossible"]:
        if level != 1:
            print("\nWait..")
            time.sleep(0.5)
            print("You win Levels - ", level, "in the Impossible!?")
            time.sleep(0.5)
            print(random.choice(["Wow!", "So Good!"]))
    if level > 1:
        print('Your win levels is - ', level, "!")
    time.sleep(0.5)
    print('Thank you open my project!')
    time.sleep(0.5)
    print('Please rest your eyes for 10 minutes.')
    time.sleep(0.5)
    print('Bye~bye.:)')  # Bye:)
    time.sleep(1)

play_game()