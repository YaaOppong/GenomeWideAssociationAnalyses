# GenomeAnalyses
Various scripts in Python and R relating to genome-wide association studies (GWAS) and convergence-based analyses on bacterial data. 
To include permutation tests to establish significance thresholds.

## bam2unmapped
Python script that takes .bam files and stores unmpped reads, iterating over all .bam files in a directory.

## mat2fa.py  
Python script to take variant matrix in the form... and output a multifasta either with variant positions only or all positions in reference. Useful for downstream analyses eg tree building.
