import unittest
import io
from core.hangman_storage import HangmanStorage

class HangmanStorageTests(unittest.TestCase):
    def _initialise_sut_with(text):
        def wrap(func):
            def core(self):
                with io.StringIO(text) as buf:
                    sut = HangmanStorage(buf)
                    func(self, sut)
            return core
        return wrap

    def test_raises_if_no_stream(self):
        with self.assertRaises(ValueError):
            HangmanStorage(None)

    def test_raises_if_data_is_corrupt(self):
        with io.StringIO("corrupt data") as buf:
            with self.assertRaises(ValueError):
                HangmanStorage(buf)

    @_initialise_sut_with("")
    def test_empty_streams_default_to_zero(self, sut):
        self.assertEqual(0, sut.get_high_score())

    @_initialise_sut_with("4")
    def test_score_is_read_from_stream(self, sut):
        self.assertEqual(4, sut.get_high_score())

    @_initialise_sut_with("2")
    def test_update_replaces_with_higher_score(self, sut):
        sut.update_high_score_if_lower_than(3)
        self.assertEqual(3, sut.get_high_score())

    @_initialise_sut_with("2")
    def test_update_does_not_replace_lower_score(self, sut):
        sut.update_high_score_if_lower_than(1)
        self.assertEqual(2, sut.get_high_score())

    @_initialise_sut_with("2")
    def test_update_returns_true_if_new_score_is_higher(self, sut):
        result = sut.update_high_score_if_lower_than(4)
        self.assertEqual(True, result)

    def test_update_persists_changes(self):
        with io.StringIO("2") as buf:
            sut = HangmanStorage(buf)
            sut.update_high_score_if_lower_than(3)
            sut = HangmanStorage(buf)  # reinitialise to check peristence
            self.assertEqual(3, sut.get_high_score())
