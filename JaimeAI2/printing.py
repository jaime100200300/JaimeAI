import sys, time, random

def status(msg):
    out = ""
    i = 0
    while i < len(msg):
        burst = random.randint(1, 3)
        out += msg[i:i+burst]
        i += burst

        sys.stdout.write("\r" + " " * 80 + "\r")  # clear line
        sys.stdout.write(out)
        sys.stdout.flush()

        time.sleep(0.05)

    sys.stdout.write("\n")
    sys.stdout.flush()



def slow(msg):
    """Cross‑platform AI‑style typing animation."""
    sys.stdout.write("\r" + " " * 80 + "\r")
    sys.stdout.flush()

    i = 0
    length = len(msg)

    while i < length:
        burst = random.randint(1, 4)
        chunk = msg[i:i+burst]
        i += burst

        # print chunk
        sys.stdout.write(chunk)
        sys.stdout.flush()

        # micro‑pauses
        delay = random.uniform(0.01, 0.03)
        last = chunk[-1]

        if last in ".!?":
            delay += random.uniform(0.05, 0.10)
        elif last in ",;:":
            delay += random.uniform(0.02, 0.05)
        elif last == " ":
            delay += random.uniform(0.005, 0.015)

        # occasional stall
        if random.random() < 0.3:
            delay += random.uniform(0.05, 0.12)

        time.sleep(delay)

    sys.stdout.write("\n")
    sys.stdout.flush()
