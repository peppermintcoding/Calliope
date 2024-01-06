from transformers import GPT2TokenizerFast
import numpy as np


def tokenize_txt(text_file: str, seq_len: int = 500, out_filename: str = "train.bin"):
    """Tokenize txt file with GPT2 Tokenizer
    
    text_file: filename of the text file
    seq_len: sequence length (txt will be split on " ")
    """
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    first_save = True
    with open(text_file) as f:
        while True:
            data = f.read(10**6)
            if not data:
                break
            split_text = data.split(" ")

            sequences = []
            for i in range(0, len(split_text) - seq_len, seq_len):
                sequences.append(" ".join(split_text[i : i + seq_len]))

            input_ids = tokenizer(sequences, truncation=True)["input_ids"]
            input_ids = np.concatenate(input_ids).astype(np.uint16).ravel()

            if first_save:
                np.save(out_filename, input_ids)
                first_save = False
            else:
                with open(out_filename, "ab") as out_file:
                    np.save(out_file, input_ids)
    return True
