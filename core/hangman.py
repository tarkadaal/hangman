import random

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