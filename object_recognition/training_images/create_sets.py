import glob, os
# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
# Percentage of images to be used for the test set
percentage_test = 10;
# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# txt_folder = "/source_image_annotation/27092018_pallet_moving_L_annotations_txt/"
txt_folder = "/home/smatgaflen/Documents/github/AI4-Object-Recognition/object_recognition/training_images/source_image_annotation/27092018_pallet_moving_L_annotations_txt"
img_path = "/home/smatgaflen/Documents/darknet/data/rockwool/images/downsampled"
# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
# for pathAndFilename in glob.iglob(os.path.join(current_dir + txt_folder, "*.txt")):  
for pathAndFilename in glob.iglob(os.path.join(txt_folder, "*.txt")): 
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write(img_path + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(img_path + "/" + title + '.jpg' + "\n")
        counter = counter + 1