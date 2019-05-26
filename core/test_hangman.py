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

if __name__ == '__main__':
    unittest.main()
