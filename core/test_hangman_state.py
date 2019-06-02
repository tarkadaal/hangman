import unittest
from core.hangman_state import HangmanState

class HangmanStateTests(unittest.TestCase):
    def test_basic_construction(self):
        target_word = "courage"
        expected_current_known = [None for x in target_word]
        state = HangmanState(
            False,
            target_word,
            expected_current_known,
            5,
            None
        )
        self.assertIsNotNone(state)
        self.assertFalse(state.is_finished)
        self.assertEqual(target_word, state.target_word)
        self.assertSequenceEqual(
            expected_current_known,
            state.current_known
        )
        self.assertEqual(5, state.lives_left)
        self.assertIsNone(state.was_last_guess_correct)

    def test_create_game(self):
        wordlist = ['target', 'words']
        state = HangmanState.create(wordlist, 3)
        self.assertIsNotNone(state)
        self.assertFalse(state.is_finished)
        self.assertTrue(state.target_word in wordlist)
        self.assertSequenceEqual(
            [None for x in state.target_word], 
            state.current_known
        )
        self.assertEqual(3, state.lives_left)
        self.assertIsNone(state.was_last_guess_correct)
