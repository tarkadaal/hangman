import core.hangman as hangman

def print_state(state):
    formatted_current_guess = hangman.format_current_known(state.current_known)
    print(f"Lives remaining: {state.lives_left}")
    print(f"Word: {formatted_current_guess}")
    print()


def prompt_for_guess():
    return input("Guess a letter: ")


def main():
    print("Welcome to Hangman!")
    state = hangman.start_game()
    while not state.is_finished:
        print_state(state)
        guess = prompt_for_guess()
        state = hangman.take_turn(state, guess)
    
    if state.has_won:
        print("Well done")
    else:
        print("Sorry, better luck next time.")


if __name__ == "__main__":
    main()