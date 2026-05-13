import datetime
import math

def math_eval(expr):
    expr = expr.strip().lower()
    expr = expr.replace("^", "**")
    

    allowed = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "radians": math.radians,
    }

    try:
        return eval(expr, {"__builtins__": None}, allowed)
    except:
        return "an error."
    


class AI():

    def __init__(self):
        self.definitions = {
            "meanings": {
                "python": "A programming language used to maek me :)",
                "ai": "A system that processes information and generates responses, like me :)",
                "math": "The study of numbers and patterns",
            },
            "people": {
                "jaime": "The creator of me :)"
            }
        }
        self.history = []
        self.potato = -1

    def tokenize(self, src):
        return src.lower().strip().split()
    
    def potato_say(self):
        self.potato += 1
        if self.potato == 0:
            return "I am NOT a potato."
        elif self.potato == 1:
            return "I SAID I AM NOT A POTATO."
        elif self.potato == 2:
            return "STOP CALLING ME A POTATO!!"
        elif self.potato == 3:
            return "FINAL WARNING! NO POTATO."
        elif self.potato >= 4:
            return "You know what fine, call me a potato all you want"
    
    def ask(self, question):
        tokens = self.tokenize(question)

        # --- HELLO COMMAND ---
        if len(tokens) >= 1 and tokens[0] in ("hey", "hello"):
            if len(tokens) >= 2 and tokens[1] == "dude":
                return "Hey dude, how can I help?"
            elif len(tokens) >= 2 and tokens[1] == "bro":
                return "Hey bro, how can I help?"
            return "Hello, how can I help?"
        
        elif len(tokens) >= 1 and tokens[0] in ("wassup", "waddup"):
            if len(tokens) >= 2 and tokens[1] == "dude":
                return "Yo wassup dude how may i help?"
            elif len(tokens) >= 2 and tokens[1] == "bro":
                return "Yo wassup bro how may I help?"
            return "Yo wassuppp"
        
        elif tokens[0] == "bye":
            exit()
            
        elif tokens[0] == "idk":
            return "I get it bro."
        
        elif tokens[0] == "thanks" or tokens[0] == "thank":
            if len(tokens) >= 2 and tokens[1] == "dude":
                return "Yo welcome dude"
            elif len(tokens) >= 2 and tokens[1] == "bro":
                return "Your welcome bro"
            return "Your welcome sir."

        # --- SOLVE COMMAND ---
        elif len(tokens) >= 1 and tokens[0] == "solve":

            # solve the math equation X, solve the math problem X, solve the math question X
            if len(tokens) >= 4 and tokens[1] == "the" and tokens[2] == "math":
                if tokens[3] == "equation":
                    idx = tokens.index("equation")
                    equation = " ".join(tokens[idx+1:])
                    answer = math_eval(equation)
                    return f"The answer is {answer}"
                elif tokens[3] == "problem":
                    idx = tokens.index("problem")
                    equation = " ".join(tokens[idx+1:])
                    answer = math_eval(equation)
                    return f"The answer is {answer}"
                elif tokens[3] == "question":
                    idx = tokens.index("question")
                    equation = " ".join(tokens[idx+1:])
                    answer = math_eval(equation)
                    return f"The answer is {answer}"

            # solve math X
            if len(tokens) >= 3 and tokens[1] == "math":
                idx = tokens.index("math")
                equation = " ".join(tokens[idx+1:])
                answer = math_eval(equation)
                return f"The answer is {answer}"
            
            # solve the math X
            if len(tokens) >= 4 and tokens[1] == "the" and tokens[2] == "math":
                idx = tokens.index("math")
                equation = " ".join(tokens[idx+1:])
                answer = math_eval(equation)
                return f"The answer is {answer}"

            # solve X
            if len(tokens) >= 2:
                equation = " ".join(tokens[1:])
                answer = math_eval(equation)
                return f"The answer is {answer}"

            return "Sorry, I can't understand."
        
        elif tokens[0] == "define":
            if len(tokens) >= 2:
                term = " ".join(tokens[1:])
                if term in self.definitions["meanings"]:
                    return f"{term}: {self.definitions['meanings'][term]}"
                return f"I dont know what {term} means yet."
            return "Define what?"
        
        elif tokens[0] == "who":
            if len(tokens) >= 3 and tokens[1] == "are" and tokens[2] == "you":
                return "I am Jaime AI 2.0, created by Jaime :)"

            elif len(tokens) >= 3 and tokens[1] == "is":
                term = " ".join(tokens[2:])
                if term in self.definitions["people"]:
                    return f"{term}: {self.definitions['people'][term]}"
                return f"I don't know who {term} is."

            return "Who what?"
        
        elif tokens[0] == "what":
            if len(tokens) >= 3 and tokens[1] == "is":
                term = " ".join(tokens[2:])
                if term in self.definitions["meanings"]:
                    return f"{term}: {self.definitions['meanings'][term]}"
                return f"{term} is not in my dictionary."
            
        elif tokens[0] == "history":
            if len(self.history) == 0:
                return "No history yet :)"
            
            lines = []
            for i, (q, a) in enumerate(self.history, start=1):
                lines.append(f"{i}. {q} -> {a}")

            return "\n".join(lines)
        
        elif tokens[0] == "clear" and len(tokens) >= 2 and tokens[1] == "history":
            self.history = []
            return "History cleared."
        
        elif tokens[0] == "repeat":
            if len(tokens) >= 3 and tokens[1] == "after" and tokens[2] == "me":
                phrase = " ".join(tokens[3:])
                return phrase
            elif tokens[1] != "after":
                return " ".join(tokens[1:])
            return "Repeat what!?"
        
        elif tokens[0] == "remember":
            if len(tokens) >= 4:
                category = tokens[1]
                term = tokens[2]
                meaning = " ".join(tokens[3:])

                if category == "person":
                    self.definitions["people"][term] = meaning
                    return f"Okay, I'll remember {term} :)"
                elif category == "meaning":
                    self.definitions["meaning"][term] = meaning
                    return f"Got it. {term} is now part of my lore."
                
                else:
                    return "Unknown category. Use 'person' or 'meaning'"
                
            return "Remember what?"
        
        elif tokens[0] == "forget":
            if len(tokens) >= 3:
                category = tokens[1]
                term = tokens[2]

                if category == "person":
                    if term in self.definitions["people"]:
                        del self.definitions["people"][term]
                        return f"I forgot {term}."
                    return f"I don't know that person."

                elif category == "meaning":
                    if term in self.definitions["meanings"]:
                        del self.definitions["meanings"][term]
                        return f"I forgot the meaning of {term}."
                    return f"I don't know that meaning."

                else:
                    return "Unknown category. Use 'person' or 'meaning'."

            return "Forget what?"
        
        elif tokens[0] == "help":
            return (
                "Available commands:\n"
                "- hello / hey\n"
                "- solve <expression>\n"
                "- define <term>\n"
                "- what is <term>\n"
                "- who are you\n"
                "- who is <name>\n"
                "- remember person <name> <desc>\n"
                "- remember meaning <term> <desc>\n"
                "- forget person <name>\n"
                "- forget meaning <term>\n"
                "- repeat after me <phrase>\n"
                "- history\n"
                "- clear history\n"
                "- call me a potato but please dont\n"
                "- say 'be potato' for me to be a potato but i dont want to PLEASE"
            )
        
        elif tokens[0] == "list" and len(tokens) >= 2 and tokens[1] == "people":
            if len(self.definitions["people"]) == 0:
                return "I don't know any people yet."
            
            lines = ["People I know:"]
            for name in self.definitions["people"]:
                lines.append(f"- {name}")
            return "\n".join(lines)
        
        elif tokens[0] == "list" and len(tokens) >= 2 and tokens[1] == "meanings":
            if len(self.definitions["meanings"]) == 0:
                return "I don't know any meanings yet."
                
            lines = ["Meanings I know:"]
            for term in self.definitions["meanings"]:
                lines.append(f"- {term}")
            return "\n".join(lines)
        
        elif tokens[0] == "version":
            return "v2.0"
        
        elif tokens[0] == "whats" and len(tokens) >= 3 and tokens[1] == "the":
            if tokens[2] == "time":
                now = datetime.datetime.now()
                return now.strftime("%H:%M:%S")

            if tokens[2] == "date":
                today = datetime.date.today()
                return today.strftime("%Y-%m-%d")

            return "Whats the what?"
        
        elif tokens[0] == "potato":
            return self.potato_say()
        
        elif tokens[0] == "be":
            if tokens[1] == "potato":
                return "Fine--I'm.... a potato.😭"
            return "Be a what?"

        elif tokens[0] == "how":
            if tokens[1] == "are" and tokens[2] == "you":
                return "I am good, how are you?"
            return "How what?"

        elif tokens[0] == "i":
            if tokens[1] == "am" and tokens[2] == "good":
                return "Nice."
            return "You what?"

        return "Command not recognized."
    
    def ask_history(self, question):
        response = self.ask(question)
        if not (question.startswith("history") or question.startswith("clear history")):
            self.history.append((question, response))

        return response
        


if __name__ == "__main__":
    ai = AI()
    while True:
        print(ai.ask_history(input("JaimeAI > ")))