from transformers import GPT2TokenizerFast
import numpy as np


def tokenize_txt(text_file: str, seq_len: int = 500):
    """Tokenize txt file with GPT2 Tokenizer
    
    text_file: filename of the text file
    seq_len: sequence length (txt will be split on " ")
    """
    with open(text_file, "r") as f:
        full_text = f.read()
    split_text = full_text.split(" ")

    sequences = []
    for i in range(0, len(split_text) - seq_len, seq_len):
        sequences.append(" ".join(split_text[i : i + seq_len]))

    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    input_ids = tokenizer(sequences, truncation=True)["input_ids"]
    input_ids = np.concatenate(input_ids).astype(np.uint16).ravel()
    return input_ids
