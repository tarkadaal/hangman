import random


class HangmanState():
    def __init__(
            self, 
            is_finished,
            target_word,
            current_known,
            lives_left,
            was_last_guess_correct
    ):
        # Whether the game is still running or has finished
        self.is_finished = is_finished

        # Which word the player is trying to guess
        self.target_word = target_word

        # This is a list, containing the player's current knowledge of 
        # the word. It starts out as containing one None for each letter
        # in the target word, which get replaced with letters once the
        # player guesses them correctly.
        self.current_known = current_known

        # Number of lives remaining.
        self.lives_left = lives_left

        # Was the player's last guess correct?
        self.was_last_guess_correct = was_last_guess_correct

    @staticmethod
    def create(target_words, lives):
        target = random.randint(0, len(target_words) - 1)
        target_word = target_words[target]
        return HangmanState(
            False,
            target_word,
            [None for x in range(len(target_word))],
            lives,
            None
        )

    @property
    def has_won(self):
        return self.is_finished and None not in self.current_known
