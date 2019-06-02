import core.hangman as hangman
from core.hangman_state import HangmanState

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/hangman/api/start_game')
def start_game():
    state = hangman.start_game()
    dict_state = _dictify_game_state(state)
    return jsonify(dict_state)

@app.route('/hangman/api/take_turn', methods=['POST'])
def take_turn():
    state = _classify_game_state(request.json)
    new_state = hangman.take_turn(state, request.json["guess"])
    dict_state = _dictify_game_state(new_state)
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

def _classify_game_state(json):
    return HangmanState(
        json["is_finished"],
        json["target_word"],
        json["current_known"],
        json["lives_left"],
        json["was_last_guess_correct"]
    )
