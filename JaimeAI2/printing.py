import time
import sys
import random

def slow(msg):
    cursor_frames = ["·", "●"]
    frame_time = 0.5   # cursor switches every 0.5 sec
    last_frame_switch = time.time()
    frame = 0

    typed = ""
    i = 0

    while i < len(msg):
        now = time.time()

        # cursor animation (every 0.5 sec)
        if now - last_frame_switch >= frame_time:
            frame = 1 - frame
            last_frame_switch = now

        # typing happens SLOWER than cursor
        if random.random() < 0.15:  # 15% chance each frame
            chunk_size = random.randint(1, 2)
            chunk = msg[i:i + chunk_size]
            typed += chunk
            i += chunk_size

        # draw line
        sys.stdout.write("\r" + typed + cursor_frames[frame])
        sys.stdout.flush()

        # THIS WAS MISSING
        time.sleep(0.03)

    sys.stdout.write("\n")
    sys.stdout.flush()
