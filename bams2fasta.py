from sys import argv
from Bio import SeqIO
import re
import os

script, directory, out_file= argv
output_file=open("%(out_file)s.fa" %locals(), 'a')

for root, dirs, files in os.walk(directory):
        for file in files:
                match=re.match(".*bam$",file)
                if match:
                        name=re.sub( ".bam$", '', file)
                        sample_fasta=SeqIO.parse(open("%(directory)s/%(name)s.fa" %locals()), 'fasta')
                        SeqIO.write(sample_fasta,out_file, 'fasta')
