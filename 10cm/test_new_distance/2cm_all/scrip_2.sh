#!/bin/sh
#python python_script.py
rm data_range.csv
rm data_peak.csv

count=1

EXT=dat
for i in *; do
	if [ "${i}" != "${i%.${EXT}}" ];then
		python2 ./parseTLV.py $i > temp.txt
		python graph_data_gen.py temp.txt
		rm temp.txt
	fi
done

LINES=10
for f in Y_*.csv; do
    #nl -s "," "$f" 
    a=`cat "$f" | wc -l`;
    if [ "$a" -le "$LINES" ]
    then
        rm -f "$f"
    fi
done


python ./data_graph_new.py Y_1_2.csv

#rm Y_*.csv

