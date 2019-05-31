import core.hangman as hangman
from core.hangman_storage import HangmanStorage

STORAGE = "./high_scores"

def print_state(state):
    formatted_current_guess = hangman.format_current_known(state.current_known)
    print(f"Lives remaining: {state.lives_left}")
    print(f"Word: {formatted_current_guess}")
    print()


def prompt_for_guess():
    return input("Guess a letter: ")


def print_was_guess_correct(state):
    if state.was_last_guess_correct:
        print("Nice guess!")
    else:
        print("Ah, it's close, but it's not the one.")
        print("You lose a life.")


def main():
    print("Welcome to Hangman!")
    with open(STORAGE, "a+") as file:
        storage = HangmanStorage(file)
        high_score = storage.get_high_score()
    print(f"Try to beat the high score of {high_score} points!")
    
    state = hangman.start_game()
    while not state.is_finished:
        print_state(state)
        guess = prompt_for_guess()
        state = hangman.take_turn(state, guess)
        print_was_guess_correct(state)

    if state.has_won:
        print("Well done!")
        score = hangman.calculate_score(state)
        print(f"You scored {score} points!")
        with open(STORAGE, "r+") as file:
            storage = HangmanStorage(file)
            if storage.update_high_score_if_lower_than(score):
                print("That's a new high score!!")
    else:
        print("Sorry, better luck next time.")


if __name__ == "__main__":
    main()
