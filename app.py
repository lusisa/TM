from typing import Iterator
import gradio as gr
from sympy.physics.units import temperature
from transformers.utils import logging
from model import get_input_token_length, run

logging.set_verbosity_info()
logger = logging.get_logger("transformers")

DEFAULT_SYSTEM_PROMPT = """"""
MAX_MAX_NEW_TOKENS = 2048
DEFAULT_MAX_NEW_TOKENS = 1024
MAX_INPUT_TOKEN_LENGTH = 4000

DESCRIPTION = """"""

LICENSE = """"""

logger.info("Starting")
def clear_and_save_textbox(message: str) -> tuple[str, str]:
    return "", message

def display_input(message: str,
                  history: list[tuple[str, str]]) -> list[tuple[str, str]]:
    history.append(message, "")
    logger.info("display_input=%s", message)
    return history

def delete_prev_fn(history: list[tuple[str, str]]) -> tuple[list[tuple[str, str]], str]:
    try:
        message, _ = history.pop()
    except IndexError:
        message = ''
    return history, message or ''

def generate(
        message: str,
        history_with_input: list[tuple[str, str]],
        system_prompt: str,
        max_new_tokens: int,
        temperature: float,
        top_p: float,
        top_k: int,
) -> Iterator[list[tuple[str, str]]]:
    logger.info("message=%s", message)
    if max_new_tokens > MAX_MAX_NEW_TOKENS:
        raise ValueError

    history = history_with_input[:-1]


