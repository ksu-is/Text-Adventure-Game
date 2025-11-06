
![Figure 3: Flow chart representing user interactions.](https://raw.githubusercontent.com/Kyle-L/Text-Adventure-Tutorial/master/docs/images/game-flow.png)

Since we have an idea of how the game will flow, how do we actually build this?
# Text Adventure Game by Gabriela Alvarez

#### Variables
A simple interactive Python adventure where you explore a **dark forest**, find treasures, and try to escape by boat!

_What is a variable and why do we need it?_
---

To build our game, we need to cover a few core concepts. One core concept we need to make our game is a **variable**. If you have ever taken a math class, you might already have an idea of what a variable is. For instance, in algebra you might recall seeing something like `x = 6` and `2 + x = ??`. From this, we can see that `2 + x = ??` evaluates to `2 + 6 = 8` by replacing the `x` in `2 + x = ??` with `6`.
## 🌲 Overview

Variables in programming are very similar to this. A variable is a thing that you can use to store information and retrieve it to use later. You can essentially think of them as boxes that you can put data into and take data out of later.
You wake up surrounded by tall trees and moonlight.  
Paths lead deeper into the forest, toward the sound of rushing water, or into a damp cave that glitters faintly in the dark.  
Your goal: **find the treasure and escape!**

**Figure 4: Variables are kind of like storage boxes in programming.**  
![Figure 4: Variables are kind of like storage boxes in programming.](https://raw.githubusercontent.com/Kyle-L/Text-Adventure-Tutorial/master/docs/images/variable.png)
---

To demonstrate this further, we will modify the code we wrote in [Writing Your First Python Code](#writing-your-first-python-code).
## 🕹️ How to Play

###### Step 1
Insert the line `sentence = "This is a groovy sentence!"` above `type("Hello world")`.
This line is indicating that we would like to store `"This is a groovy sentence!"` in the variable `sentence`.
###### Step 2
Replace `"Hello world!"` with `sentence`.
Your code should look like the following:
```python
from story_engine import *
#### TYPE YOUR CODE BELOW HERE ####
sentence = "This is a groovy sentence!"
type(sentence)
```
###### Step 3
Click `Run`!
Your terminal will now display the following:
```
> python3 main.py
This is a groovy sentence!>
```
Congratulations, you have now learned how to use a variable!
#### Functions
_What is a function and why do we need it?_
Another core concept within programming we need to discuss is the concept of a **function**. At its core, a function is a set of instructions. Think of this kind of like a recipe. It a step-by-step instruction that a programmer gives to a computer. Functions typically look like `[function name]([input])` where `[function name]` is some name to indentify the function and `[input]` is a value we can give the function to do something with (This can be a variable). For instance, say we were writing a function to tell a computer to add flour to a recipe, it might look like `add(flour)`.
Thus, you can think of a function as something that takes an input and responds with an output.
**Figure 5: A function takes an input and responds with an output.**  
![Figure 5: A function takes an input and responds with an output.](https://raw.githubusercontent.com/Kyle-L/Text-Adventure-Tutorial/master/docs/images/function.png)
An example of a function you already know is `type(text)`. As you can probably guess, `type(text)` tells the computer to type `text` into the terminal.
For our game, you will not need to create any functions of your own. I have already provided some that will make creating a game easier.
- _Note: If you are curious, you can look at all of those functions in the `story_engine.py` file._
Though we will not be making any functions, we will be using one primary function to make our adventure game which is `story_flow(story)`. `story_flow(story)` is a function that will take an adventure game's `story` as input and go through the exact same steps described in [How Will the User Interact with the Game?](#how-will-the-user-interact-with-the-game).
1. It will start the user at page 1.
2. The user will read the page.
3. At the end of the page, they are faced with a choice.
4. Based on the choice, they navigate to a new page number corresponding with the choice.
5. Repeat steps 2 through 4 until they reach the end of the adventure.
However, how exactly will we format all these pages and choices in code?
#### How do you Format an Adventure Game's Story?
_How can we represent the story of an adventure game in code?_
To give `story_flow(story)` a `story`, we need a way to format our adventure's story in code. To do that we will create a variable called `story` that will be used to store our entire adventure's story in.
The `story` variable's template will look somewhat like the following:
```python
story = {
    #### START YOUR STORY HERE ####
    [page number]: {
        'Text': [
            "[line of text]",
            "[line of text]",
            "[line of text]",
        ],
        'Options': [
            ("[option]", [option page number]),
            ("[option]", [option page number]),
            ("[option]", [option page number]),
        ]
    },
    .
    .
    .
    #### END YOUR STORY HERE ####
}
```
At first glance, this might look complex, but if we take a moment to break everything down you will see how it is like how a _Choose Your Own Adventure_ book is formatted. Everything surround by brackets [ ] is a value you need to fill in to create a story.
- [page number]
  - This represents the page of the book as an integer value such as 1, 2, or 3.
  - There can be as many pages as you want.
- [line of text]
  - Represents a single line of text on a page.
  - There can be as many lines of text as you want.
  - _Note: Should be surrounded by quotation marks._
- [option]
  - Represents a decision that can be made.
  - There can be as many decisions as you want.
  - _Note: Should be surrounded by quotation marks._
- [option page number]
  - Represents the page that will be switched to when this decision is chosen.
- _Note: the three vertical dots just represent more pages._
After we fill in all those values, our story will look something like the following:
- _Note: only pages 1 and 10 are displayed. All the other pages will follow the same format_
```python
story = {
    #### START YOUR STORY HERE ####
    1: {
        'Text': [
            "This text will display before the user can make a choice.",
            "You can have as many lines of text as you want.",
            "Once it is finished typing, the user can then make a choice."
        ],
        'Options': [
            ("This is the first choice. It will take the user to page 2.", 2),
            ("This is the second choice. It will take the user to page 3.", 3),
        ]
    },
    .
    .
    .
    10: {
        'Text': [
            "This is the last page of the story.",
            "There is no decision that can be made from here.",
        ],
        'Options': [
        ]
    },
    #### END YOUR STORY HERE ####
}
```
In this example, the reader will start on page 1 where there are three lines of text. So, when a reader starts, they will first see those three lines on their screen like:
```
This text will display before the user can make a choice.
You can have as many lines of text as you want.
Once it is finished typing, the user can then make a choice.
```
Once those three lines are displayed, they will be followed by the two options. A reader can decide what option they would like to go with by typing in a number that corresponds to the options. A reader's screen at this point will look like the following:
```
This text will display before the user can make a choice.
You can have as many lines of text as you want.
Once it is finished typing, the user can then make a choice.
0.) This is the first choice. It will take the user to page 2.
1.) This is the second choice. It will take the user to page 3.
Please choose an option:
```
From there, depending on what choice the reader makes, they will go to either page 2 or 3. This process will continue until eventually the reader ends up on page 10.
On page 10, there are no decisions that can be made as there a no option lines. Thus, the story ends after the two lines of text are displayed.
If you do not 100% understand how this works, do not worry as we will be coming back to this concept in the next section.
## Putting it All Together
_Time to make a text-based adventure game!_
We now have all the knowledge that we need to get started building our very own text-based adventure game!
#### Map Your Adventure Game's Story Out
_Before diving into code, map out the story you want to make._
You might find it beneficial to map out your story first before turning it into code.
For the following set of instructions, I have gone ahead and created a flow chart that will represent the story of a simple adventure game in which a person wakes up and goes back to bed.
**Figure 6: A flow chart of the game we will be making.**  
![Figure 6: A flow chart of the game we will be making.](https://raw.githubusercontent.com/Kyle-L/Text-Adventure-Tutorial/master/docs/images/example-tree.png)
To get the hang of things, follow along and make this story in code; then, once you are comfortable making a story, you can come back, draw out your own story, and follow steps 1 through 8 below again with your own story.
#### How to Start an Adventure Game
###### Step 1
Delete all code below `#### TYPE YOUR CODE BELOW HERE ####`
###### Step 2
Copy the template from [How do you Format an Adventure Game?](#how-do-you-format-an-adventure-game) to start creating our own story so that our code looks like the following:
```python
from story_engine import *
#### TYPE YOUR CODE BELOW HERE ####
story = {
    #### START YOUR STORY HERE ####
    [page number]: {
        'Text': [
            "[line of text]",
            "[line of text]",
            "[line of text]",
        ],
        'Options': [
            ("[option]", [option page number]),
            ("[option]", [option page number]),
            ("[option]", [option page number]),
        ]
    },
    #### END YOUR STORY HERE ####
}
```
###### Step 3
Using the template, write your first page by replacing everything surrounded by brackets [ ] with the appriopriate information from our story's first page.
```python
from story_engine import *
#### TYPE YOUR CODE BELOW HERE ####
story = {
    #### START YOUR STORY HERE ####
    1: {
        'Text': [
            "It's a dark and stormy night.",
            "Abruptly, you wake to the sound of thunder shaking your room.",
            "Peeking out from under your blankets, you take a moment to consider what to do.",
        ],
        'Options': [
            ("Get out of bed.", 2),
            ("Go back to sleep.", 4),
        ]
    },
    #### END YOUR STORY HERE ####
}
```
#### How to Branch an Adventure Game’s Story.
###### Step 4
Now that we have our first page, we can start adding more pages to our story.
To add more pages, we can simply insert a new line above `#### END YOUR STORY HERE ####` and copy and paste the following code from the template from above.
```python
[page number]: {
    'Text': [
        "[line of text]",
        "[line of text]",
        "[line of text]",
    ],
    'Options': [
        ("[option]", [option page number]),
        ("[option]", [option page number]),
        ("[option]", [option page number]),
    ]
},
```
Thus, our code should look similar to the following:
```python
from story_engine import *
#### TYPE YOUR CODE BELOW HERE ####
story = {
    #### START YOUR STORY HERE ####
    1: {
        'Text': [
            "It's a dark and stormy night.",
            "Abruptly, you wake to the sound of thunder shaking your room.",
            "Peeking out from under your blankets, you take a moment to consider what to do.",
        ],
        'Options': [
            ("Get out of bed.", 2),
            ("Go back to sleep.", 4),
        ]
    },
    [page number]: {
        'Text': [
            "[line of text]",
            "[line of text]",
            "[line of text]",
        ],
        'Options': [
            ("[option]", [option page number]),
            ("[option]", [option page number]),
            ("[option]", [option page number]),
        ]
    },
    #### END YOUR STORY HERE ####
}
```
###### Step 5
Fill in the information for page 2 so that our code looks like:
```python
from story_engine import *
#### TYPE YOUR CODE BELOW HERE ####
story = {
    #### START YOUR STORY HERE ####
    1: {
        'Text': [
            "It's a dark and stormy night.",
            "Abruptly, you wake to the sound of thunder shaking your room.",
            "Peeking out from under your blankets, you take a moment to consider what to do.",
        ],
        'Options': [
            ("Get out of bed.", 2),
            ("Go back to sleep.", 4),
        ]
    },
    2: {
        'Text': [
            "After taking a moment to look around the room, you get out of bed.",
            "You look around the room and see nothing.",
        ],
        'Options': [
            ("Get back in bed.", 4),
            ("Keep looking.", 3),
        ]
    },
    #### END YOUR STORY HERE ####
}
```
###### Step 6
Repeat Step 4 and Step 5 but fill in the information with page 3 rather than page 2.
You code should now look like the following:
```python
from story_engine import *
#### TYPE YOUR CODE BELOW HERE ####
story = {
    #### START YOUR STORY HERE ####
    1: {
        'Text': [
            "It's a dark and stormy night.",
            "Abruptly, you wake to the sound of thunder shaking your room.",
            "Peeking out from under your blankets, you take a moment to consider what to do.",
        ],
        'Options': [
            ("Get out of bed.", 2),
            ("Go back to sleep.", 4),
        ]
    },
    2: {
        'Text': [
            "After taking a moment to look around the room, you get out of bed.",
            "You look around the room and see nothing.",
        ],
        'Options': [
            ("Get back in bed.", 4),
            ("Keep looking.", 3),
        ]
    },
    3: {
        'Text': [
            "You find nothing in the room."
        ],
        'Options': [
            ("Get back in bed.", 4),
        ]
    },
    4: {
        'Text': [
            "Snuggling back under the covers of your bed, you fall back asleep."
            "The end.",
        ],
        'Options': [
        ]
    },
    #### END YOUR STORY HERE ####
}
```
#### How to End an Adventure Game.
###### Step 7
When you want your story to end, all you need to do is remove all options to go to other pages such that a page will look similar to this:
```python
[page number]: {
    'Text': [
        "[line of text]",
        "[line of text]",
        "[line of text]",
    ],
    'Options': [
    ]
},
```
Thus, we will repeat Step 4 and Step 5 and fill in the appriopriate information for page 4. However, page 4 will not have any options.
Once you are finished filling page 4, you code should look like the following:
```python
from story_engine import *
#### TYPE YOUR CODE BELOW HERE ####
story = {
    #### START YOUR STORY HERE ####
    1: {
        'Text': [
            "It's a dark and stormy night.",
            "Abruptly, you wake to the sound of thunder shaking your room.",
            "Peeking out from under your blankets, you take a moment to consider what to do.",
        ],
        'Options': [
            ("Get out of bed.", 2),
            ("Go back to sleep.", 4),
        ]
    },
    2: {
        'Text': [
            "After taking a moment to look around the room, you get out of bed.",
            "You look around the room and see nothing.",
        ],
        'Options': [
            ("Get back in bed.", 4),
            ("Keep looking.", 3),
        ]
    },
    3: {
        'Text': [
            "You find nothing in the room."
        ],
        'Options': [
            ("Get back in bed.", 4),
        ]
    },
    4: {
        'Text': [
            "Snuggling back under the covers of your bed, you fall back asleep."
            "The end.",
        ],
        'Options': [
        ]
    },
    #### END YOUR STORY HERE ####
}
```
###### Step 8
Finally, all we need to do to complete our text-based adventure game is add `story_flow(story)` after the end of the story variable.
Thus, your code should look like the following:
```python
from story_engine import *
#### TYPE YOUR CODE BELOW HERE ####
story = {
    #### START YOUR STORY HERE ####
    1: {
        'Text': [
            "It's a dark and stormy night.",
            "Abruptly, you wake to the sound of thunder shaking your room.",
            "Peeking out from under your blankets, you take a moment to consider what to do.",
        ],
        'Options': [
            ("Get out of bed.", 2),
            ("Go back to sleep.", 4),
        ]
    },
    2: {
        'Text': [
            "After taking a moment to look around the room, you get out of bed.",
            "You look around the room and see nothing.",
        ],
        'Options': [
            ("Get back in bed.", 4),
            ("Keep looking.", 3),
        ]
    },
    3: {
        'Text': [
            "You find nothing in the room."
        ],
        'Options': [
            ("Get back in bed.", 4),
        ]
    },
    4: {
        'Text': [
            "Snuggling back under the covers of your bed, you fall back asleep."
            "The end.",
        ],
        'Options': [
        ]
    },
    #### END YOUR STORY HERE ####
}
story_flow(story)
```
Now it is time to run and test your adventure game!
#### Testing and Playing Your Adventure Game.
_Time to run your adventure game and make fixes._
###### Step 9
Click `Run`!
Your terminal will now start the game from the flow chart above in [Map Your Adventure Game's Story Out](#map-your-adventure-games-story-out).
If you game does not run correctly, continue to the following step.
Otherwise, congratulations! You have made your own text-based adventure game!
###### Fix Error Step
If by chance you made an error in your code, it is important that you learn the basics of troubleshooting some simple errors that might arise.
Below are a few possible fixes to errors that might arise:
- Syntax Error
  - You have forgotten to put quotations marks around lines of text and options.
  - You have a different number of open and close brackets.
- Indentation Error
  - You have used a mixture of tabs and spaces.
  - You have not indented all lines in a block equally.
- Page Number Error
  - If you game does not go to the correct page, check to make sure an option goes to the page it is supposed to.
Additionally, ensure that your code is exactly the same in format as the code provided above.
## Closing
#### Review of Learned Concepts
We have covered an exceptional number of concepts; we should take a moment to review what we have learned.
When you run the game, you’ll see your current location and what you can do.  
Type commands at the prompt (`>`) to move or interact.

- You have learned what Python is.
- You have learned how to run code in a terminal.
- You have learned what a function is.
- You have learned what a variable is.
- You have learned how to format a story for text-based adventure.
- You have learned how to put all these concepts together.
### Available Commands
- `go [north/south/east/west]` — move between locations  
- `get [item]` — pick up an item (like `get boat` or `get gold`)  
- `use [item]` — use an item (e.g. `use boat` to win!)  
- `exit` — quit the game  

Congratulations, you have learned a lot!
You win by collecting **both the gold and the boat**, or by using the boat at the river.

#### Resources to Learn More
---

If you want to learn more about Python there are hundreds of great tutorials online. Below I have provided a few links to some great resources
## 🗺️ Game Map

- [LearnPython.org](https://www.learnpython.org/) (Interactive Python Tutorials)
- [Coursera.org](https://www.coursera.org/projects/introduction-to-python) (Guided Python tutorials)
- [CodeAcademy.com](https://www.codecademy.com/learn/learn-python-3) (Interactive Python Tutorials)

#### Challenge Yourself
- **Forest** — starting point. Paths lead north and east.  
- **River** — find a *boat*. Use it to sail away.  
- **Cave** — find *gold*.  

If you want to learn more about how everything works, feel free to look at `story_engine.py`. Though it looks rather complicated, it is actually quite simple.
---

Just take a moment to read through it line-by-line and try to understand exactly what is going. Even try modifying some of the code on your own to see what happen.
## 🧩 Game Logic Highlights

A big portion of learning how to code is experimentation and research. Try modifying the code and Googling code that might seem confusing.
- Simple command parser (split by spaces).  
- Each room has a description, exits, and optional items.  
- Tracks player’s inventory.  
- Two possible win conditions:
  1. `use boat` at the river.  
  2. Collect both *boat* and *gold*.  

## Thank you!
---

Thank you for taking time to read this set of instructions! I hope that everything here helped you learn more about how to code and was a fun experience that you can take the skills learned forward.
## 💻 How to Run the Game

Writing code is a valuable skill and will only become more valuable moving into the future. There is an exceptional amount of potential to use code to help positively impact the world. Though we only made a simple text-based adventure game, the skill learned can be used to create incredibly cool applications.
1. Make sure you have **Python 3.8+** installed.  
2. Save the script as `game.py`.  
3. In your terminal or command prompt, run:

For instance, you could create an interactive application to teach someone a complex topic.
   ```bash
   python game.py
#Example Gameplay
Adventure Game
==============
Commands: go [north/south/east/west], get [item], use [item], exit
---------------------------
You are in the Forest
Inventory: []
You are in a dark forest. Paths lead north and east.
> go north
---------------------------
You are in the River
Inventory: []
You stand beside a rushing river. There is a small boat here.
> get boat
You picked up the boat!
> use boat
You get into the boat and sail across the river... You win! 🏆

However, remember it is your reasonability to code ethically. Code can be turned malicious incredibly easily; thus, it is your responsibility to make sure you understand the consequences of your code before you share it with the world.

## Licenses & Links
