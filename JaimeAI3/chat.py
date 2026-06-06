import torch
from tokenizer import WordTokenizer, PAD, BOS, EOS, SEP
from model import JaimeTransformer

MAX_LEN = 64

def load_model():
    ckpt = torch.load("jaimeai3.pt", map_location="cpu")
    vocab = ckpt["vocab"]
    tok = WordTokenizer(vocab=vocab)
    vocab_size = len(vocab)
    model = JaimeTransformer(vocab_size=vocab_size, max_len=MAX_LEN, pad_idx=tok.stoi[PAD])
    model.load_state_dict(ckpt["model"])
    model.eval()
    return tok, model

@torch.no_grad()
def generate(tok, model, prompt, max_len=64):
    device = next(model.parameters()).device

    # decoder-only prompt: <bos> user <sep>
    text = f"{BOS} {prompt} {SEP}"
    ids = tok.encode(text, add_bos=False, add_eos=False, max_len=None)
    x = torch.tensor(ids, dtype=torch.long, device=device).unsqueeze(0)

    for _ in range(max_len):
        logits = model(x)  # [1, T, V]
        next_id = logits[0, -1].argmax().item()

        if next_id == tok.stoi[EOS]:
            break

        x = torch.cat([x, torch.tensor([[next_id]], device=device)], dim=1)
        if x.size(1) >= max_len:
            break

    return tok.decode(x[0].tolist())

def main():
    tok, model = load_model()
    while True:
        try:
            user = input("You > ").strip()
        except EOFError:
            break
        out = generate(tok, model, user, max_len=MAX_LEN)
        print("JaimeAI3 >", out)

if __name__ == "__main__":
    main()
