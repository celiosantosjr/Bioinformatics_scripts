#usage python calculate.coverage.from.bed.coverage.file.py <file.txt>
#        	0			        1		

import sys


#convert histogram to mapping X coverage
#<chromosome> <depth of coverage> <bases with that coverage> <crhsize>


filein=open(sys.argv[1],'r')
outy=sys.argv[1]


#get unique contigs name

#split sample according to unique 
unique_contig=[]
for line in filein:
   line0=line.split('\s')
   contig_name=line0[0]
   if sample in unique_contig:
     continue
   else:
      unique_contig.append(contig)

#get 
for line in filein:
   line1=line.split('\s')
   contig_name=line1[0]
   depth_of_coverage=line1[1]
   bases_with_coverage=line1[2]
   contig_legth=line1[3]
   

   if sample in unique_contig:
     continue
   else:
      unique_contig.append(contig)

