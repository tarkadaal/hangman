import random
import copy

TARGET_WORDS =[
    "3dhubs", "marvin", "print", "filament", "order", "layer"
]
LIVES = 5

class HangmanState():
    def __init__(self, target_words=TARGET_WORDS):
        self.is_finished = False
        target = random.randint(0, len(target_words) - 1)
        self.target_word = target_words[target]
        self.current_discovered = [None for x in range(len(self.target_word))]
        self.lives_left = LIVES


def start_game():
    return HangmanState()


def take_turn(state, guess):
    if state is None:
        raise ValueError("The 'state' parameter cannot be None")

    if guess is None:
        raise ValueError("The 'guess' parameter cannot be None")

    new_state = copy.copy(state)
    if guess in state.target_word:
        new_state.current_discovered = _calculate_new_discovered(
            state.target_word,
            state.current_discovered,
            guess
        )
        new_state.is_finished = None not in new_state.current_discovered
    else:
        new_state.lives_left -= 1
    
    return new_state


def _calculate_new_discovered(target, current_discovered, guess, modifier=0):
    index = target.find(guess)
    new_discovered = copy.copy(current_discovered)
    new_discovered[index + modifier] = guess

    rest = target[index+1:]
    if guess in rest:
        new_discovered = _calculate_new_discovered(
            rest,
            new_discovered,
            guess,
            index + 1
        )
    return new_discovered
