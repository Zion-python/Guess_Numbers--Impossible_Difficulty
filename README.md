#Project Description
#This is a number-guessing game featuring a system of progressively escalating difficulty.
#I wrote the original version when I was 14 years old (√196 = 14).
#The game challenges players to guess a random number situated within an ever-expanding numerical range.
#With every correct guess, your level increases, the numerical range expands (sometimes even extending into negative numbers), and your remaining #umber of attempts is dynamically adjusted.

#I. The game features four difficulty modes:

#1. Easy
#2. Normal
#3. Hard
#4. Impossible

#Can you survive the "Impossible" mode?

#II. Core Features:
#Dynamic Difficulty — The higher the difficulty level, the faster the numerical range expands.

#Level-based Attempt Recalculation — Your remaining attempts are recalculated at every level (based on the size of the current numerical range and #your current level).

#Proximity Hints — The game provides feedback indicating how close your guess is to the target number—whether it is extremely close, slightly too #high/low, or far off.

#Random Encouraging Messages/Fun Trivia

#Loading Animations and Clear Game Rules

#Type "exit" or "Exit" at any time to quit the game.

#III. How to Run:

#1. Ensure you have Python 3.6+ and PyCharm installed.
#2. Create a new text file and paste the code into it.
#3. Change the file extension to `.py`.
#4. Open the file using PyCharm.

#IV. Playing the Game:

#Follow the on-screen prompts to select a difficulty level, then start guessing the number!

#Detailed Difficulty Mode Breakdown
#｜Mode        |  Range Growth Factor        |  Lower Bound Reduction        |  Number of Chances Increases
#｜Easy        |   ×1.2 + 5                  |      slow,random              |        Moderate, slow
#｜Normal      |   ×1.5 + 10                 |        Gentle                 |            Moderate
#｜Hard        |   ×2 + 15                   |        Rapid                  |        Relatively fast
#｜Impossible  |   ×(2.5 + Level × 0.1)      |        Swift                  |             fast
#Note: "Attempts" (remaining chances) are recalculated at every level based on the current numerical range size and the current level. At higher #difficulty levels, although the numerical range expands exponentially, the number of attempts granted to you decreases correspondingly. V. Future #Improvements (Concepts)
#Run in graphical mode
#Add more features

#VI. Acknowledgments
#The original concept and code for this project were created by me when I was "√196 years old."
#Today, with the assistance of the open-source community, this project continues to be maintained and improved.
#Thanks to DeepSeek for its rigorous review and suggestions (80% or more of which were subsequently edited by me).

#VII. Modification Permissions
#Permission is hereby granted to anyone to modify this program and to adapt it into their own original work.
