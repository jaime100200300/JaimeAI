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

        # -----------------------------
        # RUN COMMAND
        # -----------------------------
        if tok.type == TokenType.WORD and tok.value == "run":
            self.advance()
            tok = self.current()

            # optional "the"
            if tok and tok.type == TokenType.WORD and tok.value == "the":
                self.advance()
                tok = self.current()

            # optional "command"
            if tok and tok.type == TokenType.WORD and tok.value == "command":
                self.advance()
                tok = self.current()

            # QUOTED VERSION
            if tok and tok.type == TokenType.QUOTE:
                cmd = tok.value
                self.advance()
                return RunCommandNode(cmd)

            # UNQUOTED VERSION
            parts = []
            while tok and tok.type in (TokenType.WORD, TokenType.NUM, TokenType.QUOTE):
                parts.append(tok.value)
                self.advance()
                tok = self.current()

            return RunCommandNode(" ".join(parts))

        # -----------------------------
        # SOLVE
        # -----------------------------
        if tok.type == TokenType.WORD and tok.value == "solve":
            self.advance()
            tok = self.current()

            # QUOTED SOLVE
            if tok and tok.type == TokenType.QUOTE:
                expr = tok.value
                self.advance()
                return SolveNode([expr])

            # UNQUOTED SOLVE
            parts = []
            while tok is not None:
                if tok.type in (TokenType.PERIOD, TokenType.COMMA):
                    break
                if tok.type == TokenType.WORD and tok.value in ("and", "solve"):
                    break
                parts.append(tok.value)
                self.advance()
                tok = self.current()

            return SolveNode(parts)

        # -----------------------------
        # WHO / WHAT
        # -----------------------------
        if tok.type == TokenType.WORD and tok.value in ("who", "what"):

            # count consecutive "who"
            count = 0
            while (
                self.current() is not None
                and self.current().type == TokenType.WORD
                and self.current().value == "who"
            ):
                count += 1
                self.advance()

            if count >= 2:
                return StopChantingWhoNode()

            tok = self.current()

            # who is X
            if tok and tok.type == TokenType.WORD and tok.value in ("is", "are"):
                self.advance()
                tok = self.current()
                if tok:
                    thing = tok.value
                    self.advance()
                    return WhoIsNode(thing)
                return WhoIsNode(None)

            return WhoIsNode(None)
        
        if tok.type == TokenType.WORD and tok.value == "think":
            self.advance()
            return ThinkNode()


        # -----------------------------
        # FALLBACK
        # -----------------------------
        text = " ".join(t.value for t in self.tokens)
        self.i = len(self.tokens)
        return UnknownNode(text)
