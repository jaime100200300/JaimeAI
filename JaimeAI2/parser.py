# parser.py

from tokens import TokenType, Token
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0

    def current(self):
        if self.i < len(self.tokens):
            return self.tokens[self.i]
        return None

    def advance(self):
        self.i += 1

    # -----------------------------
    # TOP-LEVEL MULTI-PARSER
    # -----------------------------
    def parse(self):
        nodes = []

        while True:
            node = self.parse_one()
            if node is not None:
                nodes.append(node)

            tok = self.current()
            if tok is None:
                break

            # skip punctuation and filler words
            while tok is not None and (
                tok.type in (TokenType.PERIOD, TokenType.COMMA)
                or (tok.type == TokenType.WORD and tok.value == "and")
            ):
                self.advance()
                tok = self.current()

            if tok is None:
                break

        return nodes

    # -----------------------------
    # SINGLE COMMAND PARSER
    # -----------------------------
    def parse_one(self):
        tok = self.current()
        if tok is None:
            return None

        # ---- solve ----
        if tok.type == TokenType.WORD and tok.value == "solve":
            self.advance()  # skip "solve"
            tok = self.current()

            # --- QUOTED SOLVE ---
            if tok is not None and tok.type == TokenType.QUOTE:
                expr = tok.value
                self.advance()
                return SolveNode([expr])

            # --- UNQUOTED SOLVE ---
            parts = []
            while tok is not None:

                # STOP CONDITIONS:
                if tok.type in (TokenType.PERIOD, TokenType.COMMA):
                    break

                # STOP ON "and" OR another "solve"
                if tok.type == TokenType.WORD and tok.value in ("and", "solve"):
                    break

                parts.append(tok.value)
                self.advance()
                tok = self.current()

            return SolveNode(parts)

        # fallback: preserve previous full-token text but advance to end
        text = " ".join(t.value for t in self.tokens)
        self.i = len(self.tokens)
        return UnknownNode(text)
