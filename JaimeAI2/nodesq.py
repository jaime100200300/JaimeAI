from nodes import Node
from dataclasses import dataclass

@dataclass
class AnswerHtmlNode(Node):
    pass

@dataclass
class AnswerTxtNode(Node):
    pass

@dataclass
class AnswerMdNode(Node):
    pass

@dataclass
class AnswerPythonNode(Node):
    pass

@dataclass
class AnswerAnythingNode(Node):
    pass