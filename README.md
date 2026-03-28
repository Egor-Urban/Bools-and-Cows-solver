# Bulls and Cows Solver

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Version](https://img.shields.io/badge/Version-1.3-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Metadata

* **Author:** Egor Urban
* **Repository:** [https://github.com/Egor-Urban](https://github.com/Egor-Urban)
* **Version:** 1.3

---

## Description

**Bulls and Cows Solver** is a simple command-line tool that helps solve the classic logical game *"Bulls and Cows"*.

The solver uses:

* brute-force search over all valid candidates
* filtering based on user-provided feedback
* basic combinatorics (permutations of digits)

### Supported Rules

* The secret number consists of exactly **4 digits**
* Digits range from **0 to 9**
* All digits are **unique** (no repetitions)

### How It Works

1. The program generates all possible valid 4-digit numbers.
2. It makes an initial random guess.
3. After each guess, the user provides feedback:

   * `A` (bulls): correct digit in the correct position
   * `B` (cows): correct digit in the wrong position
4. The solver filters out impossible candidates.
5. The process repeats until the correct number is found or no candidates remain.

---

## Project Structure

```
.
├── solver.py   # Main solver implementation and CLI interface
└── README.md   # Project documentation
```

### Core Components (`solver.py`)

#### `BullsAndCowsSolver`

Main class responsible for solving logic.

* `__init__`
  Generates all possible 4-digit numbers with unique digits.

* `first_guess()`
  Returns an initial random guess.

* `score(guess, target)`
  Calculates the number of bulls and cows between two numbers.

* `apply_feedback(guess, bulls, cows)`
  Filters candidate solutions based on feedback.

* `next_guess()`
  Returns the next guess from remaining candidates.

---

#### `play()`

CLI interface that:

* interacts with the user
* reads feedback
* drives the solving loop

---

#### Entry Point

```python
if __name__ == "__main__":
```

* Displays ASCII banner
* Starts interactive solving session

---

## Usage

Run the solver:

```bash
python solver.py
```

Example interaction:

```
> First guess: 1234
> Enter result (AB): 12
  Bulls: 1
  Cows : 2
> Next guess: 1325
```

---

## Notes

* The solver does not guarantee the minimal number of moves.
* Strategy is intentionally simple (random selection among valid candidates).
* Incorrect user input may lead to inconsistent state ("no solutions left").

---

## Future Improvements

* Smarter guessing strategy (e.g., minimax / entropy-based)
* Support for
