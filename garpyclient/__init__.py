__version__ = "0.3.6"

import logging

from .client import GarminClient

logging.getLogger(__name__).addHandler(logging.NullHandler())
