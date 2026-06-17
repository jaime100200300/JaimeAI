import random
import sys
import time

def slow(msg, min_delay=0.01, max_delay=0.1, end="\n", min_letters=1, max_letters=4):
    i = 0
    length = len(msg)

    while i < length:
        chunk_size = random.randint(min_letters, max_letters)
        chunk = msg[i:i+chunk_size]
        i += chunk_size

        sys.stdout.write(chunk)
        sys.stdout.flush()

        # punctuation pause
        if chunk and chunk[-1] in ".!?":
            time.sleep(max_delay * 2.5)
        else:
            time.sleep(random.uniform(min_delay, max_delay))

    sys.stdout.write(end)
    sys.stdout.flush()
