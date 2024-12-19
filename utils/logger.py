import logging

def setup_logger(log_file="application.log"):
    """
    Set up a logger to log messages to a file.
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger()

logger = setup_logger()