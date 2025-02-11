# Aider Experiments

Using Aider to test out local codegen workflows

## Setup

```bash
poetry install && poetry shell && aider-install
```

Ensure `ollama` is installed and available in your PATH.

## Usage

```bash
aider-run --model ollama_chat/<model>.yaml <files>
```

Prompt:

> Using the functions in functions.py create a main function in main.py to implement a function that takes user input, and returns encrypted text while writing a test case to make sure the encryption and decryption works.
