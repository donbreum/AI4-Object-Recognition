#!/bin/bash

# Parse the arguments
while [ "$1" != "" ]; do
    case $1 in
        -d | --datafile )       shift
                                datafile=$1
                                ;;
        -c | --cfgfile )		shift
								cfgfile=$1
                                ;;
        -w | --weights )		shift
								weights=$1
								;;
        -s | --structure )		shift
								structure=$1
								;;
        * )                     
    esac
    shift
done

cd ..

#../darknet detector train ../cfg/rockwool.data ../cfg/rockwool-yolov3-tiny.cfg ../rockwool-yolov3-tiny_1500.weights
#./darknet detector train cfg/$datafile cfg/$cfgfile $weights -dont_show

weights_folder=backup
final_weights_folder=final_weights

if [ -e results.txt ]; then
	rm results.txt
fi

for filename in $weights_folder/*.weights; do
	[ -e "$filename" ] || continue

	filename=$(basename $filename)
	
	./darknet detector map cfg/$datafile cfg/$cfgfile backup/$filename
	dummy=$filename
	
	echo $dummy

	python3 scripts/append_name.py $filename results.txt 
done

# delete the thresholds that were generated above
if [ -e thresholds.txt ]; then
	rm thresholds.txt
fi

if [ ! -d final_weights ]; then
	mkdir final_weights
fi

name=$(python3 scripts/find_best_weight_file.py backup/ results.txt $structure final_weights_folder)
# find weights file with lowest recall score

cp $weights_folder/$name $final_weights_folder/$(date +%y%m%d)_$name

best_weight=$(date +%y%m%d)_$name

for thresh_val in $(seq 0.5 0.01 0.99); do	
	./darknet detector map cfg/$datafile cfg/$cfgfile $final_weights_folder/$best_weight -thresh $thresh_val
done
