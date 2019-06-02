import random
import copy
from core.hangman_state import HangmanState

TARGET_WORDS = [
    "3dhubs", "marvin", "print", "filament", "order", "layer"
]
LIVES = 5


def start_game(possible_words=None):
    words = possible_words if possible_words else TARGET_WORDS
    return HangmanState.create(words, LIVES)


def take_turn(state, guess):
    if state is None:
        raise ValueError("The 'state' parameter cannot be None.")

    if state.is_finished:
        raise ValueError(
            "This game is finished, no further moves can be taken.")

    if guess is None:
        raise ValueError("The 'guess' parameter cannot be None.")

    if not len(guess) == 1:
        raise ValueError("The 'guess' parameter must be a single character.")

    return _take_turn(state, guess)


def _take_turn(state, guess):
    new_state = copy.copy(state)
    new_state.was_last_guess_correct = guess in state.target_word
    if new_state.was_last_guess_correct:
        new_state.current_known = _calculate_new_known(
            state.target_word,
            state.current_known,
            guess
        )
        new_state.is_finished = None not in new_state.current_known
    else:
        new_state.lives_left -= 1
        new_state.is_finished = new_state.lives_left == 0
    return new_state


def _calculate_new_known(target, current_known, guess, modifier=0):
    index = target.find(guess)
    new_known = copy.copy(current_known)
    new_known[index + modifier] = guess

    rest = target[index + 1:]
    if guess in rest:
        new_known = _calculate_new_known(
            rest,
            new_known,
            guess,
            index + 1
        )
    return new_known


def format_current_known(known):
    if not known:
        raise ValueError("The 'known' parameter must be a valid hangman known state.")

    santized = [x if x else "_" for x in known]
    return "".join(santized)


def calculate_score(state):
    if not state:
        raise ValueError("The 'state' parameter must be a valid hangman game state.")

    if not state.is_finished:
        raise ValueError("An unfinished game cannot be scored.")

    return state.lives_left if state.has_won else 0
