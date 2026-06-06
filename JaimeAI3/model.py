# model.py
import torch
import torch.nn as nn

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=512):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        pos = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div = torch.exp(torch.arange(0, d_model, 2).float() * (-torch.log(torch.tensor(10000.0)) / d_model))
        pe[:, 0::2] = torch.sin(pos * div)
        pe[:, 1::2] = torch.cos(pos * div)
        pe = pe.unsqueeze(0)  # [1, max_len, d_model]
        self.register_buffer("pe", pe)

    def forward(self, x):
        # x: [B, T, D]
        T = x.size(1)
        return x + self.pe[:, :T]

class JaimeTransformer(nn.Module):
    def __init__(self, vocab_size, d_model=128, nhead=4, num_layers=2, dim_ff=256, max_len=64, pad_idx=0):
        super().__init__()
        self.pad_idx = pad_idx
        self.emb = nn.Embedding(vocab_size, d_model, padding_idx=pad_idx)
        self.pos = PositionalEncoding(d_model, max_len=max_len)
        layer = nn.TransformerDecoderLayer(d_model=d_model, nhead=nhead, dim_feedforward=dim_ff, batch_first=True)
        self.decoder = nn.TransformerDecoder(layer, num_layers=num_layers)
        self.fc = nn.Linear(d_model, vocab_size)

    def forward(self, x):
        # x: [B, T] (we'll use it as both "memory" and "target" for simplicity)
        emb = self.emb(x)
        emb = self.pos(emb)

        # causal mask
        T = x.size(1)
        mask = torch.triu(torch.ones(T, T, device=x.device) * float("-inf"), diagonal=1)

        out = self.decoder(tgt=emb, memory=emb, tgt_mask=mask)
        logits = self.fc(out)  # [B, T, V]
        return logits
