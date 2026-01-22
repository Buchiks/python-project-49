import prompt

import sys


def logic(task, correct_ans, name):
    print(f"Question: {task}")
    users_ans = prompt.string("Your answer: ")
    if users_ans == correct_ans:
        print("Correct!")
    else:
        print(f"'{users_ans}' is wrong answer ;(. " +
            f"Correct answer was '{correct_ans}'.\n"
                f"Let's try again, {name}!")
        sys.exit()
        

