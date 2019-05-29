import unittest
import io
from core.hangman_storage import HangmanStorage

class HangmanStorageTests(unittest.TestCase):
    def test_is_constructed_with_stream(self):
        with io.StringIO("") as buf:
            self.assertIsNotNone(HangmanStorage(buf))

    def test_raises_if_no_stream(self):
        with self.assertRaises(ValueError):
            HangmanStorage(None)

    def test_empty_streams_default_to_zero(self):
        with io.StringIO("") as buf:
            sut = HangmanStorage(buf)
            self.assertEqual(0, sut.get_high_score())

    def test_score_is_read_from_stream(self):
        with io.StringIO("4") as buf:
            sut = HangmanStorage(buf)
            self.assertEqual(4, sut.get_high_score())

    def test_raises_if_data_is_corrupt(self):
        with io.StringIO("corrupt data") as buf:
            with self.assertRaises(ValueError):
                HangmanStorage(buf)
