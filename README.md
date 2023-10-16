# Spelling Bee Game Documentation

Welcome to the documentation for the Spelling Bee Game! This Python application allows you to test and improve your spelling skills. The game involves pronouncing words and then challenging the player to spell them correctly within a limited time.

**Author: Bamidele Precious**

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Getting Started](#getting-started)
4. [Game Instructions](#game-instructions)
5. [High Scores](#high-scores)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The Spelling Bee Game is a command-line-based spelling game designed to help you enhance your spelling skills. It offers various levels of difficulty and uses a list of words stored in a CSV file. The game features include:

- Multiple difficulty levels: Choose from Beginner, Intermediate, Advanced, Expert, and Impossible.
- Unique word selection: Eight unique words are randomly selected from the chosen difficulty level.
- Spelling challenge: The game pronounces a word and challenges you to spell it correctly within a time limit.
- Scoring system: Your score is calculated based on your correct spellings, and you have a limited number of lives.
- High score tracking: The game keeps track of your high scores and provides an average score.

## Prerequisites

Before running the Spelling Bee Game, you need to ensure you have the following prerequisites installed:

- Python 3.x
- Required Python packages (you can install them using pip):

  ```bash
  pip install tabulate pyttsx3 pandas mypy black pytest
  ```
-tabulate, csv, random, pyttsx3, pandas, time, mypy, black, pytest, sys 

## Getting Started

To run the game on your system, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/spelling-bee-game.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd spelling-bee-game
    ```

3. **Run the game:**

    ```bash
    python spelling_bee_game.py
    ```

    Follow the on-screen prompts to play the game.

## Game Instructions

1. **Select Your Username:**

    When you start the game, you will be prompted to enter your username. The game will capitalize the first word and strip any leading or trailing spaces.

2. **Choose Your Level:**

    You will be presented with a table of difficulty levels from 1 to 5. Enter the number corresponding to your desired level (1 for Beginner, 2 for Intermediate, and so on).

3. **Spelling Challenge:**

    - The game will select eight unique words from the chosen difficulty level.
    - Each word will be pronounced using a robot voice.
    - You will have 20 seconds to spell each word correctly.
    - You can type "R" to replay the pronunciation of the word.

4. **Scoring:**

    - Your current score and remaining lives are displayed throughout the game.
    - You gain an extra life when you reach a score of 2 or 5.
    - If you run out of lives, the game ends, and your final score is calculated.

5. **Game Over:**

    - Your final score and a corresponding emoji will be displayed.
    - Your score will be saved, and you can choose to view the high scores or start a new game.

## High Scores

The game keeps track of high scores and provides an average score. To view high scores:

1. During the game, type "H" to get high scores.

   The top five high scores and the average score will be displayed.

2. If your current score is higher than the average score, you will be notified that you've surpassed the average.

## Contributing

If you'd like to contribute to the Spelling Bee Game project, feel free to fork the repository, make your changes, and submit a pull request. I welcome improvements, bug fixes, and new features.
