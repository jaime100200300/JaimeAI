import random
import sys
import time

def slow(msg, min_delay=0.01, max_delay=0.1):
    i = 0
    length = len(msg)

    while i < length:
        chunk_size = random.randint(1, 4)
        chunk = msg[i:i+chunk_size]
        i += chunk_size

        sys.stdout.write(chunk)
        sys.stdout.flush()

        # punctuation pause
        if chunk and chunk[-1] in ".!?":
            time.sleep(max_delay * 2.5)
        else:
            time.sleep(random.uniform(min_delay, max_delay))

    sys.stdout.write("\n")
    sys.stdout.flush()
