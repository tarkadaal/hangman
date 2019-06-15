# Hangman
This is a simple implementation of Hangman.
## Project Structure
There are four main components:
* *Core:* This is the library that contains the main Hangman logic.
* *play_hangman.py:* This is a simple CLI that uses the library to play the game.
* *API:* This is an HTTP REST API that exposes the Core functionality.
* *Web:* This is a simple HTML/JS page that uses the API to play the game.

## Prerequisites

This project depends on Flask and Flask-CORS. There's a `requirements.txt` file listing the dependencies, so they can all be installed with:

```
pip3 install -r requirements.txt
```

## Core

The Core is written in a functional style, and is fully unit tested. Call `hangman.start_game` to get a new game state object, which can be passed to `hangman.take_turn` along with your guess. `hangman.take_turn` doesn't modify the original state, it returns a new copy. There are utility functions for formatting states to strings, and for scoring.

High scores are implemented by a seperate module, to keep the functional and stateful elements separated. 

To run the unit tests:
```
./run_tests.py
```

## play_hangman.py

This is a very thin wrapper around the core, and contains no logic other than the game loop.

## API

The API is a thin wrapper over the Core. The only logic it should perform is things necessary to format the data for a web client. It's built using Flask, and contains two endpoints: `/hangman/api/start_game`, and `/hangman/api/take_turn`.

To run the API:
```
./run_api.sh
```

## Web

An HTML/CSS/JS front end to the API. 

*IMPORTANT:* You'll need to edit `web/hangman.js`, and change the IP in `base_url` to be the IP of the machine on which you're running the API.

To run the Web:
```
./run_web.sh
```

## TODO

The brief was to deliver a minimum viable product to explore architecture and maintainability. As such, there as a number of improvements that could be made, such as:

* There's currently no santisation of data, or much in the way of error handling.
* There should be a layer in the Core which wraps the existing hangman.py with the High Score functionality. This would remove work from the clients while still keeping the inner core stateless.
* The high scores module currently operates on a stream for persistence; I'd like to wrap it with an abstracted storage class which provided getters and setters for scores. That would make it easier to add a database or similar at some point in the future.
* The game could store previous guesses and display them to the user.
* The Web UI could be changed to use raw keystrokes, not a prompt box.
