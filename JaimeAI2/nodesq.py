from nodes import Node
from dataclasses import dataclass

@dataclass
class OneWordNode(Node):
    word: str