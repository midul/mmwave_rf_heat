#!/bin/sh
#python python_script.py
rm data_range.csv
rm data_peak.csv

count=1

EXT=dat
for i in *; do
	if [ "${i}" != "${i%.${EXT}}" ];then
		python2 ./parseTLV.py $i >> test"$i".txt
		echo "$i" >> files_processed_order.txt
		python graph_data.py test"$i".txt "$count"
		count=$((count+1))
		rm test"$i".txt
	fi
done

cat data_*


python ./graph_gen.py
