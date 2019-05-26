import unittest
import core.hangman as hangman

class HangmanStartGameTests(unittest.TestCase):
    def test_can_start_game(self):
        result = hangman.start_game()
        self.assertIsNotNone(result)
    
    def test_game_starts_unfinished(self):
        result = hangman.start_game()
        self.assertFalse(result.is_finished)

    def test_game_has_target_word(self):
        result = hangman.start_game()
        self.assertIsNotNone(result.target_word)
        self.assertIn(result.target_word, hangman.TARGET_WORDS)

    def test_game_has_current_discovered(self):
        result = hangman.start_game()
        self.assertIsNotNone(result.current_discovered)
        self.assertTrue(
            len(result.current_discovered), 
            len(result.target_word)
        )
        self.assertSequenceEqual(
            [None for x in range(len(result.target_word))],
            result.current_discovered
        )

if __name__ == '__main__':
    unittest.main()
