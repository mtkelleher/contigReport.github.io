import argparse

parser = argparse.ArgumentParser(description = 'This program generates a report from a contig assembly. \n'
                                 'An input filename for the contig assembly in FASTA format is required. \n'
                                 'A text file is output with the number of contigs, total length in bp, \n'
                                 'largest contig, and N50 value. Argument for output filename is optional. \n'
                                 'The default output filename is contigReport.txt')
parser.add_argument('inputFile', type = str, help = 'Input filename')
parser.add_argument('-o','--outputFile', type = str, required = False, help = 'Output filename.')
args = parser.parse_args() #Parses input arguments from command line

with open(args.inputFile) as data: #Takes input file from argument and opens as data
    lines = data.readlines() #Reads and stores lines as lines

totalbp = 0 #Tracks of total base pairs by adding lengths of contigs
N50totals = 0 #Tracks track of adding contigs to get greater than or equal to half of total bp
N50iteration = 0 #Tracks iterations for N50 while loop
contig = ''
contigLengths = [] #List of contigs lengths
reportName = 'contigReport.txt' #Default report name

for i in lines:
    if i.startswith('>'): #For FASTA format from contigs assembly these are node labels for the contigs
        if contig != '':
            contigLengths.append(len(contig)) #Appends length of contigs to contigLengths
            totalbp += len(contig) #Adds contig lengths to totalbp tracker
            contig = ''
    else:
        contig += i.rstrip()

contigLengths.append(len(contig)) #Appends for last contig
totalbp += len(contig) #Adds length for last contig

contigLengths.sort(reverse = True) #Sorts contig lengths from largest to smallest

while N50totals <= totalbp/2: #While loop that adds contig lengths until greater than or equal to half of totalbp
    N50totals += contigLengths[N50iteration]
    N50iteration += 1

numContigs = len(contigLengths) #Number of contigs
largestContig = contigLengths[0] #First contig in contigLengths is longest
N50 = contigLengths[N50iteration - 1] #N50 contig length

s = f'{"# contigs":<15}{numContigs:>10}' #Formatted strings for output report
s1 = f'{"Total length":<15}{totalbp:>10}'
s2 = f'{"Largest contig":<15}{largestContig:>10}'
s3 = f'{"N50":<15}{N50:>10}'

if args.outputFile != None: #If user specifies -o argument and gives an output filename
    reportName = args.outputFile

with open(reportName, 'w') as output: #Writes formatted strings to output txt file
    output.write(s + '\n')
    output.write(s1 + '\n')
    output.write(s2 + '\n')
    output.write(s3 + '\n')

