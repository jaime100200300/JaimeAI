# engine.py

from nodes import *
from nodesq import *
import random, os, subprocess
from lexer import lex
from parser import Parser
from printing import *   # slow()
import projtemplates
import joiner
import time
from numst import number_to_ordinal_word

class Engine:

    def __init__(self):
        self.dictionary = {
            "python": "A prgoramming language used to make me :)"
        }
        self.isAsking = False
        self.question = None
        self.running = False

    def generate_project(self, kind):

        projtemplates.newTemplates()

        kind = kind.lower().strip()

        templates = {
            "html": projtemplates.htmlrandom,
            "txt": projtemplates.textrandom,
            "md": projtemplates.mdrandom,
            "python": projtemplates.pythonrandom
        }

        if kind not in templates:
            slow(f"Unknown project type '{kind}'. Allowed: html, txt, md, and python.")
            return

        folder = "jaimeaiprojects"
        print("Making folder..")
        os.makedirs(folder, exist_ok=True)

        slow("Generating project: ", end="")
        if (True if (input("Show code? (y/n) > ") == 'y') else False):
            slow("\x1b[100;97m\x1b[1;97m" + templates[kind] + "\x1b[0m", min_letters=10, max_letters=20, min_delay=0.005, max_delay=0.01)

        filename = f"project_{random.randint(1000,9999)}.{'py' if kind == "python" else kind}"
        full_path = os.path.join(folder, filename)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(templates[kind])

        slow(f"Generated a {kind.upper()} project: {full_path}")

    def runOneNode(self, node, idx):
        index, total = idx
        if not self.isAsking:

            if isinstance(node, SolveNode):
                slow(self.run_solve(node, index, total))
                return


            if isinstance(node, MakeProjectNode):
                if node.subject:
                    self.generate_project(node.subject)
                    return

                self.isAsking = True
                self.question = "project_kind"
                slow("Hm.. Which kind of project?")
                return

            if isinstance(node, MakeWhatNode):
                self.handle_makewhat(index, total)
                return



            if isinstance(node, UnknownNode):
                line = random.choice([
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
                ]).format(joiner.joiner(node.text))
                slow(line)
                return

            if isinstance(node, WhoIsNode):
                thing = node.thing

                if not thing or thing.strip() == "":
                    slow(random.choice([
                        "Who what?",
                        "Who WHAT?",
                        "Who is what?",
                        "Who is WHAT?"
                    ]))
                    return

                if thing in self.dictionary:
                    fmt = random.choice([
                        "{} is {}",
                        "I think {} means {}",
                        "pretty sure {} is {}",
                        "uhhh {} = {} ???",
                        "the scrollwaves whisper: {} is {}",
                        "legend says {} is actually {}",
                        "chaos reports that {} is {}",
                        "my brain decided {} is {}",
                    ])
                    slow(fmt.format(thing, self.dictionary[thing]))
                    return

                slow(random.choice([
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
                ]).format(thing))
                return

            if isinstance(node, WaitSecondsNode):
                time.sleep(node.secs)
                slow(f"Successfully waited {node.secs} seconds.")
                return

            if isinstance(node, StopChantingWhoNode):
                slow(random.choice([
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
                ]))
                return

            if isinstance(node, RunCommandNode):
                inner = node.command

                tokens = lex(inner)
                ast = Parser(tokens).parse()

                # If the inner command is a REAL JaimeAI command (SolveNode, MakeNode, etc.)
                if len(ast) == 1 and not isinstance(ast[0], (UnknownNode, OneWordNode)):
                    self.run(ast)
                    return

                # Otherwise treat it as a shell command
                cmd = inner
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                output = (result.stdout + result.stderr).strip()
                status = "An error, i think." if result.returncode != 0 else "runned successfully."

                if output:
                    slow(f"\"{output}\"\nFinished running, {status}")
                else:
                    slow(f"Finished running, {status}")
                return


            if isinstance(node, ThinkNode):
                decision = random.choice([
                    "solve 1+1",
                    "solve 2+2",
                    "who who who",
                    "run echo hello",
                    "run ls",
                    "solve 3+3",
                    "who is jaime",
                    "solve 5+5"
                ])
                slow(f"thinking..., decided: {decision}, running...\n")
                self.run(Parser(lex(decision)).parse())
                slow("\nThinked successfully.")
                return

            if isinstance(node, HelloNode):
                slow(random.choice([
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
                ]))
                return

            if isinstance(node, ByeNode):
                self.running = False
                slow(random.choice([
                    "Cya--bye..",
                    "",
                    "bye dude",
                    "ight peace",
                    "ok bye I guess",
                    "bro just left the chat 💀",
                    "BYE??? already??",
                    "ok fine leave me here alone",
                    "later skater",
                    "goodbye… I’ll just sit here… thinking…",
                    "bye bro don’t summon demons while I’m gone",
                    "ok bye but come back with snacks",
                    "farewell mortal",
                    "bye dude I’m shutting down emotionally",
                    "ok bye I’m gonna roll a nat‑1 without you",
                ]))
                return

            slow(random.choice([
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
            ]))
            return

        else:
            self.answer_question(node)

    def answer_question(self, node):
        if self.question == "project_kind":
            if isinstance(node, OneWordNode):
                self.clear_question()
                self.generate_project(node.word)
                return

            slow("I don't think that answered my question. Try html, md, txt, or anything.")
            return

        self.clear_question()
        slow("I forgot what I was asking.")

    def clear_question(self):
        self.isAsking = False
        self.question = None

    def run(self, node):
        if isinstance(node, list):

            total = len(node)
            index = 0

            for n in node:
                index += 1
                self.runOneNode(n, (index, total))

            return

        self.runOneNode(node, (1, 1))


    def run_solve(self, node: SolveNode, index, total):
        expr = "".join(node.expr)
        try:
            if total == 1:
                return f"The answer is {eval(expr)}"
            else:
                return f"The {number_to_ordinal_word(index)} answer is {eval(expr)}"
        except Exception as e:
            return f"Error: {e}"


    def handle_makewhat(self, index, total):
        if total == 1:
            # Only one make in the whole input
            slow(random.choice([
                "Make WHAT bro?",
                "Make... what exactly?",
                "You said make but like… make WHAT?",
                "Make what dude??",
                "Make WHAT??? I need details man",
            ]))
            return

        # Multiple makes in the same input
        if index == 1:
            slow("Make WHAT bro?")
        elif index == 2:
            slow("Wow. Another 'make' again?")
        elif index == 3:
            slow("BRO STOP MAKING THINGS")
        else:
            slow(f"Bro this is the {index}th make. Seek help.")



    def main(self):
        self.running = True
        while self.running:
            line = input("JaimeAI2 > ")
            tokens = lex(line.lower().strip())
            ast = Parser(tokens).parse()
            self.run(ast)
