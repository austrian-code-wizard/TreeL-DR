import time
from typing import Dict, List
from functools import wraps
from flask import jsonify
import traceback
from logging import getLogger
import coloredlogs
from config import LOG_LEVEL

logger = getLogger("UtilLogger")
coloredlogs.install(level=LOG_LEVEL, logger=logger)

def remove_none_from_dict(data: Dict):
    new_data = data.copy()
    for key in data:
        if data[key] == None:
            del new_data[key]
    return new_data

class Timer:
    """Context manager to time of code execution
    
    Attributes:
        logger (logging.logger): logger.
        concept (str): description for logging.
    """

    def __init__(self, logger=None, concept="", start_message="", end_message=""):
        self.logger = logger
        self.concept = concept
        self.start_message = start_message
        self.end_message = end_message

    def __enter__(self):
        self.start = time.time()
        self.logger.info(f"{self.concept} started...")
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start

        self.logger.info(f"-> {self.concept} took {self.interval:.3f} seconds")

def remove_none_from_list(data: List):
    return [val for val in data if val is not None]

def clean_phone_number(number: str):
    cleaned_number = "".join([char for char in number if char.isnumeric()])
    if number[0] == "+":
        cleaned_number = "+" + cleaned_number
    return cleaned_number

def format_event_name(text: str):
    text = text.split("_")
    text = [word.capitalize() for word in text]
    return " ".join(text)

def handle_error(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error: {traceback.format_exc()}")
            return jsonify({"info": f"An error occured: {traceback.format_exc()}"}), 500
    return wrapper

