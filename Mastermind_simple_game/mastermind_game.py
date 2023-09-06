import random

POSSIBLE_COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code() -> list:
    # generating a random sequence of colors.
    code = []
    for _ in range(CODE_LENGTH):
        current_color = random.choice(POSSIBLE_COLORS)
        code.append(current_color)

    return code


def guess_code() -> list:
    # Taking user input, validating it and returning a list of colors.
    while True:
        current_guess = input("Take a guess...").upper().split()

        if len(current_guess) != CODE_LENGTH:
            print(f"You must enter {CODE_LENGTH} colors!")
            continue

        for color in current_guess:
            if color not in POSSIBLE_COLORS:
                print(f"Invalid color: {color}! Try again.")
                break
        else:
            return current_guess


def check_code(guess, real_code) -> tuple[int, int]:
    colors_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in colors_count:
            colors_count[color] = 0
        colors_count[color] += 1

    comparison_tuple = zip(guess, real_code)

    for guess_color, real_color in comparison_tuple:
        if guess_color == real_color:
            correct_pos += 1
            colors_count[real_color] -= 1

    for guess_color, real_color in comparison_tuple:
        if guess_color in colors_count and colors_count[guess_color] > 0:
            incorrect_pos += 1
            colors_count[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to Mastermind. A random combination of {CODE_LENGTH} colors will be generated You have {TRIES}"
          f" tries to guess the code!\nSeparate your input by a single space.")
    print(f"Possible colors: {' | '.join(POSSIBLE_COLORS)}")
    code = generate_code()
    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_positions, incorrect_positions = check_code(guess, code)
        if correct_positions == CODE_LENGTH:
            print(f"Congratulations, you guessed the combination in {attempt} tries!")
            break
        print(f"Correct positions: {correct_positions}\nIncorrect positions: {incorrect_positions}")

    else:
        print(f"You ran out of tries! The code was: {'|'.join(code)}")


if __name__ == "__main__":
    game()
