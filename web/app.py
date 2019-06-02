import core.hangman as hangman
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/hangman/api/start_game')
def start_game():
    state = hangman.start_game()
    dict_state = _dictify_game_state(state)
    return jsonify(dict_state)


def _dictify_game_state(state):
    return {
        "is_finished": state.is_finished,
        "target_word": state.target_word,
        "current_known": state.current_known,
        "lives_left": state.lives_left,
        "was_last_guess_correct": state.was_last_guess_correct,
        "has_won": state.has_won
    }
