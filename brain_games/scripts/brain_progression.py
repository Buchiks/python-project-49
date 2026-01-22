import random

from brain_games import logic, welcome_user1


def progression():
    progress_list = []
    progress_list.append(str(random.randint(0, 100)))
    d = random.randint(1, 20)
    for i in range(9):
        progress_list.append(str(int(progress_list[i]) + d))
    return progress_list


def main():
    name = welcome_user1()
    rounds = 3
    for round in range(rounds):
        prog = progression()
        blind = random.randint(0, 9)
        correct_ans = prog[blind]
        prog[blind] = ".."
        prog = " ".join(prog)
        logic(prog, correct_ans, name)
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()