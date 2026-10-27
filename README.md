# Hogwarts — A Python Text Adventure

A console-based adventure game inspired by the Harry Potter universe, developed in Python as part of a university project.

Create your character, explore the wizarding world, make choices that influence your attributes, discover your Hogwarts house, learn spells, compete in a Quidditch match, and face challenges in the Chamber of Secrets.

> **Disclaimer:** This is an unofficial, fan-made educational project inspired by the Harry Potter universe. It is not affiliated with or endorsed by Warner Bros., J.K. Rowling, or any official rights holder.

## Overview

**Hogwarts** is an interactive, text-based game in which the player progresses through a series of chapters using console input. The project combines narrative storytelling with character management, decision-making, JSON-based data, and randomized game mechanics.

The game is organized into separate Python modules, with dedicated folders for chapters, data, utilities, and elements related to the fictional universe.

## Features

- **Character creation:** Choose a first name, last name, and four attributes: Courage, Intelligence, Loyalty, and Ambition.
- **Interactive storytelling:** Progress through the adventure by selecting actions and responding to characters and situations.
- **Hogwarts house sorting:** Determine a house based on character attributes and answers to sorting questions.
- **Inventory and currency management:** Purchase required school supplies and choose a magical pet while managing a starting budget of 100 Galleons.
- **Spell learning:** Explore magical spells and test your knowledge through a quiz.
- **House points:** Earn points through quiz results and Quidditch outcomes.
- **Quidditch simulation:** Participate as a Seeker in a randomized match featuring goals, defensive actions, the Golden Snitch, and score tracking.
- **Chamber of Secrets extension:** Face challenges involving the Forbidden Forest, the Basilisk, and Tom Riddle, with outcomes influenced by character attributes and decisions.

## Game Chapters

### Chapter 1 — Arrival in the Magical World
Create your character, receive your Hogwarts letter, meet Hagrid, and purchase school supplies and a pet. Your available money and required items affect your progression.

### Chapter 2 — Friends and House Sorting
Meet Ron Weasley, Hermione Granger, and Draco Malfoy. Your dialogue choices modify your character's attributes, which contribute to the house-sorting process.

### Chapter 3 — Learning Spells
Discover spells and complete a magical knowledge quiz. Quiz results contribute to the house-point system.

### Chapter 4 — Quidditch
Play as your house's Seeker against a randomly selected opposing house. The match uses randomized scoring events, a possible Golden Snitch appearance, and final score calculations.

### Chapter 5 — The Chamber of Secrets (Extension)
Explore the Forbidden Forest, confront the Basilisk, and encounter Tom Riddle. Choices and character attributes influence the outcomes of these encounters.

## Technologies

- **Python** — game logic, functions, control flow, and player interaction.
- **JSON** — structured storage for game data, including houses, inventory items, spells, quiz questions, and Quidditch teams.
- **Command-line interface** — text-based menus, prompts, and game output.
- **Modular project structure** — separate modules for chapters, utilities, and house-related logic.

## Project Structure

```text
Hogwarts/
├── README.md
└── hogwarts/
    ├── main.py
    ├── menu.py
    ├── chapters/
    │   ├── chapter_1.py
    │   ├── chapter_2.py
    │   ├── chapter_3.py
    │   ├── chapter_4.py
    │   └── chapter_5_extension.py
    ├── data/
    │   ├── houses.json
    │   ├── inventory.json
    │   ├── magic_quiz.json
    │   ├── spells.json
    │   └── teams_quidditch.json
    ├── universe/
    │   ├── characters.py
    │   └── house.py
    └── utils/
        └── input_utils.py
```

## Installation

### Prerequisites

- Python 3
- Git
- A terminal or Python IDE, such as PyCharm

No third-party Python packages are explicitly imported by the project's source files; the game primarily uses Python's built-in functionality.

### Clone the repository

```bash
git clone https://github.com/fabio-devine/Hogwarts.git
cd Hogwarts
```

### Run the game

The main entry point is `hogwarts/main.py`, which launches the main menu.

```bash
python -m hogwarts.main
```

**Note:** The current implementation loads JSON files using relative paths such as `data/inventory.json`, while the data files are located in `hogwarts/data/`. Consequently, the launch command may encounter file-path errors without an appropriate working directory or path configuration. The source code has not been modified to resolve this issue.

## Learning Objectives

This project provided an opportunity to work with:

- Decomposing a program into modules and reusable functions.
- Managing structured data with dictionaries, lists, and JSON files.
- Implementing conditional logic, loops, and user-driven branching.
- Tracking player attributes, inventory, currency, and scores.
- Using randomization to simulate game events.
- Organizing a multi-chapter application with a clear directory structure.

## Contributors

- **Fabio Devine** — project structure and core game logic.
- **Joshua Hamon** — input handling, testing, and documentation.

## Project Context

Developed as a university programming project during the 2025–2026 academic year.

This repository is an educational project. It is not an official Harry Potter game, and all references to the fictional universe belong to their respective rights holders.
