import json
import torch
from torch.utils.data import Dataset, DataLoader
from tokenizer import WordTokenizer, BOS, EOS, SEP

class SFTDataset(Dataset):
    def __init__(self, json_path, tokenizer, max_len=64):
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.pairs = [(d["user"], d["assistant"]) for d in data]
        self.tok = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, idx):
        user, assistant = self.pairs[idx]
        # one decoder-only sequence
        full = f"{BOS} {user} {SEP} {assistant} {EOS}"
        x = torch.tensor(
            self.tok.encode(full, add_bos=False, add_eos=False, max_len=self.max_len),
            dtype=torch.long
        )
        return x

def make_dataloader(json_path, max_len=64, batch_size=16):
    tok = WordTokenizer()
    tok.build_from_json(json_path)
    ds = SFTDataset(json_path, tok, max_len=max_len)
    dl = DataLoader(ds, batch_size=batch_size, shuffle=True)
    return tok, dl
