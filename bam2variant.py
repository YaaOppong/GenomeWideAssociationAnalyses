from sys import argv
from subprocess import Popen, PIPE
import re
import os

def run(cmd, dieOnError=True):
        ps=Popen(cmd, shell=True, stdout=log, stderr=log)
        exitcode=ps.wait()
        #stdout=ps.stdout.read()
        #stderr=ps.stderr.read()
       # if dieOnError and exitcode !=0:
               #raise Exception("run failed."+"cmd:`%(cmd)s` exit: %(exitcode)s" % locals())
               #return (exitcode, stdout, stderr)
        #print exitcode
        #print stdout
        #print stderr

def makeBCF(ref, name, directory, out_directory):
        #run("mkdir variants" %locals())
        run("samtools mpileup -B -Q 23 -d 2000 -C 50 -ugf %(ref)s %(directory)s/%(name)s.bam | bcftools view -bvcg - > %(out_directory)s/%(name)s.raw.bcf" %locals())
        run("bcftools view %(out_directory)s/%(name)s.raw.bcf | vcfutils.pl varFilter -d 10 > %(out_directory)s/%(name)s.filt.vcf" %locals())


log=open('log_bam2variants.txt', 'a')
script, ref, directory, out_directory=argv

for root, dirs, files in os.walk(directory):
        for file in files:
                match=re.match(".*bam$",file)
                if match:
                        name=re.sub( ".bam$", '', file)
                        log.write('\n%(name)s\n' %locals())
                        makeBCF(ref, name, directory, out_directory)
                        log.flush()


log.close()
