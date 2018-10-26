import xml.etree.ElementTree
import glob
from pathlib import Path
import os

def convert_to_txt(filename, path_in, path_out):

    split = filename.split('.')
    filename, extension = split[0], split[1]

    root = xml.etree.ElementTree.parse(path_in + filename + ".xml").getroot()

    size = root.find("size")
    objects = root.findall("object")

    width = int(size[0].text)
    height = int(size[1].text)

    obj_list = []

    for obj in objects:
        bounding_box = obj.find("bndbox")
        obj_dict = {}

        for elem in bounding_box:
            obj_dict[elem.tag] = int(elem.text)

        obj_list.append(obj_dict)

    # print(obj_list[2]['xmin'])

    for obj in obj_list:
        obj['x'] = int((obj['xmax'] + obj['xmin']) / 2)
        obj['y'] = int((obj['ymax'] + obj['ymin']) / 2)
        obj['width'] = obj['xmax'] - obj['xmin']
        obj['height'] = obj['ymax'] - obj['ymin']

    with open(path_out + filename + '.txt', "w") as file:

        for obj in obj_list:
            x = obj['x'] / float(width)
            y = obj['y'] / float(height)
            w = obj['width'] / float(width)
            h = obj['height'] / float(height)
            line = "0 {} {} {} {}\n".format(x, y, w, h)

            file.write(line)

if __name__ == "__main__":

    path = os.path.dirname(os.path.abspath(__file__))

    xml_folder = path + '/source_image_annotation/27092018_pallet_moving_L_annotations/'
    txt_folder = path + '/source_image_annotation/27092018_pallet_moving_L_annotations_txt/'

    print(path + xml_folder)

    for filepath in glob.iglob(xml_folder + '*.xml'):
        filename = filepath.split('/')[-1]
        
        try:
            convert_to_txt(filename, path_in=xml_folder, path_out=txt_folder)
        except Exception as e:
            print("Conversion failed. Aborting.")
            print(e)
            break
