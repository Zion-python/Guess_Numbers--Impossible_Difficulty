#The file size is only about 23.1KB.😀

#I created this when I was √196 years old.🧐

#I know I didn't do a good job with this,:|
#    --but you can do it better.:)

#Share your work with your friends!;)

import random
import time

def format_score(score):
    if score < 0:
        return f"-{format_score(-score)}"
    if score >= 10_000_000:
        return f"{score:,}"
    s = f"{score:07d}"
    if s == "0000000":
        return s
    parts = []
    while s:
        parts.append(s[-3:])
        s = s[:-3]
    parts.reverse()
    return ','.join(parts)

def play_game():
    score=0
    exit_game="no"
    level=1
    chance=14
    highest_number=99
    lowest_number=0
    chance_last=chance
    while True:
        time.sleep(0.1)
        print(" "*(74-int((len("1.Easy.")/2))),"|    1.Easy.","     |    2.Normal.    |\n\n")
        time.sleep(0.05)
        print(" "*(76-int((len("3.Difficult.")/2))),"|    3.Difficult.","|    4.Impossible.|\n\n")
        time.sleep(0.05)
        print(" "*(88-int((len("Which code do you want:" )/2))),end="")
        time.sleep(0.05)
        difficulty_mode=input("Which code do you want?: ")
        if str(difficulty_mode) not in ["1","Easy","easy","2","Normal","normal","3","Difficult","difficult","4","Impossible","impossible"]:
            random_choice=random.randint(1,2)
            if random_choice==1:
                print("\n"," "*(88-int((len("Sorry,I can't understand. Please input again.")/2))),"Sorry,I can't understand. Please input again.")
            else:
                print("\n"," "*(88-int((len("???")/2))),"???")
            continue
        else:
            if difficulty_mode in ["1","Easy","easy"]:
                difficulty_mode=1
                difficulty_print="Easy"
            elif difficulty_mode in ["2","Normal","normal"]:
                difficulty_mode=2
                difficulty_print="Normal"
            elif difficulty_mode in ["3","Difficult","difficult"]:
                difficulty_mode=3
                difficulty_print="Difficult"
            elif difficulty_mode in ["4","Impossible","impossible"]:
                difficulty_mode=4
                difficulty_print="Impossible"
        break
    print("\n\n<","-"*(88-int((len("Game Start")/2))),"Game Start","-"*(88-int((len("Game Start")/2))),">\n\n"," "*(88-int((len("---------loading--------")/2))),"---------loading--------\n")
    time.sleep(0.5)
    print(" "*(89-int((len("|loading>            0%|")/2))),"|loading>            0%|\n")
    time.sleep(0.1)
    print(" "*(89-int((len("|loading..>         25%|")/2))),"|loading..>         25%|\n")
    time.sleep(0.1)
    print(" "*(89-int((len("|loading.....>      50%|")/2))),"|loading.....>      50%|\n")
    time.sleep(0.1)
    print(" "*(89-int((len("|loading.......>    75%|")/2))),"|loading.......>    75%|\n")
    time.sleep(0.1)
    print(" "*(89-int((len("|loading..........>100%|")/2))),"|loading..........>100%|\n")
    time.sleep(0.05)
    print(" "*(89-int((len("------loading over------")/2))),"------loading over------\n")
    print(" "*(88-int((len("------------------------------------Game Rules----------------------------------")/2))),"-------------------------------------Game Rules----------------------------------\n")
    time.sleep(0.05)
    print(" "*(88-int((len("|1.You need to input right number.                                              |")/2))),"|1.You need to input right number.                                              |\n")
    time.sleep(0.05)
    print(" "*(88-int((len("|2.You'd better not make any input errors.                                      |")/2))),"|2.You'd better not make any input errors.                                      |\n")
    time.sleep(0.05)
    print(" "*(88-int((len("|3.Select the Appropriate Difficulty.                                           |")/2))),"|3.Select the Appropriate Difficulty.                                           |\n")
    time.sleep(0.05)
    print(" "*(88-int((len("|4.When you change the difficulty, the score and chances will be recalculated.  |")/2))),"|4.When you change the difficulty, the score and chances will be recalculated.  |\n")
    time.sleep(0.05)
    print(" "*(88-int((len("|5.Lowest_number some time will be negative number.                             |")/2))),"|5.Lowest_number some time will be negative number.                             |\n")
    time.sleep(0.05)
    print(" "*(88-int((len("|6.Each correct guess adds points.                                              |")/2))),"|6.Each correct guess adds points.                                              |\n")
    time.sleep(0.05)
    print(" "*(88-int((len("|7.Each wrong guess deducts points.                                             |")/2))),"|7.Each wrong guess deducts points.                                             |\n")
    time.sleep(0.05)
    print(" "*(88-int((len("|8.You win when you reach one million points.                                   |")/2))),"|8.You win when you reach one million points.                                   |\n")
    time.sleep(0.05)
    print(" "*(88-int((len("------------------------------------Game Rules----------------------------------")/2))),"-------------------------------------Game Rules----------------------------------\n\n")
    time.sleep(0.05)
    print(" "*(87-int((len("Welcome to my second Python program, which I created when I was  √196  years old.")/2))),"Welcome to my second Python program, which I created when I was  √196  years old.\n\n")
    time.sleep(0.05)
    print(" "*(87-int((len("Let's see how many times you can guess correctly.")/2))),"Let's see how many times you can guess correctly.\n\n")
    time.sleep(0.05)
    print(" "*(87-int((len("The number well start from '0~99'.")/2))),"The number well start from '0~99'.\n")
    time.sleep(0.05)
    print(" "*(77-int((len("For every correct guess--")/2))),"For every correct guess--\n"," "*(112-int((len("--The (H/L) Number well change higher and lower.")/2))),"--The (H/L) Number well change higher and lower.\n\n")
    time.sleep(0.05)
    print(" "*(90-int((len("Let's start!!!")/2))),"Let's start!!!\n\n")
    time.sleep(0.05)
    print(" "*(81-int((len("If you want EXIT--")/2))),"If you want EXIT--\n"," "*(99-int((len("--Please input 'EXIT'.")/2))),"--Please input 'EXIT'.\n\n")
    time.sleep(0.05)
    print(" "*(75-int((len("And if you want Change Mode--")/2))),"And if you want Change Mode--\n"," "*(102-int((len("--Please input 'Change mode.'")/2))),"--Please input 'Change mode.'\n\n\n")
    time.sleep(0.25)
    for i in range(difficulty_mode):
        chance-=random.randint(2,3)
    random_number=random.randint(lowest_number,highest_number)
    print("\n<","-"*int(69-(len(difficulty_print))),"Mode -",difficulty_print," | Level: ",level," | Score: ",format_score(score),"-"*int(72-(len(difficulty_print))),">")
    time.sleep(0.05)
    print("\n"," "*(83-int((len("Random Number: ")/2))),"Random Number: ",lowest_number,"~",highest_number)
    time.sleep(0.05)
    print("\n"," "*(86-int((len("Chance:")/2))),"Chance: ",chance)
    while chance!=0:
        time.sleep(0.5)
        print("\n\n"," "*(88-int((len("Please set your Answer here: ")/2))),end="")
        time.sleep(0.05)
        player_guess=input("Please set your Answer here: ")
        if player_guess.lower()=="exit":
            print("\n"," "*(88-int((len("Do you want exit?: ")/2))),end="")
            exit_game=input("Do you want exit?: ")
            if exit_game.lower()=="yes":
                break
            else:
                random_choice=random.randint(1,2)
                if random_choice==1:
                    print("\n"," "*(88-int((len("Maybe you input wrong.")/2))),"Maybe you input wrong.")
                    time.sleep(0.05)
                else:
                    print("\n"," "*(88-int((len("Let's continue.")/2))),"Let's continue.")
                    time.sleep(0.05)
                exit_game="no"
                continue
        if player_guess.lower()=="change mode":
            exit_game="no"
            level=1
            chance=14
            highest_number=99
            lowest_number=0
            while True:
                print(" "*(74-int((len("1.Easy.")/2))),"|    1.Easy.","     |    2.Normal.    |\n\n")
                time.sleep(0.05)
                print(" "*(76-int((len("3.Difficult.")/2))),"|    3.Difficult.","|    4.Impossible.|\n\n")
                time.sleep(0.05)
                print(" "*(88-int((len("Which code do you want:" )/2))),end="")
                time.sleep(0.05)
                difficulty_mode=input("Which code do you want?: ")
                if difficulty_mode not in ["1","Easy","easy","2","Normal","normal","3","Difficult","difficult","4","Impossible","impossible"]:
                    random_choice=random.randint(1,2)
                    if random_choice==1:
                        print("\n"," "*(88-int((len("Sorry,I can't understand. Please input again.")/2))),"Sorry,I can't understand. Please input again.")
                        time.sleep(0.05)
                    else:
                        print("\n"," "*(88-int((len("???")/2))),"???")
                        time.sleep(0.05)
                    continue
                else:
                    if difficulty_mode in ["1","Easy","easy"]:
                        difficulty_mode=1
                        difficulty_print="Easy"
                    elif difficulty_mode in ["2","Normal","normal"]:
                        difficulty_mode=2
                        difficulty_print="Normal"
                    elif difficulty_mode in ["3","Difficult","difficult"]:
                        difficulty_mode=3
                        difficulty_print="Difficult"
                    elif difficulty_mode in ["4","Impossible","impossible"]:
                        difficulty_mode=4
                        difficulty_print="Impossible"
                break
            for i in range(difficulty_mode):
                chance-=random.randint(2,3)
            random_number=random.randint(lowest_number,highest_number)
        try:
            guess=int(player_guess)
        except ValueError:
            time.sleep(0.05)
            random_choice=random.randint(1,3)
            if random_choice==1:
                print("\n"," "*(88-int((len("Sorry-What did you say?")/2))),"Sorry-What did you say?")
            elif random_choice==2:
                print("\n"," "*(88-int((len("What's this???")/2))),"What's this???")
            else:
                print("\n"," "*(88-int((len("???")/2))),"???")
            continue
        if guess>highest_number or guess<lowest_number:
            print("\n"," "*(88-int((len("Outside the random range!!")/2))),"Outside the random range!!")
            continue
        if guess==random_number:
            random_choice=random.randint(1,3)
            if random_choice==1:
                print("\n"," "*(88-int((len("High five!👋 Your guess is Right!")/2))),"High five! Your guess is Right!")
            elif random_choice==2:
                print("\n"," "*(88-int((len("Your guess is Right!!!")/2))),"You get This answer!!!")
            else:
                print("\n"," "*(88-int((len("Celebrate For You!")/2))),"Celebrate For You!")
            print("\n\n"," "*(88-int((len("Score: ")/2))),"Score: ",format_score(score),"-->",format_score(score+100000))
            score+=100000
            level+=1
            chance_last=chance
            if difficulty_mode==1:
                highest_number=int(highest_number*1.2+5)
                lowest_number=lowest_number-random.randint(0,max(1,int(highest_number*0.02)))
                range_size=highest_number-lowest_number+1
                chance+=max(random.randint(3,5),int(range_size**0.35)+level)
            elif difficulty_mode==2:
                highest_number=int(highest_number*1.5+10)
                lowest_number=lowest_number-random.randint(0,max(1,int(highest_number*0.05)))
                range_size=highest_number-lowest_number+1
                chance+=max(random.randint(3,4),int(range_size**0.3)+level)
            elif difficulty_mode==3:
                highest_number=int(highest_number*2.0+15)
                lowest_number=lowest_number-random.randint(0,max(1,int(highest_number*0.10)))
                range_size=highest_number-lowest_number+1
                chance+=max(random.randint(2,3),int(range_size**0.25)+level//2)
            else:
                highest_number=int(highest_number*(2.5+level*0.1))
                lowest_number=lowest_number-random.randint(0,max(1,int(highest_number*0.20)))
                range_size=highest_number-lowest_number+1
                chance=max(random.randint(1,2),int(range_size**0.2)+level//3)
            time.sleep(0.25)
            print("\n\n<","-"*int(78-(len(difficulty_print))),"Mode:",difficulty_print," | Level: ",level-1," - Cleared","-"*int(72-(len(difficulty_print))),">\n")
            time.sleep(0.25)
            random_choice=random.randint(1,2)
            if random_choice==1:
                print("\n"," "*(88-int((len("Let's proceed to the next' guess....")/2))),"Let's proceed to the next' guess....")
            else:
                print("\n"," "*(87-int((len("Level Up!")/2))),"Level Up!")
            time.sleep(0.25)
            print("\n"," "*(86-int((len("Level:")/2))),"Level:",level-1,"-->",level)
            random_number=int(random.randint(lowest_number,highest_number))
            time.sleep(0.05)
            print(" "*(85-int((len("Chance:")/2))),"Chance: ",chance_last,"-->",chance)
            time.sleep(0.05)
            print("\n\n<", "-" * int(69 - (len(difficulty_print))), "Mode -", difficulty_print, " | Level: ", level," | Score: ", format_score(score), "-" * int(72 - (len(difficulty_print))), ">")
            time.sleep(0.05)
            print("\n"," "*(82-int((len("Random Number: ")/2))),"Random Number: ",lowest_number,"~",highest_number)
            time.sleep(0.05)
            print("\n"," "*(85-int((len("Chance:")/2))),"Chance: ",chance)
            continue
        else:
            time.sleep(0.1)
            if guess>random_number:
                if guess-random_number<=int((highest_number+1)*0.05/level+level*random.randint(0,5)):
                    random_choice=random.randint(1,2)
                    if random_choice==1:
                        print("\n"," "*(88-int((len("It's very Close.       (your guess)A little higher.")/2))),"It's very Close.       (your guess)A little higher.")
                    else:
                        print("\n"," "*(88-int((len("(your guess is higher)Very Close.")/2))),"(your guess is higher)Very Close.")
                    score_deduct_points=int((guess-random_number)*(100+level*random.randint(1,10)/max(1,level*10-10)))
                    time.sleep(0.05)
                    print("\n"," "*(88-int((len("Score +")/2))),"Score  +",format_score(score_deduct_points))
                    score+=score_deduct_points
                    print("\n"," "*(80-int((len("Current Score:")/2))),"Current Score:",format_score(score))
                elif guess-random_number<=int((highest_number+1)*0.1/level+level*random.randint(0,10)):
                    random_choice=random.randint(1,2)
                    if random_choice==1:
                        print("\n"," "*(88-int((len("Bit higher...        Your guess is higher.")/2))),"Bit higher...        Your guess is higher.")
                    else:
                        print("\n"," "*(88-int((len("(your guess is higher)Close....")/2))),"(your guess is higher)Close....")
                    score_deduct_points=int((guess-random_number)*(50+level*random.randint(1,10)/max(1,level*10-10)))
                    time.sleep(0.05)
                    print("\n"," "*(88-int((len("Score +")/2))),"Score  +",format_score(score_deduct_points))
                    score+=score_deduct_points
                    print("\n"," "*(80-int((len("Current Score:")/2))),"Current Score:",format_score(score))
                elif guess-random_number<=int((highest_number+1)*0.1):
                    print("\n"," "*(88-int((len("(your guess)Some higher?         (High for 0~...)")/2))),"(your guess)Some higher?         (High for 0~",int((highest_number+1)*0.1),")")
                    score_deduct_points=int((guess-random_number)*(20+level*random.randint(1,10)/max(1,level*10-10)))
                    time.sleep(0.05)
                    print("\n"," "*(88-int((len("Score +")/2))),"Score  +",format_score(score_deduct_points))
                    score+=score_deduct_points
                    print("\n"," "*(80-int((len("Current Score:")/2))),"Current Score:",format_score(score))
                else:
                    random_choice=random.randint(1,2)
                    if random_choice==1:
                        print("\n","\n"," "*(88-int((len("Your guess is higher.")/2))),"Your guess is higher.")
                    else:
                        print("\n","\n"," "*(88-int((len("Your guess is not lower.")/2))),"Your guess is not lower.")
                    score_deduct_points=int((guess-random_number)*(40+level*random.randint(1,10)/max(1,level*10-10)))
                    time.sleep(0.05)
                    print("\n"," "*(88-int((len("Score ")/2))),"Score  ",format_score(score_deduct_points))
                    score-=score_deduct_points
                    print("\n"," "*(80-int((len("Current Score:")/2))),"Current Score:",format_score(score))
            elif guess<random_number:
                if random_number-guess<=int((highest_number+1)*0.05/level+level*random.randint(0,5)):
                    random_choice=random.randint(1,2)
                    if random_choice==1:
                        print("\n"," "*(88-int((len("It's very Close.        A bit lower.(your guess)")/2))),"It's very Close.        A bit lower.(your guess)")
                    else:
                        print("\n"," "*(88-int((len("Very Close.(your guess is lower)")/2))),"Very Close.(your guess is lower)")
                    score_deduct_points=int((guess-random_number)*(100+level*random.randint(1,10)/max(1,level*10-10)))
                    time.sleep(0.05)
                    print("\n"," "*(88-int((len("Score +")/2))),"Score  +",format_score(score_deduct_points))
                    score+=score_deduct_points
                    print("\n"," "*(80-int((len("Current Score:")/2))),"Current Score:",format_score(score))
                elif random_number-guess<=int((highest_number+1)*0.1/level+level*random.randint(0,10)):
                    random_choice=random.randint(1,2)
                    if random_choice==1:
                        print("\n"," "*(88-int((len("Bit lower...        Your guess is lower.")/2))),"Bit lower...        Your guess is lower.")
                    else:
                        print("\n"," "*(88-int((len("Close....(your guess is lower)")/2))),"Close....(your guess is lower)")
                    score_deduct_points=int((guess-random_number)*(50+level*random.randint(1,10)/max(1,level*10-10)))
                    time.sleep(0.05)
                    print("\n"," "*(88-int((len("Score +")/2))),"Score  +",format_score(score_deduct_points))
                    score+=score_deduct_points
                    print("\n"," "*(80-int((len("Current Score:")/2))),"Current Score:",format_score(score))
                elif random_number-guess<=int((highest_number+1)*0.1):
                    print("\n"," "*(88-int((len("Some lower?(your guess)          (Low for 0~...)")/2))),"Some lower?(your guess)          (Low for 0~",int((highest_number+1)*0.1),")")
                    score_deduct_points=int((guess-random_number)*(20+level*random.randint(1,10)/max(1,level*10-10)))
                    time.sleep(0.05)
                    print("\n"," "*(88-int((len("Score +")/2))),"Score  +",format_score(score_deduct_points))
                    score+=score_deduct_points
                    print("\n"," "*(80-int((len("Current Score:")/2))),"Current Score:",format_score(score))
                else:
                    random_choice=random.randint(1,2)
                    if random_choice==1:
                        print("\n"," "*(88-int((len("Your guess is lower.")/2))),"Your guess is lower.")
                    else:
                        print("\n"," "*(88-int((len("Your guess is not higher.")/2))),"Your guess is not higher.")
                    score_deduct_points=int((guess-random_number)*(10+level*random.randint(1,10)/max(1,level*10-10)))
                    time.sleep(0.05)
                    print("\n"," "*(88-int((len("Score ")/2))),"Score  ",format_score(score_deduct_points))
                    score+=score_deduct_points
                    print("\n"," "*(80-int((len("Current Score:")/2))),"Current Score:",format_score(score))
        chance-=1
        time.sleep(0.1)
        if chance<1 or score<0:
            break
        if chance>=level*3:
            print("\n"," "*(88-int((len("You have  chance left")/2))),"You have: ",chance,"chance left.")
        else:
            print("\n"," "*(88-int((len("You only have  chance left")/2))),"You only have",chance,"chance left.")
        if 1000000-score>500000:
            print("\n"," " * (84 - int((len("You are points away from winning.") / 2))),"You are",1000000-score,"points away from winning.")
        else:
            print("\n\n"," " * (84 - int((len("You are only points away from winning.") / 2))),"You are only",1000000-score,"points away from winning.")
    time.sleep(0.1)
    if score>=1000000:
        print("\n"," " * (81 - int((len("You successfully reached 1,000,000 points and you win!") / 2))),"You successfully reached 1,000,000 points and you win!")
    elif score>=0:
        print("\n"," " * (81 - int((len("Oh, so close! You almost made it to 1,000,000 points.") / 2))),"Oh, so close! You almost made it to 1,000,000 points.")
        time.sleep(0.1)
        print("\n"," " * (88 - int((len("Your final score is: ") / 2))),"Your final score is: ",format_score(score))
    else:
        time.sleep(0.25)
        print("\n"," "*(87-int((len("Ohh,no!")/2))),"Ohh,no!")
        time.sleep(0.25)
        print("\n"," "*(87-int((len("Your score is below 0!")/2))),"Your score is below 0!")
    if chance<1:
        time.sleep(0.25)
        print("\n"," "*(87-int((len("Ohh,no!")/2))),"Ohh,no!")
        time.sleep(0.25)
        print("\n"," "*(87-int((len("Chance over!")/2))),"Chance over!")
    time.sleep(0.25)
    print("\n\n<","-"*(87-int((len("Game Over")/2))),"Game Start","-"*(89-int((len("Game Over")/2))),">\n\n")
    if level>1:
        if difficulty_mode==4:
            print("\nWait..")
            time.sleep(0.3)
            print(" "*(80-int((len("You win Levels - ")/2))),"You win Levels - ",level-1,"in the Impossible!?\n")
            time.sleep(0.1)
            random_choice=random.randint(1,2)
            if random_choice==1:
                print(" "*(87-int((len("Wow!")/2))),"Wow!\n")
            else:
                print(" "*(87-int((len("So Good!")/2))),"So Good!\n")
        time.sleep(0.05)
        print(" "*(87-int((len("Your win levels is - ")/2))),"Your win levels is - ",level,"!\n")
    time.sleep(0.1)
    print(" "*(87-int((len("Thank you open my project!")/2))),"Thank you open my project!\n")
    time.sleep(0.1)
    print(" "*(87-int((len("Please rest your eyes for 10 minutes.")/2))),"Please rest your eyes for 10 minutes.\n")
    time.sleep(0.1)
    print(" "*(87-int((len("Bye~bye.:)")/2))),"Bye~bye.:)")#Bye:)
    time.sleep(3)

play_game()
