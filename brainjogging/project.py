#!/usr/bin/env python3

import sys
import random
import pyfiglet


def main():
    try:
        if sys.argv[1] == "--math10" and len(sys.argv) == 2:
            func1()
            sys.exit(0)

        elif sys.argv[1] == "--math30" and len(sys.argv) == 2:
            func2()
            sys.exit(0)

        elif sys.argv[1] == "--rps10" and len(sys.argv) == 2:
            func3()
            sys.exit(0)

        elif sys.argv[1] == "--rps30" and len(sys.argv) == 2:
            func4()
            sys.exit(0)

        elif sys.argv[1] == "--sentences10" and len(sys.argv) == 2:
            func5()
            sys.exit(0)

        elif sys.argv[1] == "--sentences30" and len(sys.argv) == 2:
            func6()
            sys.exit(0)

        elif len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)

        elif len(sys.argv) >= 3:
            print("Too many command-line arguments")
            sys.exit(1)

    except EOFError:
        pyfiglet.FigletFont.getFonts()

        outcome = "You did exit the program!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print("\n" + fontrender)
        sys.exit(0)


def func1():
    counter = 0
    score = 0

    while counter < 10:
        counter += 1
        try:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            operator = ["+", "-", "*", "/"]
            op = random.choice(operator)

            if op == "+":
                result = x + y
            elif op == "-":
                x = random.randint(1, 9)
                y = random.randint(1, 9)
                if x > y:
                    result = x - y
                elif y > x:
                    x = random.randint(10, 19)
                    y = random.randint(0, 9)
                    result = x - y
                elif x == y:
                    result = x - y
            elif op == "*":
                result = x * y
            elif op == "/":
                x = random.randint(1, 9)
                y = random.randint(1, 9)
                temp = int(x * y)
                result = temp / y

            if op == "+" or op == "-" or op == "*":
                solution = int(
                    input(f"Please solve this little equation: {x} {op} {y} = ")
                )
            elif op == "/":
                solution = int(
                    input(f"Please solve this little equation: {temp} {op} {y} = ")
                )

            if result == solution:
                score = score + 1
            elif result != solution:
                continue

        except ValueError:
            continue

    pyfiglet.FigletFont.getFonts()

    if counter == 10 and score >= 7:
        outcome = f"Score {score} out of 10! You win!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)

    elif counter == 10 and score < 7:
        outcome = f"Score {score} out of 10! You lose!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)


def func2():
    counter = 0
    score = 0

    while counter < 30:
        counter += 1
        try:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            operator = ["+", "-", "*", "/"]
            op = random.choice(operator)

            if op == "+":
                result = x + y
            elif op == "-":
                x = random.randint(1, 9)
                y = random.randint(1, 9)
                if x > y:
                    result = x - y
                elif y > x:
                    x = random.randint(10, 19)
                    y = random.randint(0, 9)
                    result = x - y
                elif x == y:
                    result = x - y
            elif op == "*":
                result = x * y
            elif op == "/":
                x = random.randint(1, 9)
                y = random.randint(1, 9)
                temp = int(x * y)
                result = temp / y

            if op == "+" or op == "-" or op == "*":
                solution = int(
                    input(f"Please solve this little equation: {x} {op} {y} = ")
                )
            elif op == "/":
                solution = int(
                    input(f"Please solve this little equation: {temp} {op} {y} = ")
                )

            if result == solution:
                score = score + 1
            elif result != solution:
                continue

        except ValueError:
            continue

    pyfiglet.FigletFont.getFonts()

    if counter == 30 and score >= 21:
        outcome = f"Score {score} out of 30! You win!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)

    elif counter == 30 and score < 21:
        outcome = f"Score {score} out of 30! You lose!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)


def func3():
    counter = 0
    score = 0

    while counter < 10:
        counter += 1

        task = ["Win on", "Lose on"]
        gesture = ["rock", "paper", "scissors"]
        choosen1 = random.choice(task)
        choosen2 = random.choice(gesture)

        solution = (
            input(f"{choosen1} {choosen2} - so what's your choice? ").lower().strip()
        )

        if choosen1 == "Win on" and choosen2 == "rock" and solution == "paper":
            score = score + 1
        elif choosen1 == "Lose on" and choosen2 == "rock" and solution == "scissors":
            score = score + 1
        elif choosen1 == "Win on" and choosen2 == "rock" and solution != "paper":
            continue
        elif choosen1 == "Lose on" and choosen2 == "rock" and solution != "scissors":
            continue

        elif choosen1 == "Win on" and choosen2 == "paper" and solution == "scissors":
            score = score + 1
        elif choosen1 == "Lose on" and choosen2 == "paper" and solution == "rock":
            score = score + 1
        elif choosen1 == "Win on" and choosen2 == "paper" and solution != "scissors":
            continue
        elif choosen1 == "Lose on" and choosen2 == "paper" and solution != "rock":
            continue

        elif choosen1 == "Win on" and choosen2 == "scissors" and solution == "rock":
            score = score + 1
        elif choosen1 == "Lose on" and choosen2 == "scissors" and solution == "paper":
            score = score + 1
        elif choosen1 == "Win on" and choosen2 == "scissors" and solution != "rock":
            continue
        elif choosen1 == "Lose on" and choosen2 == "scissors" and solution != "paper":
            continue

    pyfiglet.FigletFont.getFonts()

    if counter == 10 and score >= 7:
        outcome = f"Score {score} out of 10! You win!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)

    elif counter == 10 and score < 7:
        outcome = f"Score {score} out of 10! You lose!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)


