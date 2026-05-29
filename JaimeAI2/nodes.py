# nodes.py

from dataclasses import dataclass

# ===== BASE NODE =====

@dataclass
class Node:
    """Base class for all AST nodes."""
    pass


@dataclass
class StopChantingWhoNode(Node):
    pass


# ===== COMMAND NODES =====

@dataclass
class SolveNode(Node):
    expr: list  # list of tokens or strings

@dataclass
class WhoIsNode(Node):
    thing: str | None


@dataclass
class RunCommandNode(Node):
    command: str | list[str]



@dataclass
class UnknownNode(Node):
    text: str