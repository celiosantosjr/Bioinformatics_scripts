#usage python create.newcazy.dictionary.py <fasta.file> <output.pkl.file>
#        	0				1		2		

import pickle
import sys
import Bio
from Bio import SeqIO
import re

filein=open(sys.argv[1],'rb')
fileout=open(sys.argv[2],'w')

print (filein)

cazydict={}

for seq_record in SeqIO.parse(filein, format="fasta"):
   description=seq_record.description
   subject=seq_record.name
   print(subject)
   organismsearch=re.search('\[[A-Za-z0-9\.\s\'\]]+',description)
   if organismsearch==None:
      organism="None"
   else:
      organism=organismsearch.group(0)

   description_search=re.search('\(["]?[A-a]+["]?:["]?[0-9]+["]?\)',description)
   familydata=description_search.group(0)
   thecazyclass=familydata.split(':')
   cazyclass=thecazyclass[0].strip('("')
   familynumber=thecazyclass[1].strip(')"')
   cazy=cazyclass+familynumber
   

   x=cazydict.get(subject, [])
   x.append(description)
   x.append(cazy)
   x.append(cazyclass)
   x.append(organism)
   cazydict[subject]=x

pickle.dump(cazydict,fileout)
