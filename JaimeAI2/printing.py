import time, random, sys



def status(msg):
    out = "               \r"
    i = 0
    while i < len(msg):
        burst = random.randint(1, 3)
        out += msg[i:i+burst]
        i += burst
        print(out, end="\r")
        time.sleep(random.uniform(0.02, 0.06))


def slow(msg):
    print(" " * 80, end="\r")

    i = 0
    length = len(msg)

    while i < length:
        # faster bursts, more chaotic
        burst = random.randint(1, 4)
        chunk = msg[i:i+burst]

        sys.stdout.write(chunk + " ●")
        sys.stdout.flush()

        i += burst

        # base speed: FAST
        delay = random.uniform(0.01, 0.03)

        last = chunk[-1]

        # micro‑pauses but TINY
        if last in ".!?":
            delay += random.uniform(0.05, 0.10)   # small pause
        elif last in ",;:":
            delay += random.uniform(0.02, 0.05)   # tiny pause
        elif last == " ":
            delay += random.uniform(0.005, 0.015) # barely noticeable

        # occasional random stall (feels alive)
        if random.random() < 0.3:
            delay += random.uniform(0.05, 0.12)

        time.sleep(delay)

        # erase cursor
        sys.stdout.write("\b\b  \b\b")
        sys.stdout.flush()

    sys.stdout.write("\n")
