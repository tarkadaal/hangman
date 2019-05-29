class HangmanStorage():
    def __init__(self, buffer):
        if buffer is None:
            raise ValueError("The 'buffer' parameter must be a valid stream.")

        self._buffer = buffer
        line = self._buffer.readline()
        self._high_score = 0 if line == "" else int(line)

    def get_high_score(self):
        return self._high_score