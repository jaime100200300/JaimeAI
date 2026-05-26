# engine.py

from nodes import *

class Engine:
    def run(self, node):
        # SolveNode
        if isinstance(node, SolveNode):
            return self.run_solve(node)

        # UnknownNode
        if isinstance(node, UnknownNode):
            return f"Unknown: {node.text}"

        return "Unknown node type"

    def run_solve(self, node: SolveNode):
        # join tokens into a Python expression
        expr = "".join(node.expr)

        try:
            result = eval(expr)
            return f"The answer is {str(result)}"
        except Exception as e:
            return f"Error: {e}"
