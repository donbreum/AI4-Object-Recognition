#!/bin/bash

cd ..

datafile=rockwool.data
cfgfile=rockwool-yolov3-tiny
best_weight=190110_rockwool-yolov3-tiny416_2400.weights
final_results_folder=final_results/different_sizes

# delete the thresholds that were generated before
if [ -e thresholds.txt ]; then
	rm thresholds.txt
fi

generate_plot()
{
	cfgname=$cfgfile$@".cfg"
	echo $cfgname
	no_extension="${cfgname%.*}"
	for thresh_val in $(seq 0.5 0.01 0.99); do	
		./darknet detector map cfg/$datafile cfg/$cfgname final_results/$best_weight -thresh $thresh_val
	done

	echo "Moving thresholds to "$final_results_folder/$no_extension"_thresholds.txt"
	mv thresholds.txt $final_results_folder/$no_extension"_thresholds.txt"

	python3 scripts/plot_threshold_results.py $final_results_folder/$no_extension"_thresholds.txt" $no_extension

	echo "Exporting graph to "$final_results_folder/$(date +%y%m%d)_$no_extension"_recall_vs_iou.png"

	mv $no_extension"_recall_vs_iou.png" $final_results_folder/$(date +%y%m%d)_$no_extension"_recall_vs_iou.png"
}

generate_plot 160
generate_plot 224
generate_plot 288
generate_plot 352
generate_plot 416
