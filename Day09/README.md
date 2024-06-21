# Sequence Analysis Tool

This tool analyzes sequence files in Fasta format to find certain features within the sequences.

## Features

- Find the longest sub-sequence that appears at least twice (`--duplicate`).
- Find the longest GC-rich sequence (`--gc_sequence`).

## Requirements

This tool requires Biopython. Install the necessary dependencies with:

```
pip install -r requirements.txt

```

## Usage

To analyze a sequence file, run:

```
python analyze.py FILE --duplicate --gc_sequence

```

