# lexer.py

from tokens import Token, TokenType


def lex(src: str):
    tokens = []
    i = 0

    while i < len(src):
        ch = src[i]

        # skip whitespace
        if ch.isspace():
            i += 1
            continue

        # comma
        if ch == ",":
            tokens.append(Token(TokenType.COMMA, ch))
            i += 1
            continue

        # period
        if ch == ".":
            tokens.append(Token(TokenType.PERIOD, ch))
            i += 1
            continue

        if ch == "!":
            tokens.append(Token(TokenType.EXCLAMATION, ch))
            i += 1
            continue

        if ch == "?":
            tokens.append(Token(TokenType.QUESTION, ch))
            i += 1
            continue

        # quote
        if ch == '"':
            tokens.append(make_quote(src, i))
            i = tokens[-1].value_end
            continue


        # number
        if ch.isdigit():
            tokens.append(make_number(src, i))
            i = tokens[-1].value_end
            continue

        # word (letters only)
        if ch.isalpha():
            tokens.append(make_word(src, i))
            i = tokens[-1].value_end
            continue

        # unknown → treat as WORD (your choice)
        tokens.append(Token(TokenType.WORD, ch))
        i += 1

    return tokens


# ===== HELPERS =====

def make_word(src, i):
    start = i
    while i < len(src) and src[i].isalpha():
        i += 1
    word = src[start:i]
    tok = Token(TokenType.WORD, word)
    tok.value_end = i
    return tok


def make_number(src, i):
    start = i
    while i < len(src) and src[i].isdigit():
        i += 1
    num = src[start:i]
    tok = Token(TokenType.NUM, num)
    tok.value_end = i
    return tok

def make_quote(src, i):
    # starting quote
    start = i
    i += 1  # skip the opening "

    value_chars = []

    # read until closing quote OR end of string
    while i < len(src) and src[i] != '"':
        value_chars.append(src[i])
        i += 1

    # if we stopped on a closing quote, skip it
    if i < len(src) and src[i] == '"':
        i += 1

    tok = Token(TokenType.QUOTE, "".join(value_chars))
    tok.value_end = i
    return tok
