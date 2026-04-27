import random
import time
import math


# Variables

ranswer = random.choice(
    [
        "Bro that math ain’t mathing.",
        "Yeah no, that broke my brain.",
        "Stop with the invalidity.",
        "Stop breaking my brain bro."
    ]
)

kernelamnt = 0
mode = 0

last_message = ""
previous = ""

# Functions

def command(cmd):
    global mode
    
    if cmd == "/lore":
        return "the terminal hums... ancient code awakens."
    
    if cmd == "/meow":
        mode = 1
        return "meow mode activated."
        
    if cmd == "/normal":
        mode = 0
        return "normal mode restored."
    return None
  

def math_mode(expr):
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
        return ranswer


def line():
    print("\n" + "-" * 40 + "\n")


def slow(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.02)
    print()
    
    
# Boot sequence

slow("BOOTING JAIME_AI..")
time.sleep(random.uniform(0.02, 0.1))
print()

for i in range(1, random.randint(4, 7)):
    print(f"starting ai_kernel_{i}")
    time.sleep(random.uniform(0.02, 0.13))
    kernelamnt += 1

print()
slow("starting ai_services")
print()

time.sleep(0.5)

# Name asker
name = input("Hi! What shall I call you? > ").lower().strip()

print()

slow(f"\nHello, {name}! I am JAIME‑AI v0.1.")
slow(f"I don’t know everything, but I can vibe, {name}!")
slow("Be careful how you type on math equations")
slow("or you will get an error.")


time.sleep(0.5)
line()

responses1 = [
    "Interesting... tell me more.",
    "Bro that’s wild.",
    "I didn’t expect that.",
    "Explain that again.",
    "You might be onto something.",
    "That sounds like chaos energy.",
    "I respect it.",
    "Say that one more time but with style.",
    "Yo, idk what your talking about..",
    "Mommy choochoo.",
    "Mommy choochoo.",
]
responses2 = [
    "Bandlab? Say less, that’s music app.",
    "Bandlab spotted… Prepare for latency and music.",
    "Bandlab again? That glitch beast stays hungry.",
    "Bandlab again? That app stays plotting side quests.",
]
responses3 = [
    "MeowLab? Say less, that's the meowing music app.",
    "MeowLab spotted… Prepare for meow and music.",
    "MeowLab again? That meow beast stays hungry.",
    "MeowLab again? That app stays plotting meow quests."
]
# the actual chat
while True:
    user = input("> ").lower().strip()
    previous = last_message
    last_message = user
    
    slow(user)
    if previous != "":
        if user == previous:
            slow("You said that already bro, but")
        elif len(previous) > 20:
            slow("That previous message was kinda long bro, but")
        elif previous.endswith("?"):
            slow("You keep asking things huh, but")
    
    result = command(user)
    if result:
        slow(result)
        continue

    if user in ["bye", "exit", "quit"]:
        # Shutdown sequence
        line()
        slow("Shutting down MEOW_AI..." if mode == 1 else "Shutting down JAIME-AI...")
        print()

        for j in range(1, (kernelamnt + 1)):
            print(f"stopping ai_kernel_{j}")
            time.sleep(random.uniform(0.02, 0.13))

        print()
        slow("stopping ai_services")
        print()

        time.sleep(0.5)
        slow("Bye!")
        break

    elif "chess" in user:
        slow("MeowChess detected. The cathorsemeow is still cracked." if mode == 1 else "Chess detected. The horse is still cracked.")
        continue

    elif "bandlab" in user:
        slow(random.choice(responses3) if mode == 1 else random.choice(responses2))
        continue

    elif "who are you" in user or "hello" in user:
        slow("Meow! I am a tiny Python cat you summoned." if mode == 1 else "Hello, i am a tiny Python AI you summoned.")
        continue

    elif "help" in user:
        slow("commands you can try:")
        slow("- talk about chess")
        slow("- mention bandlab")
        slow("- ask who I am")
        slow("- say hello")
        slow("- do math problems with me")
        slow("- meow at me :)")
        slow("- /meow to activate meow mode")
        slow("- /normal to go back to normal mode")
        slow("- thank me idk")
        slow("- say bye to exit")
        continue

    elif name in user:
        slow("Meow... thats your name..." if mode == 1 else "Yeah... that's your name...")
            
        continue

    elif "math" in user:
        answer = input("Yo, math question?")
        print()
        slow(f"> {answer}")

        if str(math_mode(answer)) == ranswer:
            slow(ranswer)
        else:
            slow("The answer is " + str(math_mode(answer)))

        continue

    elif "meow" in user:
        if mode == 1:
            slow("super suPeR MEOW MODE ACTIVATED")
            slow("MEOW MEOW MEOW MEOW MEOW MEOWW")
            slow("MMMMEEEEOOOOWWWW!!!")
        else:
            slow("MEOW MEOW MEOW MEEEOOOWWW!!")
            slow("I AM CAT!!!")
        continue

    elif "thanks" in user or "thank you" in user:
        slow("uh.. You're welcome!")
        continue

    elif "ok" in user:
        slow("yeah yaayaeyah.. ok.")
        continue
        
    elif "banana" in user or "bananas" in user:
        slow("Banana Banana Bananaa" if mode == 0 else "Meow Banana!!!")
        continue

    else:
        slow(random.choice(responses1) if mode == 0 else "Meow.")