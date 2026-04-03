# Guess Numbers: Impossible Difficulty

> The file size is only about 11KB. 😀  
> The code is quite verbose (I'm so sorry 😬) – it wastes space and unnecessary computational overhead. 😓  
> I do not possess extensive coding expertise.  
> **The program is fully functional (tested). 😉**

---

## Project Description

This is a number‑guessing game with **progressively escalating difficulty**.  
I wrote the original version when I was 14 years old (√196 = 14).

You guess a random number inside an **ever‑expanding numerical range**.  
Each correct guess increases your **level**, expands the range (sometimes into negative numbers), and **recalculates your remaining chances**.

> ⚠️ **Important**: The number of chances increases **slowly** – even on higher levels it is only theoretically sufficient.

---

## I. Difficulty Modes

1. Easy  
2. Normal  
3. Hard  
4. Impossible

Can you survive the **Impossible** mode?

---

## II. Core Features

- **Dynamic Difficulty** – Higher difficulty makes the range expand much faster.  
- **Level‑based Chance Recalculation** – Remaining attempts are recomputed each level based on current range size and level.  
- **Proximity Hints** – Tells you if your guess is very close, slightly high/low, or far off.  
- **Random Encouraging Messages & Fun Trivia**  
- **Loading Animation & Clear Game Rules**  
- Type `exit` or `Exit` at any time to quit.

---

## III. How to Run (No PyCharm Needed)

You only need **Python 3.6 or newer** – no extra IDE or packages.

### 1. Install Python 3.6 from the official website

- Go to [Python 3.6 archive](https://www.python.org/downloads/release/python-360/)  
- Download the installer for your OS:  
  - **Windows 64‑bit**: `Windows x86-64 executable installer`  
  - **Windows 32‑bit**: `Windows x86 executable installer`  
  - **macOS**: `macOS 64-bit installer`  
  - **Linux**: use `sudo apt install python3.6` (or your distro's package manager)  
- Run the installer – **IMPORTANT**: check **“Add Python 3.6 to PATH”**  
- Click `Install Now`

> ✅ `import time` and `import random` are **built‑in modules** – they work immediately after Python is installed.

### 2. Verify installation

Open a terminal (CMD, PowerShell, or bash) and type:

    python --version

You should see `Python 3.6.x` (or higher).

### 3. Run the game

- Save the game code as `guess_numbers.py`  
- Open a terminal in that folder  
- Run:

    python guess_numbers.py

That's it – enjoy!

---

## IV. Playing the Game

Follow the on‑screen prompts to select a difficulty level, then start guessing.

### Difficulty Mode Breakdown

| Mode       | Range Growth Factor        | Lower Bound Reduction | Chances Increase Rate |
|------------|----------------------------|----------------------|------------------------|
| Easy       | ×1.2 + 5                   | Slow, random         | Small & fast           |
| Normal     | ×1.5 + 10                  | Gentle               | Normal                 |
| Hard       | ×2 + 15                    | Rapid                | Very slow              |
| Impossible | ×(2.5 + Level × 0.1)       | Swift                | Extremely slow         |

> 📉 **Note**: The number of chances you get **does not increase quickly** – especially on Hard and Impossible modes, the growth is deliberately slow. Each level recalculates chances based on current range size and level; higher difficulties give you fewer attempts relative to the explosion of the number range.

---

## V. Health & Sharing Tips

- 👀 **Rest your eyes** – after playing, look away from the screen for a few minutes.  
- ⏰ **Take breaks** – don't play for too long in one sitting.  
- 📢 **Share with friends** – challenge them to beat your level!  
- 🔧 **Modify freely** – you are allowed to change the code and turn it into your own original work.

---

## VI. Future Improvements (Ideas)

- Graphical mode (GUI)  
- Save high scores across sessions  
- More balanced chance formulas  
- Cleaner code structure

---

## VII. Acknowledgments

The original concept and code were created by me when I was **“√196 years old”** (14).  

Today, with the help of the open‑source community, this project continues to be maintained and improved.  
Special thanks to **DeepSeek** for its rigorous review and suggestions – more than 80% of which were subsequently edited by me (so any remaining mistakes are entirely my own 😅).

---

## VIII. Modification Permissions

**Permission is hereby granted to anyone to modify this program and to adapt it into their own original work.**  
You are encouraged to share your improved version with your friends!

---

*Made with by a 14‑year‑old. Keep guessing, keep learning.


# This article was largely compiled and optimized by deepseek from the original version (which I wrote) and generated.
