import glob, os
# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
# Percentage of images to be used for the test set
percentage_test = 10
# Create and/or truncate train.txt and test.txt
file_train = open('../../darknet/train.txt', 'w')  
file_test = open('../../darknet/test.txt', 'w')

# txt_folder = "/source_image_annotation/27092018_pallet_moving_L_annotations_txt/"
dji_path = current_dir + "/source_images/dji/samlet/"
static_path = current_dir + "/source_images/static/"

darknet_rel_path_dji = "../object_recognition/training_images/source_images/dji/samlet/"
darknet_rel_path_static = "../object_recognition/training_images/source_images/static/"
# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
# for pathAndFilename in glob.iglob(os.path.join(current_dir + txt_folder, "*.txt")):  
for pathAndFilename in glob.iglob(os.path.join(dji_path, "*.jpg")): 
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(darknet_rel_path_dji + title + '.jpg' + "\n")
    else:
        file_train.write(darknet_rel_path_dji + title + '.jpg' + "\n")
        counter = counter + 1

for pathAndFilename in glob.iglob(os.path.join(static_path, "*.txt")): 
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(darknet_rel_path_static + title + '.jpg' + "\n")
    else:
        file_train.write(darknet_rel_path_static + title + '.jpg' + "\n")
        counter = counter + 1
        