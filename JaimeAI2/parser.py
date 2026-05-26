# parser.py

from tokens import TokenType, Token
from nodes import *

class Parser:
    """The parser parses one command only."""
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.i = 0

    def current(self):
        if self.i < len(self.tokens):
            return self.tokens[self.i]
        return None

    def advance(self):
        self.i += 1

    def parse(self):

        tok = self.current()

        # empty input
        if tok is None:
            return UnknownNode("")

        # --- solve ---
        if tok.type == TokenType.WORD and tok.value == "solve":
            self.advance()  # skip "solve"
            tok = self.current()

            if tok is None:
                return SolveNode([])

            parts = []

            while tok is not None:

                parts.append(tok.value)
                self.advance()
                tok = self.current()

            return SolveNode(parts)

        # fallback
        return UnknownNode(" ".join(t.value for t in self.tokens))
