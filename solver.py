"""
Bulls and Cows Solver
---------------------

A simple solver for the classic "Bulls and Cows" game based on
brute-force filtering and basic combinatorics.

Rules supported:
- Secret number has exactly 4 digits
- Digits range from 0 to 9
- All digits are unique (no repeats)

Developer: https://github.com/Egor-Urban
Version: 1.3
"""



import random
from itertools import permutations



class BullsAndCowsSolver:
    def __init__(self):
        # generate all possible 4-digit numbers with unique digits
        self.candidates = list(permutations(range(10), 4))
        random.shuffle(self.candidates)

    
    def first_guess(self):
        return self._format(random.choice(self.candidates))

    
    def _format(self, number_tuple):
        return ''.join(map(str, number_tuple))

    
    def score(self, guess, target):
        bulls = sum(g == t for g, t in zip(guess, target))
        cows = sum(g in target for g in guess) - bulls
        return bulls, cows

    
    def apply_feedback(self, guess, bulls, cows):
        # leave only numbers that match the feedback
        self.candidates = [
            num for num in self.candidates
            if self.score(guess, self._format(num)) == (bulls, cows)
        ]

    
    def next_guess(self):
        if not self.candidates:
            return None
        return self._format(random.choice(self.candidates))



def play():
    solver = BullsAndCowsSolver()
    guess = solver.first_guess()
    attempts = 1

    print(f"> First guess: {guess}")

    while True:
        # input loop
        while True:
            raw = input("> Enter result (AB): ").strip()
            if len(raw) != 2 or not raw.isdigit():
                print("! Invalid input, expected two digits like '12'")
                continue
            break

        bulls, cows = int(raw[0]), int(raw[1])

        print(f"  Bulls: {bulls}")
        print(f"  Cows : {cows}")

        if bulls == 4:
            print(f"> Solved in {attempts} attempts.")
            break

        solver.apply_feedback(guess, bulls, cows)
        guess = solver.next_guess()

        if guess is None:
            print("! No solutions left. Check your inputs.")
            break

        print(f"> Next guess: {guess}")
        attempts += 1



if __name__ == "__main__":
    print("""
    ░▒█▀▀▄░░░█▀▀▄░█▀▀▄░█▀▄░░░▒█▀▀▄░░░█▀▄░█░░░░█▀▀░█▀▀▄░▀█▀
    ░▒█▀▀▄░░░█▄▄█░█░▒█░█░█░░░▒█░░░░░░█░░░█▀▀█░█▀▀░█▄▄█░░█░
    ░▒█▄▄█░░░▀░░▀░▀░░▀░▀▀░░░░▒█▄▄▀░░░▀▀▀░▀░░▀░▀▀▀░▀░░▀░░▀░
                        by Urban Egor
        """)

    print("Enter result as 'AB': A = bulls, B = cows")
    play()

