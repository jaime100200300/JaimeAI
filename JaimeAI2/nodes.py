# nodes.py

from dataclasses import dataclass

# ===== BASE NODE =====

@dataclass
class Node:
    """Base class for all AST nodes."""
    pass


# ===== COMMAND NODES =====

@dataclass
class SolveNode(Node):
    expr: list  # list of tokens or strings




@dataclass
class BePotatoNode(Node):
    pass


@dataclass
class StopPotatoNode(Node):
    pass


@dataclass
class UnknownNode(Node):
    text: str
