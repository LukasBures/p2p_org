import logging
import os
import sys
from datetime import datetime

from common.config import LOG_TO_FILE, LOGGING_LEVEL, WORKING_DIRECTORY


def logging_setup() -> None:
    """
    Logging setting. Only console or console + time.log file.

    :return: None.
    """
    if LOG_TO_FILE:
        logging.basicConfig(
            level=LOGGING_LEVEL,
            format="%(asctime)s | %(levelname)-7s | %(filename)s:%(lineno)d | %(message)s",
            handlers=[
                logging.FileHandler(
                    f"{os.path.join(WORKING_DIRECTORY, 'logs/')}/{str(datetime.now()).replace(' ', '_')}.log"
                ),
                logging.StreamHandler(sys.stdout),
            ],
            force=True,
        )
    else:
        logging.basicConfig(
            level=LOGGING_LEVEL,
            format="%(asctime)s | %(levelname)-7s | %(filename)s:%(lineno)d | %(message)s",
            handlers=[logging.StreamHandler(sys.stdout)],
            force=True,
        )
