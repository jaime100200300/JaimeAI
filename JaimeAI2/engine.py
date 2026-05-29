# engine.py

from nodes import *
import random, os
from lexer import lex
from parser import Parser

class Engine:

    def __init__(self):
        self.dictionary = {}

    def runOneNode(self, node):
        # SolveNode
        if isinstance(node, SolveNode):
            return self.run_solve(node)

        # UnknownNode
        if isinstance(node, UnknownNode):
            return f"Unknown: {node.text}"
        
        if isinstance(node, WhoIsNode):
            thing = node.thing

            # no input
            if thing is None or thing.strip() == "":
                return random.choice([
                    "Who what?",
                    "Who WHAT?",
                    "Who is what?",
                    "Who is WHAT?"
                ])

            # known?
            if thing in self.dictionary:
                return f"{thing} is {self.dictionary[thing]}"

            # unknown → funny fallback
            return f"I don't know who {thing} is."
        
        if isinstance(node, StopChantingWhoNode):
            return "Stop chanting 'WHO WHO WHO', dude."
        if isinstance(node, RunCommandNode):
            inner = node.command

            # Try to interpret internally
            tokens = lex(inner)
            ast = Parser(tokens).parse()

            # If parser produced something meaningful → run AI command
            if not (len(ast) == 1 and isinstance(ast[0], UnknownNode)):
                return self.run(ast)

            # Otherwise → fallback to OS shell
            code = os.system('echo ""\n' + inner)
            return f"FInished running, {'An error, i think.' if code != 0 else 'Runned successfully.'}"
        
        if isinstance(node, ThinkNode):

            options = [
                "solve 1+1",
                "solve 2+2",
                "who who who",
                "run echo hello",
                "run ls",
                "solve 3+3",
                "who is jaime",
                "solve 5+5"
            ]

            decision = random.choice(options)
            return (f"thinking... decided: {decision}, running: {self.run(Parser(lex(decision)).parse())}")


        return "Unknown node type"

    def run(self, node):
        # list of nodes → run each
        if isinstance(node, list):
            results = []
            for n in node:
                results.append(self.runOneNode(n))
            # join with ", and " but KEEP full sentences
            return ", and ".join(results)

        # single node
        return self.runOneNode(node)

    def run_solve(self, node: SolveNode):
        expr = "".join(node.expr)

        try:
            result = eval(expr)
            return f"The answer is {result}"
        except Exception as e:
            return f"Error: {e}"
