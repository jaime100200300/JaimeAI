

from lexer import lex
from parser import Parser
from engine import Engine
from printing import status, slow




def main():
    engine = Engine()
    while True:
        try:
            line = input("JaimeAI2 > ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        line = line.lower().strip()
        status("Lexing")
        tokens = lex(line)
        status("Parsing")
        ast = Parser(tokens).parse()
        status("Thinking")
        response = engine.run(ast)
        slow(response)

if __name__ == "__main__":
    main()
