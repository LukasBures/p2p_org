"""
Risk Assessment Model Configuration

This module handles the configuration of the Risk Assessment Model project, including logging,
caching, API keys, and other settings.
"""

import logging
import os
import sys

from starlette.config import Config
from starlette.datastructures import Secret


def get_project_version(config_file: str) -> str:
    """
    Get the project version from the configuration file.

    :param config_file: Path to the configuration file.
    :return: The project version string.
    """
    try:
        with open(config_file, "r") as fp:
            line = fp.readline()
            if line.startswith("__version__"):
                delimiter = '"' if '"' in line else "'"
                return line.split(delimiter)[1]
    except Exception as e:
        return f"Unknown version. Error while reading project version: {e}"


# Determine the location of the configuration file.
dir_name = os.path.dirname(__file__)
config_file_path = os.path.join(dir_name, "../.env")
config = Config(config_file_path)

# Ensure the configuration file is not empty or missing.
if not config.file_values:
    raise Exception("Configuration file .env is empty or is missing!")

# Set the working directory.
WORKING_DIRECTORY: str = os.path.join(dir_name, "../")
sys.path.append(WORKING_DIRECTORY)

# General project configurations.
LOGGING_DEBUG: bool = config("LOGGING_DEBUG", cast=bool, default=False)
LOG_TO_FILE: bool = config("LOG_TO_FILE", cast=bool, default=True)
PROJECT_VERSION: str = get_project_version(f"{WORKING_DIRECTORY}/__init__.py")
PROJECT_NAME: str = config(key="PROJECT_NAME", default="p2p_org")

# Configure logging level based on LOGGING_DEBUG.
LOGGING_LEVEL: int = logging.DEBUG if LOGGING_DEBUG else logging.INFO

# API keys configuration.
INFURA_API_KEY: Secret = config("INFURA_API_KEY", cast=Secret)
ETHERSCAN_API_KEY: Secret = config("ETHERSCAN_API_KEY", cast=Secret)

# Additional configuration and initialization code as needed.
