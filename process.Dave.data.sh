#! /bin/sh

#input format = sample,otu
sort $1 |uniq -c > $1.score

#

python strip.white.space.py $1.score

R --no-save -f create.sample.by.OTU.table.R $1.score.csv $1.sample.by.OTU.csv


