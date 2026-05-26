from dataclasses import dataclass
from enum import Enum, auto

class TokenType(Enum):
    WORD = auto()
    NUM = auto()
    COMMA = auto()
    PERIOD = auto()
    EXCLAMATION = auto()
    QUESTION = auto()

@dataclass
class Token:
    type: TokenType
    value: str