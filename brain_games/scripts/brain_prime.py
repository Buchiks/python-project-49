import random

import math

from brain_games import logic, welcome_user1


def is_prime(number):
    ceiling = int(math.sqrt(number))
    for i in range(2, ceiling + 1):
        if number % i == 0:
            return "no"
    return "yes"


def main():
    name = welcome_user1()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    rounds = 3
    for round in range(rounds):
        task_number = random.randint(0, 100)
        correct_ans = is_prime(task_number)
        logic(task_number, correct_ans, name)
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()