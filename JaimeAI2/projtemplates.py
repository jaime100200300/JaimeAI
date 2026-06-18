import random


def newTemplates():
    random.seed()

htmlrandom = random.choice([
    r"""

<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>JaimeAI2 Mini Chaos Site</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0a0a0f;
            color: #eee;
            overflow-x: hidden;
        }

        header {
            padding: 1rem 2rem;
            background: #11111a;
            border-bottom: 1px solid #222;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .orb {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: radial-gradient(circle at 30% 30%, #ff7bff, #6b00ff);
            box-shadow: 0 0 12px #b300ff;
        }

        .title {
            font-size: 1.2rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }

        .status {
            font-size: 0.8rem;
            color: #9aa;
        }

        .container {
            padding: 2rem;
            max-width: 900px;
            margin: auto;
        }

        .card {
            background: #14141f;
            border: 1px solid #222;
            border-radius: 0.6rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 0 20px rgba(255,255,255,0.04);
        }

        .card h2 {
            margin-top: 0;
            font-size: 1rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #9cf;
        }

        .terminal {
            background: #0d0d14;
            border: 1px solid #222;
            border-radius: 0.4rem;
            padding: 0.8rem;
            font-family: monospace;
            font-size: 0.9rem;
            line-height: 1.4;
            position: relative;
        }

        .cursor {
            display: inline-block;
            width: 7px;
            height: 1em;
            background: #eee;
            animation: blink 1s infinite steps(2, start);
            margin-left: 2px;
        }

        @keyframes blink {
            0%, 49% { opacity: 1; }
            50%, 100% { opacity: 0; }
        }

        .btn {
            display: inline-block;
            padding: 0.4rem 0.8rem;
            background: #222236;
            border: 1px solid #333;
            border-radius: 0.4rem;
            color: #9cf;
            cursor: pointer;
            margin-top: 0.5rem;
            transition: 0.15s;
        }

        .btn:hover {
            background: #2d2d4a;
            transform: translateY(-2px);
        }

        .log {
            margin-top: 0.6rem;
            font-size: 0.85rem;
            color: #aaa;
        }
    </style>
</head>
<body>

<header>
    <div style='display:flex;align-items:center;gap:0.6rem;'>
        <div class='orb'></div>
        <div class='title'>JaimeAI2</div>
    </div>
    <div class='status'>engine online</div>
</header>

<div class='container'>

    <div class='card'>
        <h2>mini terminal</h2>
        <div class='terminal' id='term'>
            booting JaimeAI2...<br>
            loading modules...<br>
            ready.<br><br>
            jaime@ai2:~$ <span id='input'>_</span><span class='cursor'></span>
        </div>
        <div class='btn' onclick='addLog()'>run random command</div>
    </div>

    <div class='card'>
        <h2>stats</h2>
        <div class='log' id='stats'>
            projects spawned: 0<br>
            who-chants blocked: 0<br>
            chaos level: 7/10<br>
        </div>
    </div>

</div>

<script>
    let projects = 0;
    let whos = 0;

    function addLog() {
        const term = document.getElementById('term');
        const stats = document.getElementById('stats');

        const lines = [
            'thinking...',
            'running internal chaos engine...',
            'compiling gremlin thoughts...',
            'error: too much who who who',
            'generating project...',
            'evaluating 2+2...',
            'parsing unknown command...',
            'activating sarcasm module...'
        ];

        const pick = lines[Math.floor(Math.random() * lines.length)];

        term.innerHTML += 'jaime@ai2:~$ ' + pick + '<br>';

        if (pick.includes('project')) projects++;
        if (pick.includes('who')) whos++;

        stats.innerHTML =
            'projects spawned: ' + projects + '<br>' +
            'who-chants blocked: ' + whos + '<br>' +
            'chaos level: ' + (7 + Math.floor(Math.random()*4)) + '/10<br>';
    }
</script>

</body>
</html>


""", r"""

<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>JaimeAI2 Retro Panel</title>
    <style>
        body {
            margin: 0;
            background: #050510;
            font-family: Arial, sans-serif;
            color: #e0e0ff;
        }

        header {
            padding: 1rem 2rem;
            background: linear-gradient(to right, #120022, #220044);
            border-bottom: 2px solid #330066;
            text-shadow: 0 0 6px #a020f0;
        }

        .title {
            font-size: 1.4rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }

        .container {
            padding: 2rem;
            max-width: 900px;
            margin: auto;
        }

        .panel {
            background: #0d0d1a;
            border: 1px solid #2a0055;
            border-radius: 0.6rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 0 20px rgba(162, 0, 255, 0.25);
        }

        .panel h2 {
            margin-top: 0;
            font-size: 1rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: #c080ff;
        }

        .meter {
            height: 14px;
            background: #1a1a2a;
            border-radius: 999px;
            overflow: hidden;
            margin-top: 0.5rem;
            border: 1px solid #330066;
        }

        .meter-fill {
            height: 100%;
            width: 40%;
            background: linear-gradient(to right, #ff00ff, #ff66ff);
            animation: pulse 2s infinite alternate;
        }

        @keyframes pulse {
            from { width: 30%; }
            to { width: 80%; }
        }

        .terminal {
            background: #0a0a14;
            border: 1px solid #330066;
            border-radius: 0.4rem;
            padding: 0.8rem;
            font-family: monospace;
            font-size: 0.9rem;
            line-height: 1.4;
            height: 180px;
            overflow-y: auto;
        }

        .btn {
            display: inline-block;
            padding: 0.4rem 0.8rem;
            background: #220044;
            border: 1px solid #330066;
            border-radius: 0.4rem;
            color: #e0b0ff;
            cursor: pointer;
            margin-top: 0.6rem;
            transition: 0.15s;
        }

        .btn:hover {
            background: #330066;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>

<header>
    <div class='title'>JaimeAI2 Retro Panel</div>
</header>

<div class='container'>

    <div class='panel'>
        <h2>system load</h2>
        <div class='meter'>
            <div class='meter-fill'></div>
        </div>
        <p style='margin-top:0.6rem;color:#aaa;'>chaos engine warming up...</p>
    </div>

    <div class='panel'>
        <h2>terminal</h2>
        <div class='terminal' id='term'>
            boot sequence initiated...<br>
            loading retro modules...<br>
            ready.<br><br>
        </div>
        <div class='btn' onclick='runCommand()'>run random command</div>
    </div>

</div>

<script>
    function runCommand() {
        const term = document.getElementById('term');

        const lines = [
            'executing neon pulse...',
            'scanning memory banks...',
            'compiling chaos shaders...',
            'rendering retro grid...',
            'checking who who who levels...',
            'spawning virtual project...',
            'evaluating 3+3...',
            'activating purple mode...'
        ];

        const pick = lines[Math.floor(Math.random() * lines.length)];

        term.innerHTML += '> ' + pick + '<br>';
        term.scrollTop = term.scrollHeight;
    }
</script>

</body>
</html>


""", r"""
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>JaimeAI2 Mini Monitor</title>
    <style>
        body {
            margin: 0;
            background: #0b0b12;
            color: #e5e5e5;
            font-family: Arial, sans-serif;
            padding: 1.5rem;
        }

        .box {
            background: #14141f;
            border: 1px solid #222;
            border-radius: 0.5rem;
            padding: 1rem 1.2rem;
            max-width: 500px;
            margin: auto;
            box-shadow: 0 0 14px rgba(255,255,255,0.05);
        }

        h1 {
            margin: 0 0 0.8rem 0;
            font-size: 1.1rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: #9cf;
        }

        .stat {
            margin-bottom: 0.6rem;
            font-size: 0.9rem;
        }

        .bar {
            height: 10px;
            background: #1d1d2a;
            border-radius: 999px;
            overflow: hidden;
            border: 1px solid #333;
        }

        .fill {
            height: 100%;
            width: 40%;
            background: linear-gradient(to right, #6b00ff, #bb66ff);
            animation: wiggle 2s infinite alternate;
        }

        @keyframes wiggle {
            from { width: 25%; }
            to { width: 85%; }
        }

        .btn {
            margin-top: 1rem;
            display: inline-block;
            padding: 0.4rem 0.8rem;
            background: #1d1d2a;
            border: 1px solid #333;
            border-radius: 0.4rem;
            cursor: pointer;
            color: #9cf;
            transition: 0.15s;
        }

        .btn:hover {
            background: #26263a;
            transform: translateY(-2px);
        }

        .log {
            margin-top: 0.8rem;
            font-size: 0.85rem;
            color: #aaa;
            min-height: 1rem;
        }
    </style>
</head>
<body>

<div class='box'>
    <h1>jaimeai2 system monitor</h1>

    <div class='stat'>cpu load</div>
    <div class='bar'><div class='fill'></div></div>

    <div class='stat' style='margin-top:0.8rem;'>status log</div>
    <div class='log' id='log'>waiting...</div>

    <div class='btn' onclick='updateLog()'>update</div>
</div>

<script>
    function updateLog() {
        const log = document.getElementById('log');

        const msgs = [
            'running diagnostics...',
            'checking chaos levels...',
            'optimizing gremlin cores...',
            'cleaning memory dust...',
            'evaluating 7+7...',
            'scanning for who who who...',
            'boosting neon output...',
            'stabilizing engine... maybe'
        ];

        const pick = msgs[Math.floor(Math.random() * msgs.length)];
        log.textContent = pick;
    }
</script>

</body>
</html>

"""])
mdrandom = random.choice([

    r"""
# JaimeAI2 Markdown Report

Generated automatically by the chaos-driven project engine.

---

## 📘 Project Summary

**Project Type:** Markdown  
**Generated By:** JaimeAI2  
**Mode:** chaos  
**Status:** operational  

This file documents the internal behavior of the JaimeAI2 engine during a simulated session.

---

## 🧠 Engine Capabilities

- Custom command language  
- Stateful question system  
- Randomized decision maker  
- Project generator (html, txt, md)  
- Sarcastic unknown-command handler  
- Tiny REPL simulation  

---

## 🧪 Example Session

Below is an example of how JaimeAI2 behaves during normal operation.

    JaimeAI2 > make project
    JaimeAI2: Which kind?

    JaimeAI2 > md
    JaimeAI2: Generated a MD project in jaimeaiprojects/

    JaimeAI2 > solve 3+3
    The answer is 6

    JaimeAI2 > who is jaime
    legend says jaime is a chaos dev.

---

## 🔧 Internal Notes

- The parser does **not** know about questions.  
- The engine uses a flag called `self.isAsking`.  
- When `self.isAsking` is true, the next input is treated as an **answer**, not a command.  
- This allows multi-step interactions like:
  - asking what kind of project to generate  
  - waiting for the user to answer  
  - generating the correct file  

---

## 📂 Example Project Directory

    jaimeaiprojects/
    ├─ project_1234.html
    ├─ project_9001.txt
    └─ project_7777.md

---

## 📝 Future Ideas

- Add more project templates  
- Add a `help` command  
- Add a `history` command  
- Add a `mode` switch (normal / chaos / dev)  
- Add more sarcastic responses  

---

_Generated by JaimeAI2 • chaos level: 11/10_
""", r"""

# JaimeAI2 Status Sheet

Auto-generated by the JaimeAI2 engine.  
Mode: chaos • Confidence: questionable • Vibes: immaculate

---

## 🔍 Overview

This document was created as part of a randomized project generation sequence.  
It contains a snapshot of JaimeAI2's internal state at the moment of creation.

---

## 📊 Engine Stats

- parser mood: stable  
- lexer mood: confused  
- engine mood: chaotic neutral  
- who-chants blocked: 1  
- solve operations executed: 3  
- unknown commands roasted: infinite  

---

## 🧪 Sample Output Log

    JaimeAI2 > think
    thinking... decided: solve 5+5, running: The answer is 10

    JaimeAI2 > who is jaime
    scrollwaves whisper: jaime is a chaos dev

    JaimeAI2 > run echo hello
    hello
    Finished running, runned successfully.

---

## 🧠 Internal Notes

- The parser still does not know about questions.  
- The engine still pretends it does.  
- `self.isAsking` continues to be the entire brain.  
- Unknown commands will always be met with sarcasm.  
- Project generation is 40% logic, 60% vibes.

---

## 📝 TODO (Automatically Suggested)

- add more templates  
- add more chaos  
- add more who-chants protection  
- maybe fix something? (unlikely)

---

Generated by **JaimeAI2**  
Chaos level: **11/10**  


"""

])


