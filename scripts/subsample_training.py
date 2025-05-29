import argparse
import random

def subsample_parallel(src_file, trg_file, output_prefix, num_samples):
    # Read input files
    with open(src_file, 'r', encoding='utf-8') as f:
        src_lines = f.readlines()
    with open(trg_file, 'r', encoding='utf-8') as f:
        trg_lines = f.readlines()

    assert len(src_lines) == len(trg_lines), "Mismatch in source and target line counts!"

    # Randomly sample indices
    indices = random.sample(range(len(src_lines)), num_samples)

    # Write subsampled files
    src_suffix = src_file.split('.')[-1]
    trg_suffix = trg_file.split('.')[-1]

    with open(f"{output_prefix}.{src_suffix}", 'w', encoding='utf-8') as f_src:
        for i in indices:
            f_src.write(src_lines[i])

    with open(f"{output_prefix}.{trg_suffix}", 'w', encoding='utf-8') as f_trg:
        for i in indices:
            f_trg.write(trg_lines[i])

    print(f"✅ Subsampled {num_samples} sentence pairs to {output_prefix}.{src_suffix} and {output_prefix}.{trg_suffix}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subsample a parallel corpus to a fixed number of sentence pairs.")
    parser.add_argument("src_file", type=str, help="Path to source language file (e.g., train.it-de.it)")
    parser.add_argument("trg_file", type=str, help="Path to target language file (e.g., train.it-de.de)")
    parser.add_argument("output_prefix", type=str, help="Prefix for output files (e.g., train_100k.it-de)")
    parser.add_argument("num_samples", type=int, help="Number of sentence pairs to sample (e.g., 100000)")

    args = parser.parse_args()
    subsample_parallel(args.src_file, args.trg_file, args.output_prefix, args.num_samples)
