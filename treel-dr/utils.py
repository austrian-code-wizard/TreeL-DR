import time

def remove_none_from_dict(data: dict):
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