import unittest
import core.hangman as hangman

class HangmanTests(unittest.TestCase):
    def test_can_start_game(self):
        result = hangman.start_game()
        self.assertIsNotNone(result)
    
    def test_game_starts_unfinished(self):
        result = hangman.start_game()
        self.assertFalse(result.is_finished)

if __name__ == '__main__':
    unittest.main()
