# AI4-Object-Recognition

### Clone Darkflow and install

git clone https://github.com/thtrieu/darkflow.git

cd darkflow 

pip install .


### move the images to the folder /object_recognition/training_images/source_images/annotated/
### find the images here

https://www.dropbox.com/sh/6fcwosml8tg08f9/AADrZ1jqSEstEV9MK8fKmKQxa?dl=0

### run the training
python3 flow --model cfg/tiny-yolo-voc-1c.cfg --load bin/tiny-yolo-voc.weights --train --annotation ../object_recognition/training_images/source_image_annotation/27092018_pallet_moving_L_annotations/ --dataset ../object_recognition/training_images/source_images/annotated/

### run on image using the test_object_detection.py