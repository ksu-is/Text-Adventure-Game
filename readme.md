
![Figure 3: Flow chart representing user interactions.](https://raw.githubusercontent.com/Kyle-L/Text-Adventure-Tutorial/master/docs/images/game-flow.png)

Since we have an idea of how the game will flow, how do we actually build this?
# Text Adventure Game 
By Gabriela Alvarez

## 📖 Overview
This is a simple text-based adventure game where players explore a small world, collect items, and try to escape with treasure. The game is played entirely through typed commands in the console.

The player begins in a forest and can travel to different connected locations, discover items, and use them to win the game.

---

## 🎮 How to Play

### **Available Commands**
- `go <direction>` — Move to another room (north, south, east, west)  
- `get <item>` — Pick up an item you find  
- `use <item>` — Use an item in your inventory  
- `exit` — Quit the game  

Example commands:


go north
get boat
use boat


## 🌍 Game Map

 River
   |
Forest --- Cave

- Forest — Starting area  
- River — Contains a boat  
- Cave — Contains gold

## 🎯 Objective / How to Win
You can win in two ways:
1. Use the boat at the River: Pick up the boat, go to the River, and type `use boat` to escape and win.
2. Collect both the gold and the boat: If your inventory contains both items, the game automatically ends with a win.

## 🧩 Features
- Movement between rooms  
- Status display  
- Inventory system  
- Item pickup and item usage  
- Multiple win conditions  
- Error handling for invalid commands

## ▶️ How to Run the Game
### Option 1: Run in a terminal
1. Make sure you have Python installed  
2. Open a terminal  
3. Navigate to the folder containing `game.py`  
4. Run:


python game.py


### Option 2: Run in an IDE
You can also run this game in tools like VS Code, PyCharm, or IDLE.

## 🛠️ Code Structure


Text-Adventure-Game/
├── game.py
└── README.md

## ✨ Future Improvements I will be adding
- Add more rooms  
- Add enemies or traps  
- Add puzzles  
- Add health system  
- Add save/load feature  
- Add title screen

## 📬 Author
**Gabriela Alvarez**  
Text Adventure Game Project  
Kennesaw State University — IS Class
