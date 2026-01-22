import random

from brain_games import logic, welcome_user1


def main():
    name = welcome_user1()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num_of_rounds = 3
    temp = 0
    while temp < num_of_rounds:
        number = random.randint(1, 1000)
        if number % 2 == 0:
            correct_ans = "yes"
        else:
            correct_ans = "no"
        logic(number, correct_ans, name)
        temp += 1
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()