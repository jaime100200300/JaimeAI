import re

def joiner(text: str) -> str:
    # Remove spaces BEFORE punctuation
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)

    # Collapse multiple spaces into one
    text = re.sub(r"\s+", " ", text)

    # Trim leading/trailing spaces
    return text.strip()
