# contigReport
This stand-alone Python program generates a report from a contig file in FASTA format.

The report generated is a text file that contains:
* Number of contigs
* Total length in base pairs
* Largest contig
* N50 value

## Requirements and installation
Must have Python3 and download contigReport.py to run.

## Usage
python3 myquast.py test_data/contigs_1.fasta \
        -o quast_test_output (optinal for output directory)
        -h (showing usage)

## Input
An input filename for the contig assembly in FASTA format is required. Argument for output filename is optional.

## Output
The report is a text file that contains the number of contigs, total length in base pairs, largest contig, and N50 value. The default output filename is contigReport.txt.
