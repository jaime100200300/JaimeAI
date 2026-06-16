# parser.py

from tokens import TokenType, Token
from nodes import *
from nodesq import *

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

    def peek(self):
        if self.i+1 < len(self.tokens):
            return self.tokens[self.i+1]
        return None


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
                tok.type in (TokenType.PERIOD, TokenType.COMMA, TokenType.EXCLAMATION)
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
        

        # ANSWER NODES
        if tok.type == TokenType.WORD:

            if tok.value == "html":
                self.advance()
                return AnswerHtmlNode()

            if tok.value == "txt" or tok.value == "text":
                self.advance()
                return AnswerTxtNode()

            if tok.value == "md" or tok.value == "markdown":
                self.advance()
                return AnswerMdNode()

            if tok.value == "python" or tok.value == "py":
                self.advance()
                return AnswerPythonNode()
            
            if tok.value == "anything" or tok.value == "idk":
                self.advance()
                return AnswerAnythingNode()


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
        # -----------------------------
        # WHO / WHAT
        # -----------------------------
        if tok.type == TokenType.WORD and tok.value in ("who", "what"):

            # count consecutive "who", or consume one "what"
            count = 0
            if tok.value == "who":
                while (
                    self.current() is not None
                    and self.current().type == TokenType.WORD
                    and self.current().value == "who"
                ):
                    count += 1
                    self.advance()
            else:
                self.advance()

            if count >= 2:
                return StopChantingWhoNode()

            tok = self.current()

            # who/what is X
            if tok and tok.type == TokenType.WORD and tok.value in ("is", "are"):
                self.advance()
                tok = self.current()
                if tok:
                    thing = tok.value
                    self.advance()
                    return WhoIsNode(thing)
                return WhoIsNode(None)

            # if it's "what" without "is", treat as unknown
            return WhoIsNode(None)

        
        if tok.type == TokenType.WORD and tok.value == "think":
            self.advance()
            return ThinkNode()
        
        # -----------------------------
        # MAKE PROJECT
        # -----------------------------
        if tok.type == TokenType.WORD and tok.value == "make":
            self.advance()
            tok = self.current()

            if tok is None:
                return MakeWhatNode()


            # optional "a"
            if tok.type == TokenType.WORD and tok.value in ("a", "an"):
                self.advance()
                tok = self.current()
                if tok is None:
                    return MakeWhatNode()

            # must be "project"
            if tok.type == TokenType.WORD and tok.value == "project":
                self.advance()
                tok = self.current()

                # subject exists
                if tok and tok.type == TokenType.WORD:
                    subject = tok.value
                    self.advance()
                    return MakeProjectNode(subject)

                # no subject -> ask which kind of project
                return MakeProjectNode()

            # user said "make" but not "project"
            return MakeWhatNode()

        if tok.type == TokenType.WORD and tok.value == "wait":
            self.advance()
            tok = self.current()

            # default wait time
            num = 1.0

            # optional number
            if tok and tok.type == TokenType.NUM:
                num = float(tok.value)
                self.advance()
                tok = self.current()

            # optional "seconds" or "secs"
            if tok and tok.type == TokenType.WORD and tok.value in ("seconds", "secs"):
                self.advance()

            return WaitSecondsNode(num)

        if tok.type == TokenType.WORD and tok.value in ("hello", "hi", "wassup", "waddup", "hey"):
            self.advance()
            tok = self.current()

            # optional comma
            if tok and tok.type == TokenType.COMMA:
                self.advance()
                tok = self.current()   # <-- FIX

            # optional "bro" or "dude"
            if tok and tok.type == TokenType.WORD and tok.value in ("bro", "dude"):
                self.advance()
                tok = self.current()   # <-- FIX

            # optional "!"
            if tok and tok.type == TokenType.EXCLAMATION:
                self.advance()
                tok = self.current()   # <-- FIX

            return HelloNode()

        if tok.type == TokenType.WORD and tok.value in ("bye", "exit", "cya", "ttyl"):
            self.advance()
            tok = self.current()

            # skip optional "bro" or "dude"
            if tok and tok.type == TokenType.WORD and tok.value in ("bro", "dude"):
                self.advance()

            return ByeNode()



            


        # -----------------------------
        # FALLBACK
        # -----------------------------
        text = " ".join(t.value for t in self.tokens[self.i:])
        self.i = len(self.tokens)
        return UnknownNode(text)
