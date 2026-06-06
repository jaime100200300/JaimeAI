import random
import sys
import time


def slow(msg, min_delay=0.01, max_delay=0.1):
    cursor_frames = ["|", " "]
    frame_time = 0.16
    last_frame_switch = time.time()
    frame = 0

    typed = ""
    i = 0

    while i < len(msg):
        now = time.time()

        if now - last_frame_switch >= frame_time:
            frame = 1 - frame
            last_frame_switch = now

        chunk_size = random.randint(2, 5)
        chunk = msg[i:i + chunk_size]
        typed += chunk
        i += chunk_size

        sys.stdout.write("\r" + typed + cursor_frames[frame])
        sys.stdout.flush()

        if chunk and chunk[-1] in ".!?":
            time.sleep(max_delay * 2.5)
        else:
            time.sleep(random.uniform(min_delay, max_delay))

    sys.stdout.write("\r" + typed + " \n")
    sys.stdout.flush()

