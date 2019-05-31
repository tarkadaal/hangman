class HangmanStorage():
    def __init__(self, buffer):
        if buffer is None:
            raise ValueError("The 'buffer' parameter must be a valid stream.")

        self._buffer = buffer
        self._buffer.seek(0)
        line = self._buffer.readline()
        self._high_score = 0 if line == "" else int(line)

    def get_high_score(self):
        return self._high_score

    def update_high_score_if_lower_than(self, new_score):
        is_new_score_higher = self._high_score < new_score
        if is_new_score_higher:
            self._buffer.seek(0)
            self._buffer.write(str(new_score))
            self._buffer.flush()
            self._high_score = new_score
        return is_new_score_higher
