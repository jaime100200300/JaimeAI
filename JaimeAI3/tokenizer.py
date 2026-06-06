import json
from collections import Counter

PAD = "<pad>"
BOS = "<bos>"
EOS = "<eos>"
UNK = "<unk>"
SEP = "<sep>"

class WordTokenizer:
    def __init__(self, vocab=None):
        self.special_tokens = [PAD, BOS, EOS, UNK, SEP]
        if vocab is not None:
            self.itos = vocab
            self.stoi = {t: i for i, t in enumerate(self.itos)}
        else:
            self.itos = None
            self.stoi = None

    def build_from_json(self, path, min_freq=1):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        counter = Counter()
        for item in data:
            counter.update(item["user"].split())
            counter.update(item["assistant"].split())

        words = [w for w, c in counter.items() if c >= min_freq]
        self.itos = self.special_tokens + sorted(words)
        self.stoi = {t: i for i, t in enumerate(self.itos)}

    def encode(self, text, add_bos=False, add_eos=False, max_len=None):
        tokens = text.split()
        ids = []
        if add_bos:
            ids.append(self.stoi[BOS])
        for t in tokens:
            ids.append(self.stoi.get(t, self.stoi[UNK]))
        if add_eos:
            ids.append(self.stoi[EOS])

        if max_len is not None:
            ids = ids[:max_len]
            while len(ids) < max_len:
                ids.append(self.stoi[PAD])
        return ids

    def decode(self, ids):
        tokens = []
        for i in ids:
            if i < 0 or i >= len(self.itos):
                continue
            t = self.itos[i]
            if t in (PAD, BOS, EOS, SEP):
                continue
            tokens.append(t)
        return " ".join(tokens)
