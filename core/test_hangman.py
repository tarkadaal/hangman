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


class HangmanTakeTurnTests(unittest.TestCase):
    def test_state_cannot_be_none(self):
        with self.assertRaises(ValueError):
            hangman.take_turn(None, "m")

    def test_guess_cannot_be_none(self):
        with self.assertRaises(ValueError):
            hangman.take_turn(hangman.start_game(), None)

    #pass in correct letter you don't have
    def test_pass_in_correct_letter_we_dont_have(self):
        state = hangman.HangmanState(["monitor"])
        result = hangman.take_turn(state, "o")
        self.assertEqual(False, result.is_finished)
        self.assertEqual(state.target_word, result.target_word)
        self.assertEqual(
            [None, "o", None, None, None, "o", None],
            result.current_discovered
        )
        self.assertEqual(state.lives_left, result.lives_left)


    #pass in correct letter you have
    def test_pass_in_correct_letter_we_have(self):
        state = hangman.HangmanState(["monitor"])
        state.current_discovered = [None, "o", None, None, None, "o", None]
        result = hangman.take_turn(state, "o")
        self.assertEqual(False, result.is_finished)
        self.assertEqual(state.target_word, result.target_word)
        self.assertEqual(
            [None, "o", None, None, None, "o", None],
            result.current_discovered
        )
        self.assertEqual(state.lives_left, result.lives_left)

    #pass in final correct letter
    def test_pass_in_final_correct_letter(self):
        state = hangman.HangmanState(["monitor"])
        state.current_discovered = ["m", "o", "n", None, "t", "o", "r"]
        result = hangman.take_turn(state, "i")
        self.assertEqual(True, result.is_finished)
        self.assertEqual(state.target_word, result.target_word)
        self.assertEqual(
            ["m", "o", "n", "i", "t", "o", "r"],
            result.current_discovered
        )
        self.assertEqual(state.lives_left, result.lives_left)

    #pass in incorrect letter
    def test_guess_incorrect_letter(self):
        state = hangman.HangmanState(["monitor"])
        result = hangman.take_turn(state, "x")
        self.assertEqual(False, result.is_finished)
        self.assertEqual(state.target_word, result.target_word)
        self.assertEqual(
            state.current_discovered,
            result.current_discovered
        )
        self.assertEqual(state.lives_left -1 , result.lives_left)

    #pass in incorrect letter when you're on your last life
    #pass in finished game
    #pass in multi-character guess


if __name__ == '__main__':
    unittest.main()
