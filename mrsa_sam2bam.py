from sys import argv
from subprocess import Popen, PIPE
import re

def run(cmd, dieOnError=True):
        ps=Popen(cmd, shell=True, stdout=log_sam2bam, stderr=log_sam2bam)
        exitcode=ps.wait()
        if dieOnError and exitcode !=0:
                raise Exception("run failed."+"cmd:`%(cmd)s` exit: %(exitcode)s" % locals())
                return (exitcode, stdout, stderr)



filenames=argv[1:]
log_sam2bam=open('log_sam2bam.txt', 'a')
for filename in filenames:
        name=re.sub("_R1_001.fastq.gz$", "", filename)
        log_sam2bam.write('\n%(name)s\n' %locals())
        log_sam2bam.flush()

        run("samtools view -bS sams2/%(name)s.sam >  bams2/%(name)s.bam" %locals() )
        run("samtools sort bams2/%(name)s.bam bams2/%(name)s.sorted" %locals())
        run("samtools index bams2/%(name)s.sorted.bam"%locals())
        run("mv bams2/%(name)s.sorted.bam bams2/%(name)s.bam" %locals())
        run("mv bams2/%(name)s.sorted.bam.bai bams2/%(name)s.bam.bai" %locals())
