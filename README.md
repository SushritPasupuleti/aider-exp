# Aider Experiments

Using Aider to test out local codegen workflows

## Tested Flows

- [x] Implementing a function in a file
- [x] Implementing a function in a file with a test case
- [x] Implementing a function in a file with a test case and a streamlit UI
- [x] Implementing a function in a file with a test case and a FastAPI service

## Setup

```bash
poetry install && poetry shell && aider-install
```

Ensure `ollama` is installed and available in your PATH.

## Usage

```bash
aider --model ollama_chat/<model> <files>
# or depending on the model
aider --model ollama/<model> <files>
```

## Prompts

To generate `main.py` based on `functions.py`:

> Using the functions in functions.py create a main function in main.py to implement a function that takes user input, and returns encrypted text while writing a test case to make sure the encryption and decryption works.

To generate `streamlit` UI based on `main.py`:
> Using main.py as reference, build a streamlit UI to serve the same functionality.

To generate `FastAPI` service based on `main.py`:
> Using main.py build a FastAPI service to serve the 2 functions as endpoints.
