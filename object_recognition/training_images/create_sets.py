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
all_path = current_dir + "/source_images/new_downsampled/"

darknet_rel_path_dji = "../object_recognition/training_images/source_images/dji/samlet/"
darknet_rel_path_static = "../object_recognition/training_images/source_images/static/"
darknet_rel_path_all = "../object_recognition/training_images/source_images/new_downsampled/"
# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
# look for images with an associated txt file 
# for pathAndFilename in glob.iglob(os.path.join(dji_path, "*.txt")): 
#     title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#     if counter == index_test:
#         counter = 1
#         # file_test.write(darknet_rel_path_dji + title + '.jpg' + "\n")
#     else:
#         # file_train.write(darknet_rel_path_dji + title + '.jpg' + "\n")
#         counter = counter + 1

# for pathAndFilename in glob.iglob(os.path.join(static_path, "*.txt")): 
#     title, ext = os.path.splitext(os.path.basename(pathAndFilename))
#     if counter == index_test:
#         counter = 1
#         # file_test.write(darknet_rel_path_static + title + '.jpg' + "\n")
#     else:
#         # file_train.write(darknet_rel_path_static + title + '.jpg' + "\n")
#         counter = counter + 1
 
# testing_path = current_dir + "/source_images/testing/"
# darknet_rel_path_testing = "../object_recognition/training_images/source_images/testing/"
print(all_path)
for pathAndFilename in glob.iglob(os.path.join(all_path, "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(darknet_rel_path_all + title + '.jpg' + "\n")
    else:
        file_train.write(darknet_rel_path_all + title + '.jpg' + "\n")
        counter = counter + 1