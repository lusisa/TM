from threading import Thread
from typing import Iterator

#import torch
from transformers.utils import logging
from ctransformers import AutoModelForCausalLM
from transformers import TextIteratorStreamer, AutoTokenizer

logging.set_verbosity_info()
logger = logging.get_logger("transformers")

config = {"max_new_tokens": 256, "repetition_penalty": 1.1,
          "temperature": 0.1, "stream": True}
model_id = "TheBloke/Llama-2-7B-Chat-GGML"
device = "cpu"

model = AutoModelForCausalLM.from_pretrained(model_id, model_type="llama", lib="avx2", hf=True)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

def get_prompt(message: str, chat_history: list[tuple[str, str]],
               system_prompt: str) -> str:
    logger.info("get_prompt chat_history=%s", chat_history)




