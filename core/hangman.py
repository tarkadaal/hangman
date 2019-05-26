import random
import copy

TARGET_WORDS =[
    "3dhubs", "marvin", "print", "filament", "order", "layer"
]
LIVES = 5

class HangmanState():
    def __init__(self, target_words):
        self.is_finished = False
        target = random.randint(0, len(target_words) - 1)
        self.target_word = target_words[target]
        self.current_known = [None for x in range(len(self.target_word))]
        self.lives_left = LIVES

    @property
    def has_won(self):
        return self.is_finished and None not in self.current_known


def start_game(possible_words=None):
    words = possible_words if possible_words else TARGET_WORDS
    return HangmanState(words)


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

    new_state = copy.copy(state)
    if guess in state.target_word:
        new_state.current_known = _calculate_new_known(
            state.target_word,
            state.current_known,
            guess
        )
        new_state.is_finished = None not in new_state.current_known
    else:
        new_state.lives_left -= 1
        if new_state.lives_left == 0:
            new_state.is_finished = True
    return new_state


def _calculate_new_known(target, current_known, guess, modifier=0):
    index = target.find(guess)
    new_known = copy.copy(current_known)
    new_known[index + modifier] = guess

    rest = target[index+1:]
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
