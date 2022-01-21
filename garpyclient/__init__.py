__version__ = "0.1.0"

import logging

from .client import GarminClient

logging.getLogger(__name__).addHandler(logging.NullHandler())
