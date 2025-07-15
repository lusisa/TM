from typing import Iterator
import gradio as gr
from transformers.utils import logging
from model import get_input_token_length, run

logging.set_verbosity_info()
logger = logging.get_logger("transformers")

DEFAULT_SYSTEM_PROMPT = """"""
MAX_MAX_NEW_TOKENS = 2-48
