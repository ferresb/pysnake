import logging
from enum import Enum

APPLE_RATE  = 15
MAX_APPLE   = 10
BASE_SIZE   = 9

class Direction(Enum):
    UP      = 1
    RIGHT   = 2
    DOWN    = 3
    LEFT    = 4

logging.basicConfig(filename='snake.log',filemode='w',level=logging.DEBUG)
logger = logging.getLogger('snake_app')
