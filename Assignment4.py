import random

words = ["apple", "bread", "candy", "dream", "eagle",
         "flame", "grape", "house", "input", "joker"]

max_tries = 6


def play_game():
    while True:
        secret_word = generate_secret_word()
        word_length
        word_length = len(secret_word)
        number_try = 1
        print("Welcome to Wordle!")
        print(
            f"Guess the {word_length}-letter word. You have {max_tries} tries.")
        while number_try < max_tries:
            guess = player_guess(word_length, number_try)
            number_try += 1

            if guess == secret_word:
                print("You win!!!")
                break

            result = the_result(secret_word, guess)
            the_display(guess, result)
        else:
            print(f"You lose! The word was: {secret_word}")

        while True:
            play_again = input("Would you like to play again?\n")
            if play_again == "yes":
                break
            elif play_again == "no":
                return
            else:
                print("Please enter 'yes' or 'no'.")


def generate_secret_word():
    return random.choice(words)


def player_guess(word_length, number_try):
    while number_try < max_tries:
        try:
            guess = input(f"Attempt {number_try}/6 – Enter guess: ").lower()
            if len(guess) != word_length:
                print("Wrong length. Expected", word_length)
                continue
            return guess
        except ValueError:
            print("Введіть слово")


def the_result(secret_word, guess):
    result = []
    index = 0
    while index < len(secret_word):
        character = guess[index]
        if character == secret_word[index]:
            result.append("correct")
        elif character in secret_word:
            result.append("present")
        else:
            result.append("absent")
        index += 1
    return result


def the_display(guess, result):
    display = []
    position = 0
    while position < len(result):
        letter = guess[position]
        if result[position] == "correct":
            display.append("["+letter.upper()+"]")
        elif result[position] == "present":
            display.append("("+letter+")")
        else:
            display.append(" "+letter+" ")
        position += 1

    print("Result:", ' '.join(display))


play_game()
