"""Create a simple shared logger so all modules print consistent messages."""

import logging
import sys


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger and avoid adding duplicate handlers."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(handler)
    logger.propagate = False
    return logger
