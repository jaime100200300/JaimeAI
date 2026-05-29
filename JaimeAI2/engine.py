# engine.py

from nodes import *
from nodesq import *
import random, os
from lexer import lex
from parser import Parser
from printing import *
import projtemplates

class Engine:

    def __init__(self):
        self.dictionary = {}
        self.isAsking = False

    def generate_project(self, kind):

        projtemplates.newTemplates()

        kind = kind.lower().strip()

        # allowed types
        templates = {
            "html": projtemplates.htmlrandom,
            "txt": projtemplates.textrandom,
            "md": projtemplates.mdrandom
        }

        # if unknown → error message
        if kind not in templates:
            return f"Unknown project type '{kind}'. Allowed: html, txt, md."

        # 1. Create the directory if it doesn't exist
        folder = "jaimeaiprojects"
        os.makedirs(folder, exist_ok=True)

        # 2. Generate filename
        filename = f"project_{random.randint(1000,9999)}.{kind}"
        full_path = os.path.join(folder, filename)

        # 3. Write file
        with open(full_path, "w") as f:
            f.write(templates[kind])

        return f"Generated a {kind.upper()} project: {full_path}"

    def runOneNode(self, node):
        if not self.isAsking:
            # SolveNode
            if isinstance(node, SolveNode):
                return self.run_solve(node)
            
            if isinstance(node, MakeProjectNode):
                self.isAsking = True

                if node.subject:
                    return self.generate_project(node.subject)

                return "Hm.. Which kind of project?"
            
            if isinstance(node, MakeWhatNode):
                return random.choice([
                    "Make WHAT bro?",
                    "Make... what exactly?",
                    "You said make but like… make WHAT?",
                    "Make what dude??",
                    "Make WHAT??? I need details man",
                ])


            # UnknownNode
            if isinstance(node, UnknownNode):

                unknown_lines = [
                    "bro what even IS that",
                    "Unknown command detected. I’m scared.",
                    "I have NO idea what '{}' means.",
                    "???",
                    "my brain just blue‑screened at '{}'",
                    "that command is illegal in 47 states",
                    "I refuse to parse '{}'",
                    "I tried. I failed. '{}'",
                    "Unknown. Chaos intensifies.",
                    "idk what '{}' is but ok",
                    "bro you summoned a demon with '{}'",
                    "Unknown: I rolled a nat‑1 on comprehension with '{}'.",
                ]

                line = random.choice(unknown_lines)
                return line.format(node.text)

            
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

                    lines = [
                        "{} is {}",
                        "I think {} means {}",
                        "pretty sure {} is {}",
                        "uhhh {} = {} ???",
                        "the scrollwaves whisper: {} is {}",
                        "legend says {} is actually {}",
                        "chaos reports that {} is {}",
                        "my brain decided {} is {}",
                    ]

                    fmt = random.choice(lines)
                    return fmt.format(thing, self.dictionary[thing])

                # unknown → funny fallback

                lines = [
                    "I don't know who {} is.",
                    "never heard of {} in my life.",
                    "{}?? who dat.",
                    "bro I genuinely have no clue who {} is.",
                    "scrollwaves whisper nothing about {}.",
                    "my brain returns NULL for {}.",
                    "{} is a mystery wrapped in confusion.",
                    "I searched the chaos dimension and found no {}.",
                    "idk who {} is but they sound suspicious.",
                    "??? {} ???",
                ]

                return random.choice(lines).format(thing)

            
            if isinstance(node, StopChantingWhoNode):

                lines = [
                    "Stop chanting 'WHO WHO WHO', dude.",
                    "BRO STOP THE WHO‑CHANTING.",
                    "ENOUGH WITH THE WHO WHO WHO.",
                    "my ears cannot handle more WHO WHO WHO.",
                    "WHO WHO WHO detected. shutting it down.",
                    "pls stop chanting WHO WHO WHO.",
                    "bro you sound like an owl on caffeine.",
                    "WHO WHO WHO??? NO. STOP.",
                    "the council forbids more WHO chanting.",
                    "I swear if you WHO WHO WHO again—",
                ]

                return random.choice(lines)

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
                return f"FInished running, {'An error, i think.' if code != 0 else 'runned successfully.'}"
            
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
            
            if isinstance(node, HelloNode):
                lines = [
                    "YOOO 😎🔥",
                    "ayooo what’s good",
                    "bro slid into the chat like 👀",
                    "yo yo yo",
                    "sup lil gremlin",
                    "heyyyyy dude",
                    "YOOOOO USER IN THE BUILDING",
                    "wassup my chaotic entity",
                    "yo bro I just spawned",
                    "HELLO??? yes hi I exist",
                    "yo dude I’m literally right here",
                    "bro said hello like an NPC",
                    "hey hey hey what’s poppin",
                    "yo I woke up for this",
                    "sup dude I’m alive again",
                    "YOOOOOOO WHAT’S UP BROOOO",
                ]

                return random.choice(lines)
            
            


            lines = [
                "Unknown node type.",
                "bro this node is from another dimension.",
                "I looked at this node and my brain said 'nope'.",
                "this node type is ILLEGAL.",
                "I cannot comprehend this cursed node.",
                "unknown node detected. send help.",
                "what IS this node supposed to be.",
                "my parser just fainted looking at this node.",
                "node type: ???",
                "chaos reports: unknown node.",
            ]

            return random.choice(lines)
        else:
            self.isAsking = False
            if isinstance(node, AnswerHtmlNode):
                return self.generate_project("html")
            
            if isinstance(node, AnswerMdNode):
                return self.generate_project("md")
            
            if isinstance(node, AnswerPythonNode):
                return self.generate_project("python")
            
            if isinstance(node, AnswerTxtNode):
                return self.generate_project("txt")
            
            if isinstance(node, AnswerAnythingNode):
                choice = random.choice([
                    "html",
                    "md",
                    "python",
                    "txt"
                ])

                return self.generate_project(choice)
            return "I don't think that answered my question."

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


    def main(self):
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
            response = self.run(ast)

            slow(response)