textrandom = random.choice([

r"""


JaimeAI2 status report
engine: online
chaos: stable
vibes: maximum

""",

r"""
booting jaimeai2...
loading modules...
done.

""",
r"""
remember:
jaime is a chaos dev.

"""
])

pythonrandom = random.choice([
    """# Chaos Insult Generator
    import random

    insults = [
        "bro your code has 3 braincells",
        "you debug like a confused potato",
        "skill issue detected",
        "your syntax is crying",
        "you summoned a bug demon",
        "Yo head lookin like a deformed tomato who been left on la highway for 3 years, ran over by 34 cars, and brutally stepped on 45 times.",
        "bro your code running on 2fps",
        "you type like your keyboard is allergic to you",
        "your indentation is a war crime",
        "your variables look like they were named by a confused squirrel",
        "your logic flow fell down the stairs",
        "your code smells like expired spaghetti",
        "you debug like you're guessing lottery numbers",
        "your functions have commitment issues",
        "your syntax ran away and filed a restraining order",
        "your code is held together by hopes and prayers",
        "you program like a microwave with brain damage",
        "your IDE is begging you to stop",
        "your code is so cursed even demons said 'nah'",
        "your loops loop back to shame",
        "your code has more issues than a soap opera",

    ]

    print(random.choice(insults))
    """,
    """# dice_roller
import random
print("You rolled:", random.randint(1, 6))
""",
"""# coin_flip
import random
print(random.choice(["Heads", "Tails"]))
""",
"""# password_gen
import random, string
chars = string.ascii_letters + string.digits
print("Password:", "".join(random.choice(chars) for _ in range(12)))
""",
"""# mini_calc
expr = input("Enter math: ")
print("Result:", eval(expr))
""",
"""# random_color
import random
print("RGB:", random.randint(0,255), random.randint(0,255), random.randint(0,255))
""",
"""# silly_bot
import random
responses = [
    "bro what",
    "nahhh try again",
    "skill issue",
    "I am a toaster",
    "processing... nope"
]
while True:
    input("> ")
    print(random.choice(responses))
""",
"""# guess_game.py
import random
secret = random.randint(1, 20)
guess = int(input("Guess 1-20: "))
if guess == secret:
    print("YOU WIN 🎉")
else:
    print("Nope, it was", secret)
""",
"""# ascii_art
arts = [
    "(•_•)",
    "( •_•)>⌐■-■",
    "(⌐■_■)",
    "ʕ•ᴥ•ʔ",
    "(╯°□°）╯︵ ┻━┻"
]
import random
print(random.choice(arts))
""",
"""# hacker_typer.py
import time, random
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for _ in range(200):
    print(random.choice(chars), end="", flush=True)
    time.sleep(0.02)
"""
])