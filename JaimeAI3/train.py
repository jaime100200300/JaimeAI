import torch
import torch.nn as nn
from data import make_dataloader
from model import JaimeTransformer
from tokenizer import PAD

JSON_PATH = "jaimeai3_sft.json"
MAX_LEN = 64
BATCH_SIZE = 16
EPOCHS = 20
LR = 1e-3

def main():
    tok, dl = make_dataloader(JSON_PATH, max_len=MAX_LEN, batch_size=BATCH_SIZE)
    vocab_size = len(tok.itos)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = JaimeTransformer(vocab_size=vocab_size, max_len=MAX_LEN, pad_idx=tok.stoi[PAD]).to(device)

    opt = torch.optim.Adam(model.parameters(), lr=LR)
    loss_fn = nn.CrossEntropyLoss(ignore_index=tok.stoi[PAD])

    model.train()
    for epoch in range(EPOCHS):
        total = 0.0
        for x in dl:  # now only x
            x = x.to(device)  # [B, T]

            logits = model(x)  # [B, T, V]

            # predict token[t+1] from token[t]
            loss = loss_fn(
                logits[:, :-1].reshape(-1, vocab_size),
                x[:, 1:].reshape(-1)
            )

            opt.zero_grad()
            loss.backward()
            opt.step()

            total += loss.item()
        print(f"epoch {epoch} loss {total / len(dl):.4f}")

    torch.save({"model": model.state_dict(), "vocab": tok.itos}, "jaimeai3.pt")

if __name__ == "__main__":
    main()
