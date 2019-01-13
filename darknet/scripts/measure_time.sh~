#!/bin/bash

start_time=$SECONDS

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
        * )                     
    esac
    shift
done

cd ..

#../darknet detector train ../cfg/rockwool.data ../cfg/rockwool-yolov3-tiny.cfg ../rockwool-yolov3-tiny_1500.weights

./darknet detector train cfg/$datafile cfg/$cfgfile weights/$weights -dont_show

weights_folder=backup
final_results_folder=final_results
model="${cfgfile%.*}"

if [ -e results.txt ]; then
	rm results.txt
fi

for filename in $weights_folder/*.weights; do
	[ -e "$filename" ] || continue

	filename=$(basename $filename)
	
	./darknet detector map cfg/$datafile cfg/$cfgfile backup/$filename

	python3 scripts/append_name.py $filename results.txt 
done

# delete the thresholds that were generated above
if [ -e thresholds.txt ]; then
	rm thresholds.txt
fi

if [ ! -d $final_results_folder ]; then
	mkdir $final_results_folder
fi

# find weights file with lowest recall score and return filename
name=$(python3 scripts/find_best_weight_file.py backup/ results.txt $model final_results_folder)
best_weight=$(date +%y%m%d)_$name
no_extension="${best_weight%.*}"

cp $weights_folder/$name $final_results_folder/$best_weight

echo "Moving results to "$final_results_folder/$no_extension"_results.txt"
mv results.txt $final_results_folder/$no_extension"_results.txt"

for thresh_val in $(seq 0.5 0.01 0.99); do	
	./darknet detector map cfg/$datafile cfg/$cfgfile $final_results_folder/$best_weight -thresh $thresh_val
done

echo "Moving thresholds to "$final_results_folder/$no_extension"_thresholds.txt"
mv thresholds.txt $final_results_folder/$no_extension"_thresholds.txt"

python3 scripts/plot_threshold_results.py $final_results_folder/$no_extension"_thresholds.txt" $model

echo "Exporting graph to "$final_results_folder/$(date +%y%m%d)_$model"_recall_vs_iou.png"

mv $model"_recall_vs_iou.png" $final_results_folder/$(date +%y%m%d)_$model"_recall_vs_iou.png"

rm $weights_folder/*

finish_time=$SECONDS
duration=$(expr $finish_time - $start_time)
hours=$(expr $duration / 3600)
remaining=$(expr $duration % 3600)
minutes=$(expr $remaining / 60)
seconds=$(expr $remaining % 60)

echo "This script took $hours:$minutes:$seconds"
