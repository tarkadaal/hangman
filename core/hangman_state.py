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
        self.is_finished = is_finished
        self.target_word = target_word
        self.current_known = current_known
        self.lives_left = lives_left
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
