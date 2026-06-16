import re

def joiner(text: str) -> str:

    # Collapse multiple spaces into one
    return re.sub(r"\s+", " ", re.sub(r"\s+([.,!?;:])", r"\1", text)).strip()
