import engine
from parser import Parser
from lexer import lex
engine = engine.Engine()


def ask(stuff: str):
    parser = Parser(lex(stuff))
    ast = parser.parse()
    engine.run(ast)


if __name__ == "__main__":
    engine.main()