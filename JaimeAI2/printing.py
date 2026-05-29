import time, random, sys

def status(msg):
    print(msg, end="\r")
    time.sleep(random.uniform(0.05, 0.20))

def slow(msg):
    # clear the line
    print(" " * 80, end="\r")

    i = 0
    length = len(msg)

    while i < length:
        # print 2–3 characters at once
        burst = random.randint(1, 3)
        chunk = msg[i:i+burst]

        sys.stdout.write(chunk)
        sys.stdout.flush()

        i += burst

        # natural delay
        time.sleep(random.uniform(0.03, 0.09))

    sys.stdout.write("\n")
