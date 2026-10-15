# Tic Tac Toe

**English** | [Русский](README.ru.md)

A desktop Tic Tac Toe game written in Python with [customtkinter](https://github.com/TomSchimansky/CustomTkinter). You can play against a friend on the same computer or against a built-in AI, and you have full control over who moves first and who plays X or O.

![screenshot](screenshot.png)

## Table of contents

- [Features](#features)
- [Game modes](#game-modes)
- [How the AI works](#how-the-ai-works)
- [Installation](#installation)
- [Usage](#usage)
- [Building an .exe](#building-an-exe)
- [Project structure](#project-structure)
- [Known limitations](#known-limitations)
- [Roadmap](#roadmap)
- [Author](#author)

## Features

- Three game modes: Player vs Player, Player vs AI, AI vs Player
- Choose who makes the first move
- Choose whether player 1 plays **X** or **O**
- Score board during the session: wins of player 1, wins of player 2, games played and ties
- Visual feedback at the end of a game: the board turns green on a win and black on a tie
- Pop-up message with the result of each game
- Clean black-and-white interface built with customtkinter
- Start a new game at any time with one button, the score is kept

## Game modes

| Player 1 | Player 2 | Mode |
|----------|----------|------|
| Player   | Player   | Two humans on one computer |
| Player   | AI       | You are player 1, the AI is player 2 |
| AI       | Player   | The AI is player 1, you are player 2 |

The settings at the top of the window can be combined freely:

- **Who goes first?**: player 1 or player 2
- **Who will be player 1?**: human or AI
- **Who will be player 2?**: human or AI
- **Player 1 symbol**: X or O

For example, if the AI is player 1 and goes first, it makes its move right after you press **play**, and you play with the opposite symbol.

## How the AI works

The AI is rule-based. On each turn it checks the following priorities from top to bottom and makes the first move that applies:

1. **Win**: if it has two in a line and the third cell is free, it takes it
2. **Block**: if the opponent has two in a line, it takes the third cell
3. **Center**: it takes the center cell if it is free
4. **Corner**: it takes a random free corner
5. **Side**: it takes a random free side cell

The AI always wins or blocks when it can, but it does not look further ahead, so it is possible to beat it by creating a double threat. Corners and sides are chosen randomly, so games are not identical every time.

## Installation

Requirements:

- Python 3.8 or newer
- [customtkinter](https://pypi.org/project/customtkinter/)

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install customtkinter
```

`tkinter` is included with the standard Python installer on Windows and macOS. On some Linux distributions it must be installed separately:

```bash
sudo apt install python3-tk
```

## Usage

Make sure `imag.ico` is in the same folder as the script, then run:

```bash
python main.py
```

Step by step:

1. Choose who goes first.
2. Choose who is player 1 and who is player 2 (human or AI).
3. Choose whether player 1 plays X or O.
4. Press **play**.
5. Click on a free cell to make your move.
6. When the game ends, press **play** again to start a new round. The score board is kept.

## Building an .exe

You can turn the game into a standalone Windows application with [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=imag.ico --add-data "imag.ico;." main.py
```

The result will appear in the `dist` folder. To make the icon load correctly inside the built `.exe`, load it through the `openicon` helper:

```python
window.wm_iconbitmap(openicon("imag.ico"))
```

On Linux and macOS use `:` instead of `;` in `--add-data`.

## Project structure

```
.
├── main.py          # game logic, AI and user interface
├── imag.ico         # window icon
├── screenshot.png   # screenshot for the README
├── README.md        # English version
└── README.ru.md     # Russian version
```

Main parts of `main.py`:

- `Cs()`: the AI move logic
- `Win()`: checks for a win or a tie, updates the score board and the board colors
- `GameOver()`: tells whether the current game is already finished
- `step()`: handles a click on a cell
- `StartGame()`: reads the settings, resets the board and starts a new game
- `openicon()`: resolves the path to resources, also when running from a PyInstaller bundle

## Known limitations

- AI vs AI is not supported
- The `.ico` window icon works on Windows; on Linux and macOS it may need to be removed or replaced
- The score is not saved after the program is closed
- The AI is not unbeatable

## Roadmap

- [ ] Difficulty levels for the AI (including an unbeatable mode with minimax)
- [ ] Saving the score between sessions
- [ ] Highlighting the winning line
- [ ] Light/dark theme switch
- [ ] Refactoring the AI code to remove duplication

## Author

jmyrickk
