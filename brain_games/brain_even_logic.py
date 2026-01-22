from brain_games import welcome_user1
import random
import prompt


def even():
    name = welcome_user1()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    n = 0
    while n < 3:
        number = random.randint(1, 1000)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if number % 2 == 0 and answer == "yes" or number % 2 != 0 and answer == "no":
            print("Correct!")
            n += 1
        else:
            n = 0
            if number % 2 == 0:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'." \
                f"Let's try again, {name}!")
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'." \
                f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")
    
