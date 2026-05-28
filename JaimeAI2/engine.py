# engine.py

from nodes import *

class Engine:

    def runOneNode(self, node):
        # SolveNode
        if isinstance(node, SolveNode):
            return self.run_solve(node)

        # UnknownNode
        if isinstance(node, UnknownNode):
            return f"Unknown: {node.text}"

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
            return f"the answer is {result}"
        except Exception as e:
            return f"Error: {e}"