def func4():
    counter = 0
    score = 0

    while counter < 30:
        counter += 1

        task = ["Win on", "Lose on"]
        gesture = ["rock", "paper", "scissors"]
        choosen1 = random.choice(task)
        choosen2 = random.choice(gesture)

        solution = (
            input(f"{choosen1} {choosen2} - so what's your choice? ").lower().strip()
        )

        if choosen1 == "Win on" and choosen2 == "rock" and solution == "paper":
            score = score + 1
        elif choosen1 == "Lose on" and choosen2 == "rock" and solution == "scissors":
            score = score + 1
        elif choosen1 == "Win on" and choosen2 == "rock" and solution != "paper":
            continue
        elif choosen1 == "Lose on" and choosen2 == "rock" and solution != "scissors":
            continue

        elif choosen1 == "Win on" and choosen2 == "paper" and solution == "scissors":
            score = score + 1
        elif choosen1 == "Lose on" and choosen2 == "paper" and solution == "rock":
            score = score + 1
        elif choosen1 == "Win on" and choosen2 == "paper" and solution != "scissors":
            continue
        elif choosen1 == "Lose on" and choosen2 == "paper" and solution != "rock":
            continue

        elif choosen1 == "Win on" and choosen2 == "scissors" and solution == "rock":
            score = score + 1
        elif choosen1 == "Lose on" and choosen2 == "scissors" and solution == "paper":
            score = score + 1
        elif choosen1 == "Win on" and choosen2 == "scissors" and solution != "rock":
            continue
        elif choosen1 == "Lose on" and choosen2 == "scissors" and solution != "paper":
            continue

    pyfiglet.FigletFont.getFonts()

    if counter == 30 and score >= 21:
        outcome = f"Score {score} out of 30! You win!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)

    elif counter == 30 and score < 21:
        outcome = f"Score {score} out of 30! You lose!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)


def func5():
    counter = 0
    score = 0

    while counter < 10:
        try:
            counter += 1
            letter = chr(random.randint(ord("a"), ord("z")))
            solution1, solution2, solution3, solution4, solution5 = (
                input(
                    f"Build a five words sentence where every word begins with: '{letter}' - so what's your sentence? "
                )
                .lower()
                .lstrip()
                .rstrip()
                .split(" ")
            )

            if (
                solution1.startswith(f"{letter}") == True
                and solution2.startswith(f"{letter}") == True
                and solution3.startswith(f"{letter}") == True
                and solution4.startswith(f"{letter}") == True
                and solution5.startswith(f"{letter}") == True
            ):
                score = score + 1
            else:
                continue

        except ValueError:
            continue

    pyfiglet.FigletFont.getFonts()

    if counter == 10 and score >= 7:
        outcome = f"Score {score} out of 10! You win!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)

    elif counter == 10 and score < 7:
        outcome = f"Score {score} out of 10! You lose!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)


def func6():
    counter = 0
    score = 0

    while counter < 30:
        counter += 1

        try:
            letter = chr(random.randint(ord("a"), ord("z")))
            solution1, solution2, solution3, solution4, solution5 = (
                input(
                    f"Build a five words sentence where every word begins with: '{letter}' - so what's your sentence? "
                )
                .lower()
                .lstrip()
                .rstrip()
                .split(" ")
            )

            if (
                solution1.startswith(f"{letter}") == True
                and solution2.startswith(f"{letter}") == True
                and solution3.startswith(f"{letter}") == True
                and solution4.startswith(f"{letter}") == True
                and solution5.startswith(f"{letter}") == True
            ):
                score = score + 1
            else:
                continue

        except ValueError:
            continue

    pyfiglet.FigletFont.getFonts()

    if counter == 30 and score >= 21:
        outcome = f"Score {score} out of 30! You win!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)

    elif counter == 30 and score < 21:
        outcome = f"Score {score} out of 30! You lose!"
        fontrender = pyfiglet.figlet_format(outcome, font="slant")
        print(fontrender)
        sys.exit(0)


if __name__ == "__main__":
    main()
