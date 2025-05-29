import sys

def clean_vocab(infile, outfile):
    with open(infile, 'r', encoding='utf-8') as fin, open(outfile, 'w', encoding='utf-8') as fout:
        for line in fin:
            # Each line should be: token count
            token = line.strip().split()[0]
            fout.write(token + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_vocab.py input_vocab.txt output_vocab.txt")
        sys.exit(1)

    input_vocab = sys.argv[1]
    output_vocab = sys.argv[2]

    clean_vocab(input_vocab, output_vocab)
    print(f"Cleaned vocab written to {output_vocab}")
