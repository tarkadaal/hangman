import core.hangman as hangman
from core.hangman_state import HangmanState

from flask import Flask, jsonify, request
from flask_cors import CORS
from core.hangman_storage import HangmanStorage

app = Flask(__name__)
CORS(app)

STORAGE = "./high_scores"

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
    dict_state = {
        "is_finished": state.is_finished,
        "target_word": state.target_word,
        "current_known": state.current_known,
        "lives_left": state.lives_left,
        "was_last_guess_correct": state.was_last_guess_correct,
        "has_won": state.has_won,
        "printable_known": hangman.format_current_known(state.current_known)
    }
    if state.is_finished:
        score = hangman.calculate_score(state)
        dict_state["score"] = score
        dict_state["is_new_high_score"] = _update_high_score(score)
    dict_state["high_score"] = _read_high_score()
    return dict_state

def _classify_game_state(json):
    return HangmanState(
        json["is_finished"],
        json["target_word"],
        json["current_known"],
        json["lives_left"],
        json["was_last_guess_correct"]
    )


def _read_high_score():
    with open(STORAGE, "a+") as file:
        storage = HangmanStorage(file)
        return storage.get_high_score()


def _update_high_score(new_score):
    with open(STORAGE, "r+") as file:
        storage = HangmanStorage(file)
        return storage.update_high_score_if_lower_than(new_score)
