import logging
import sys

def setup_logger():
    """Configures the application logger to output to both file and the console"""

    logger = logging.getLogger("trading_bot")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Year-Month-Day Hour:Minute:Second - LOG_LEVEL - Your Message
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # saves everything to a file "trading_bot.log"
        file_handler = logging.FileHandler('trading_bot.log')
        file_handler.setFormatter(formatter)

        # prints the saved log in the terminal window
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger