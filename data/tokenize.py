import numpy as np
import tiktoken


def tokenize_txt_tiktoken(text_file: str, out_filename: str = "train.bin"):
    """Tokenize txt file with tiktoken gpt2 tokenizer"""
    tokenizer = tiktoken.get_encoding("gpt2")
    first_save = True
    with open(text_file) as f:
        while True:
            data = f.read(10**9)
            if not data:
                break
            input_ids = np.array(tokenizer.encode(data)).astype(np.uint16)
            if first_save:
                np.save(out_filename, input_ids)
                first_save = False
            else:
                with open(out_filename, "ab") as out_file:
                    np.save(out_file, input_ids)
    return True
