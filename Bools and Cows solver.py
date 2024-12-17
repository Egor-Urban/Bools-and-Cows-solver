'''
Вычислитель ответов для игры "Быки и Коровы" на основе мат. анализа и статистики
!Подходит для правил: 1) число 4-значное, 2) разрешены цифры 0-9!

Разработчик: Urban Egor
Версия: 1.2.8 r
Разработано в России
'''


import random
import itertools



class AbsoluteCowSplver:
    def __init__(self):
        self.x_num = list(itertools.permutations(range(10), 4))
        random.shuffle(self.x_num)
        
        
    def first_gen(self):
        return ''.join(map(str, random.choice(self.x_num)))
    
    
    def progress(self, guess, s):
        bulls = sum(g == s for g, s in zip(guess, s))
        cows = sum(g in s for g in guess) - bulls
        return bulls, cows
    
    
    def filter_(self, guess, bulls, cows):
        self.x_num = [
            number for number in self.x_num 
            if self.progress(guess, ''.join(map(str, number))) == (bulls, cows)
        ]
        
    
    def next_(self):
        if self.x_num:
            return ''.join(map(str, random.choice(self.x_num)))
        return None
    
    

def play():
    solver = AbsoluteCowSplver()
    current_guess = solver.first_gen()
    attempts = 1
    
    
    print(f"| Первое предположение: {current_guess}")
    
    
    while True:
        while True:
            i = input("| Введите результат: ")
        
            if len(str(i)) != 2:
                print("|| Ошибка ввода, попробуйте ещё раз")
                continue
            else:
                break
            
        bulls = int(str(i)[0])
        cows = int(str(i)[1])
        print("[] Быков:", bulls)
        print("[] Коров:", cows)
        
        if bulls == 4:
            print(f"| Число угадано за {attempts} попыток!")
            break
        solver.filter_(current_guess, bulls, cows)
        
        current_guess = solver.next_()
        print(f"| Следующее предположение: {current_guess}")
        attempts += 1

        if not solver.x_num:
            print("|| Невозможно найти число. Возможно, была допущена ошибка при вводе")
            break



if __name__ == "__main__":
    print("""
    ░▒█▀▀▄░░░█▀▀▄░█▀▀▄░█▀▄░░░▒█▀▀▄░░░█▀▄░█░░░░█▀▀░█▀▀▄░▀█▀
    ░▒█▀▀▄░░░█▄▄█░█░▒█░█░█░░░▒█░░░░░░█░░░█▀▀█░█▀▀░█▄▄█░░█░
    ░▒█▄▄█░░░▀░░▀░▀░░▀░▀▀░░░░▒█▄▄▀░░░▀▀▀░▀░░▀░▀▀▀░▀░░▀░░▀░
                        by Urban Egor
        """)
    print("Введите результат в формате 'AB', A - кол-во быков, B - кол-во коров")

    play()
    
    
    
    
    
# P.S. Славя привет)