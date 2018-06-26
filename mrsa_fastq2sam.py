from sys import argv
from subprocess import Popen, PIPE
import re
import os
import argv

def run(cmd, dieOnError=True):
        ps=Popen(cmd, shell=True, stdout=log, stderr=log)
        exitcode=ps.wait()
       #stdout=ps.stdout.read().rstrip('\n')
       #stderr=ps.stderr.read().rstrip('\n')
        if dieOnError and exitcode !=0:
               raise Exception("run failed."+"cmd:`%(cmd)s` exit: %(exitcode)s" % locals())
               #return (exitcode, stdout, stderr)
        #print exitcode
        #print stdout
        #print stderr


log=open('log.txt', 'a')
filenames=argv[1:]
reference=

path='~/mrsa_singapore'
for root, dirs, files in os.walk(directory):
  for dir in dirs:
    for filename in dir:
    name=re.sub(".h5", "", dir)
    if name== :
        log.write('\n%(name)s\n' %locals())
        run("java -jar /usr/local/bin/trimmomatic-0.32.jar PE -phred33 %(path)s/%(dir)s/%(name)s_R1.fastq.gz %(path)s/%(dir)s/%(name)s_R2.fastq.gz %(path)s/%(dir)s/%(name)s_R1_trimmed_paired.txt  ~/Neisseria/fastq/%(name)s_R1_001_trimmed_unpaired.txt %(path)s/%(dir)s/%(name)s_R2_trimmed_paired.txt ~/Neisseria/fastq/%(path)s/%(dir)s/%(name)s_R2_trimmed_unpaired.txt LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:36" %locals())
        log.write('\n%(name)s\n' %locals())
        #log.flush()
        run('bwa mem -c 100 -M -T 50 -t 10 -R "@RG\tID:%(name)s\tSM:%(name)s\tPL:Illumina" %(path)s/ref/%(reference)s ~/Neisseria/fastq/%(name)s_trimmed_paired.txt  ~/Neisseria/fastq/%(name)s_trimmed_paired.txt > ~%(path)s/sams/%(name)s.sam' %locals())
        log.flush()


############################################################################################
args=
