# Hogwarts — A Python Text Adventure

A console-based adventure game inspired by the Harry Potter universe, developed in Python as a university project (2025–2026). Create your character, make choices that shape your attributes, discover your house, learn spells, play a Quidditch match and face the Chamber of Secrets.

> **Disclaimer:** unofficial, fan-made educational project, not affiliated with or endorsed by Warner Bros., J.K. Rowling, or any rights holder.

## Features

- **Character creation** with four attributes: Courage, Intelligence, Loyalty, Ambition
- **Interactive storytelling** through choices and dialogues
- **House sorting** based on attributes and answers
- **Inventory and currency** management (100 Galleons to buy supplies and a pet)
- **Spell quiz** and house points
- **Randomized Quidditch match** (Seeker, Golden Snitch, score tracking)
- **Chamber of Secrets extension**: Forbidden Forest, Basilisk, Tom Riddle

## Chapters

| # | Chapter | Author |
|---|---------|--------|
| 1 | Arrival in the Magical World | Joshua Hamon |
| 2 | Friends and House Sorting | Fabio Devine |
| 3 | Learning Spells | Joshua Hamon |
| 4 | Quidditch | Fabio Devine |
| 5 | The Chamber of Secrets (extension) | Fabio Devine |

## Technologies

Python 3 (standard library only: `json`, `random`), JSON data files, command-line interface, modular structure (`chapters/`, `data/`, `universe/`, `utils/`), Git and GitHub.

## Run the game

Requires Python 3 and Git. Data files are loaded with relative paths, so the game must be launched **from the `hogwarts/` folder**:

```bash
git clone https://github.com/fabio-devine/Hogwarts.git
cd Hogwarts/hogwarts
PYTHONPATH=.. python3 -m hogwarts.main
```

On Windows (PowerShell): `$env:PYTHONPATH=".."; python -m hogwarts.main`

## Contributors

The project was developed in pairs. Each contributor coded the chapters assigned to them, and the work was integrated through Git and GitHub.

- **Fabio Devine** — Chapters 2, 4 and 5
- **Joshua Hamon** — Chapters 1 and 3, main menu, house logic, input utilities, initial README

## Use of AI

Fabio Devine used AI tools only as a learning aid: to understand concepts and to get help with bugs or dead ends, alongside the course material.
