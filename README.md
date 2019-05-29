# Hangman
This is a simple implementation of Hangman.
## Project Structure
There are three main components:
* *Core:* This is the library that contains the main Hangman logic.
* *play_hangman.py:* This is a simple CLI that uses the library to play the game.
* *API:* This is an HTTP REST API that exposes the Core functionality.

## Core

The Core is written in a functional style, and is fully unit tested. Call `hangman.start_game` to get a new game state object, which can be passed to `hangman.take_turn` along with your guess. `hangman.take_turn` doesn't modify the original state, it returns a new copy. There are utility functions for formatting states to strings, and for scoring.

To run the unit tests:
```
python3 -m unittest discover
```

## Hangman.py

This is a very thin wrapper around the core, and contains no logic other than the game loop.