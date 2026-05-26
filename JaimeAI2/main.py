

from lexer import lex
from parser import Parser
from engine import Engine

def main():
    engine = Engine()
    while True:
        try:
            line = input("JaimeAI2 > ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        tokens = lex(line)
        ast = Parser(tokens).parse()
        response = engine.run(ast)

        print(response)

if __name__ == "__main__":
    main()
