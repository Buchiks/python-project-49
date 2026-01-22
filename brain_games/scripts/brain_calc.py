import random

from brain_games import logic, welcome_user1


def main():
    name = welcome_user1()
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y
    }
    operators = ["+", "-", "*"]
    print("What is the result of the expression?")
    rounds = 3
    for round in range(rounds):
        x = random.randint(1, 100)
        y = random.randint(1,100)
        operator = random.choice(operators)
        task = f"{x} {operator} {y}"
        correct_ans = str(operations[operator](x, y))
        logic(task, correct_ans, name)
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()