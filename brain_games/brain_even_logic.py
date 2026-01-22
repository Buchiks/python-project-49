import random

import prompt

from brain_games import welcome_user1


def even():
    name = welcome_user1()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    num_of_correct_answers = 3
    while n < num_of_correct_answers:
        number = random.randint(1, 1000)
        print(f"Question: {number}")
        ans = prompt.string("Your answer: ")
        if (number % 2 == 0 and ans == "yes" 
            or number % 2 != 0 and ans == "no"):
            print("Correct!")
            n += 1
        else:
            if number % 2 == 0:
                print(f"'{ans}' is wrong answer ;(. Correct answer was 'yes'.\n"
                f"Let's try again, {name}!")
            else:
                print(f"'{ans}' is wrong answer ;(. Correct answer was 'no'.\n"
                f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
    
