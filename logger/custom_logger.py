import os
import logging
from datetime import datetime

class CustomLogger:
    def __init__(self, log_dir="logs"):
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, log_file)

    def get_logger(self, name=__file__):
        logger_name = os.path.splitext(os.path.basename(name))[0]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        logger.propagate = False  # Avoid duplicate logs if root logger is set

        if not logger.handlers:
            # Define formatter
            formatter = logging.Formatter(
                fmt='[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            # File handler
            file_handler = logging.FileHandler(self.log_file_path)
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
if __name__ == "__main__":
    logger = CustomLogger().get_logger("DocumentPortal")
    logger.info("This is an info message")
    logger.error("This is an error message")
