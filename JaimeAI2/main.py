# main.py

from lexer import lex

def main():
    while True:
        try:
            line = input("JaimeAI2 > ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        tokens = lex(line)
        print(tokens)

if __name__ == "__main__":
    main()
