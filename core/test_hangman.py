import unittest
import core.hangman as hangman


class HangmanStartGameTests(unittest.TestCase):
    def setUp(self):
        self.result = hangman.start_game()

    def test_can_start_game(self):
        self.assertIsNotNone(self.result)
    
    def test_game_starts_unfinished(self):
        self.assertFalse(self.result.is_finished)

    def test_game_has_target_word(self):
        self.assertIsNotNone(self.result.target_word)
        self.assertIn(self.result.target_word, hangman.TARGET_WORDS)

    def test_game_has_current_discovered(self):
        self.assertIsNotNone(self.result.current_discovered)
        self.assertTrue(
            len(self.result.current_discovered), 
            len(self.result.target_word)
        )
        self.assertSequenceEqual(
            [None for x in range(len(self.result.target_word))],
            self.result.current_discovered
        )

    def test_game_has_lives_left(self):
        self.assertEqual(5, self.result.lives_left)

    def test_game_has_has_won(self):
        self.assertFalse(self.result.has_won)

class HangmanTakeTurnTests(unittest.TestCase):
    def test_state_cannot_be_none(self):
        with self.assertRaises(ValueError):
            hangman.take_turn(None, "m")

    def test_guess_cannot_be_none(self):
        with self.assertRaises(ValueError):
            hangman.take_turn(hangman.start_game(), None)

    def _test_take_turn_core(self,
        state,
        guess,
        expected_is_finished,
        expected_current_discovered,
        expected_lives_left,
        expected_has_won=False
    ):
        result = hangman.take_turn(state, guess)
        self.assertEqual(expected_is_finished, result.is_finished)
        self.assertEqual(state.target_word, result.target_word)
        self.assertEqual(
            expected_current_discovered,
            result.current_discovered
        )
        self.assertEqual(expected_lives_left, result.lives_left)
        self.assertEqual(expected_has_won, result.has_won)

    #pass in correct letter you don't have
    def test_pass_in_correct_letter_we_dont_have(self):
        state = hangman.HangmanState(["monitor"])
        self._test_take_turn_core(
            state,
            "o",
            False,
            [None, "o", None, None, None, "o", None],
            state.lives_left
        )


    #pass in correct letter you have
    def test_pass_in_correct_letter_we_have(self):
        state = hangman.HangmanState(["monitor"])
        state.current_discovered = [None, "o", None, None, None, "o", None]
        self._test_take_turn_core(
            state,
            "o",
            False,
            [None, "o", None, None, None, "o", None],
            state.lives_left
        )

    #pass in final correct letter
    def test_pass_in_final_correct_letter(self):
        state = hangman.HangmanState(["monitor"])
        state.current_discovered = ["m", "o", "n", None, "t", "o", "r"]
        self._test_take_turn_core(
            state,
            "i",
            True,
            ["m", "o", "n", "i", "t", "o", "r"],
            state.lives_left,
            True
        )

    #pass in incorrect letter
    def test_guess_incorrect_letter(self):
        state = hangman.HangmanState(["monitor"])
        self._test_take_turn_core(
            state,
            "x",
            False,
            state.current_discovered,
            state.lives_left - 1
        )

    #pass in incorrect letter when you're on your last life
    def test_guess_incorrectly_and_lose_last_life(self):
        state = hangman.HangmanState(["monitor"])
        state.lives_left = 1
        self._test_take_turn_core(
            state,
            "x",
            True,
            state.current_discovered,
            0
        )

    #should store win/loss, not just finished
    #pass in finished game
    #pass in multi-character guess


if __name__ == '__main__':
    unittest.main()
