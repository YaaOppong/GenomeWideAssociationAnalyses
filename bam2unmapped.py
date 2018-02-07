from sys import argv
import os
import re
from subprocess import Popen, PIPE

def run(cmd, dieOnError=True):
        ps=Popen(cmd, shell=True, stdout=log, stderr=log)
        exitcode=ps.wait()

def getUnmapped(bam_file, in_directory, out_directory, name):
        run("samtools view -f 0x4 %(in_directory)s/%(bam_file)s >  %(out_directory)s/%(name)s.unmapped.sam" %locals())

script, in_directory, out_directory=argv

log=open('log_unmapped.txt', 'a')

for root, dirs, files in os.walk(in_directory):
        for file in files:
                match=re.match(".*bam$",file)
                if match:
                        name=re.sub(".bam$", '', file)
                        getUnmapped(file, in_directory, out_directory, name)

log.flush()
