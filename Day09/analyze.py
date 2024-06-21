import argparse
from Bio import SeqIO

def find_longest_duplicate(sequence):
    longest_subseq = ""
    seq_length = len(sequence)
    for i in range(seq_length):
        for j in range(i + len(longest_subseq) + 1, seq_length):
            if sequence[i:j] in sequence[j:]:
                longest_subseq = sequence[i:j]
    return longest_subseq

def find_longest_gc_sequence(sequence):
    max_gc_length = 0
    max_gc_seq = ""
    current_gc_length = 0
    current_gc_seq = ""

    for base in sequence:
        if base in ['G', 'C']:
            current_gc_seq += base
            current_gc_length += 1
            if current_gc_length > max_gc_length:
                max_gc_length = current_gc_length
                max_gc_seq = current_gc_seq
        else:
            current_gc_seq = ""
            current_gc_length = 0

    return max_gc_seq

def main():
    parser = argparse.ArgumentParser(description='Analyze sequence files for certain features.')
    parser.add_argument('file', help='Path to the sequence file')
    parser.add_argument('--duplicate', action='store_true', help='Find the longest duplicate sub-sequence')
    parser.add_argument('--gc_sequence', action='store_true', help='Find the longest GC-rich sequence')
    args = parser.parse_args()

    # Read the sequence file
    with open(args.file, 'r') as file:
        for record in SeqIO.parse(file, "fasta"):
            sequence = str(record.seq)

            if args.duplicate:
                longest_dup = find_longest_duplicate(sequence)
                print(f"Longest duplicate sub-sequence: {longest_dup}")

            if args.gc_sequence:
                longest_gc_seq = find_longest_gc_sequence(sequence)
                print(f"Longest GC-rich sequence: {longest_gc_seq}")

if __name__ == "__main__":
    main()
