from lexer import TokenType, Token

def get_value(token: Token): return token.value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0

    def current(self):
        return self.tokens[self.i] if self.i < len(self.tokens) else None

    def advance(self):
        self.i += 1

    def parse():
        ast = []

        return ast