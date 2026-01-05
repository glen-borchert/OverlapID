# OverlapID
OverlapID is designed to determine overlaps between genomic positions listed in two separate .txt files in BED format.

The positions of annotated enhancers and/or genes of various different species can be obtained via Ensembl BioMart and/or Enhancer Atlas 2.0, and they should be saved as separate .txt files.

LG4 positions can be obtained via LG4ID, and should be extracted to be in BED format, then saved as .txt files.

The separate enhancer or gene position files are then input into OverlapID along with the LG4 positions to find any potential overlaps. Any identified overlaps are annotated with the positions of both the LG4 and overlapping regulatory elements, along with any other relevant data, and then output as an Excel file.
