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

    def test_game_has_current_known(self):
        self.assertIsNotNone(self.result.current_known)
        self.assertTrue(
            len(self.result.current_known), 
            len(self.result.target_word)
        )
        self.assertSequenceEqual(
            [None for x in range(len(self.result.target_word))],
            self.result.current_known
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
    
    def test_guess_cannot_be_multiple_characters(self):
        with self.assertRaises(ValueError):
            hangman.take_turn(hangman.start_game(), "hi")

    def test_guess_cannot_be_empty_string(self):
        with self.assertRaises(ValueError):
            hangman.take_turn(hangman.start_game(), "")

    def _test_take_turn_core(
        self,
        state,
        guess,
        expected_is_finished,
        expected_current_known,
        expected_lives_left,
        expected_has_won=False
    ):
        result = hangman.take_turn(state, guess)
        self.assertEqual(expected_is_finished, result.is_finished)
        self.assertEqual(state.target_word, result.target_word)
        self.assertEqual(
            expected_current_known,
            result.current_known
        )
        self.assertEqual(expected_lives_left, result.lives_left)
        self.assertEqual(expected_has_won, result.has_won)


    def test_pass_in_correct_letter_we_dont_have(self):
        state = hangman.HangmanState(["monitor"])
        self._test_take_turn_core(
            state,
            "o",
            False,
            [None, "o", None, None, None, "o", None],
            state.lives_left
        )


    def test_pass_in_correct_letter_we_have(self):
        state = hangman.HangmanState(["monitor"])
        state.current_known = [None, "o", None, None, None, "o", None]
        self._test_take_turn_core(
            state,
            "o",
            False,
            [None, "o", None, None, None, "o", None],
            state.lives_left
        )

    def test_pass_in_final_correct_letter(self):
        state = hangman.HangmanState(["monitor"])
        state.current_known = ["m", "o", "n", None, "t", "o", "r"]
        self._test_take_turn_core(
            state,
            "i",
            True,
            ["m", "o", "n", "i", "t", "o", "r"],
            state.lives_left,
            True
        )

    def test_guess_incorrect_letter(self):
        state = hangman.HangmanState(["monitor"])
        self._test_take_turn_core(
            state,
            "x",
            False,
            state.current_known,
            state.lives_left - 1
        )

    def test_guess_incorrectly_and_lose_last_life(self):
        state = hangman.HangmanState(["monitor"])
        state.lives_left = 1
        self._test_take_turn_core(
            state,
            "x",
            True,
            state.current_known,
            0
        )

    def test_raises_if_game_is_finished(self):
        state = hangman.HangmanState(["string"])
        state.is_finished = True
        state.current_known = list(state.target_word)
        state.lives_left = 3
        with self.assertRaises(ValueError):
            self._test_take_turn_core(
                state,
                "s",
                True,
                state.current_known,
                3,
                True
            )


class HangmanStringFormatterTests(unittest.TestCase):
    def test_raises_on_empty(self):
        with self.assertRaises(ValueError):
            hangman.format_current_known([])

    def test_with_completely_unknown(self):
        result = hangman.format_current_known(
            [None for x in range(6)]
        )
        self.assertEqual("______", result)

    def test_with_some_known_letters(self):
        result = hangman.format_current_known(
            ["p", None, "o", "n", None]
        )
        self.assertEqual("p_on_", result)

    def test_with_all_known_letters(self):
        result = hangman.format_current_known(
            ["u", "t", "i", "l", "i", "t", "y"]
        )
        self.assertEqual("utility", result)

if __name__ == '__main__':
    unittest.main()
