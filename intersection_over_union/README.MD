### To run comparison between truth and prediction results:

#### RUN 

python3 compare_truth_prediction.py PATH_TO_XML_FILES PATH_TO_FIRST_XML_FILE_TO_USE PATH_TO_LAST_XML_FILE_TO_USE  PATH_TO_RESUL_TXT_FILE PATH_TO_IMAGE_FOLDER

e.g.

python3 compare_truth_prediction.py xml_anno/ xml_anno/image_0100_left.xml xml_anno/image_1529_left.xml  result.txt ../object_recognition/training_images/source_images/downsampled/
