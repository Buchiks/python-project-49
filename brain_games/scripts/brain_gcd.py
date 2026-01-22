import random

from brain_games import logic, welcome_user1


def main():
    name = welcome_user1()
    print("Find the greatest common divisor of given numbers.")
    rounds = 3
    for round in range(rounds):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        task = f"{x} {y}"
        while y != 0:
            temp = x
            x = y
            y = temp % x
        correct_ans = str(x)
        logic(task, correct_ans, name)
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()