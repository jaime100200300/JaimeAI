import time, sys, random

def slow(msg):
    for ch in msg:
        sys.stdout.write(ch)
        sys.stdout.flush()

        # tiny random delay per character
        time.sleep(random.uniform(0.03, 0.09))

    sys.stdout.write("\n")
    sys.stdout.flush()
