from sklearn.model_selection import train_test_split
from pathlib import Path
import os

BASE_PATH_DATA = "C:/Users/sange/OneDrive/Desktop/AAR_Project/archive"
IMAGES_PATH_INITIAL = os.path.sep.join([BASE_PATH_DATA, "images/train"])
ANNOTS_PATH = os.path.sep.join([BASE_PATH_DATA, "_annotations.csv"])

filenames = []

images_train_path = os.path.sep.join([BASE_PATH_DATA, "images/train"])
images_validation_path = os.path.sep.join([BASE_PATH_DATA, "images/val"])
images_test_path = os.path.sep.join([BASE_PATH_DATA, "images/test"])

labels_train_path = os.path.sep.join([BASE_PATH_DATA, "labels/train"])
labels_validation_path = os.path.sep.join([BASE_PATH_DATA, "labels/val"])
labels_test_path = os.path.sep.join([BASE_PATH_DATA, "labels/test"])

#TODO: Have to add code to filter out the images that do not have any useful labels (i.e. traffic lights); Maybe we can just have empty text files if there are no cars, and just
# ignore the traffic lights and other useless things

def organize_dataset(images):
    train_split, val_split_raw = train_test_split(images, test_size=0.2, random_state=1)
    val_split, test_split = train_test_split(val_split_raw, test_size = 0.5, random_state=1)


    for im in val_split:
        current_path_img = os.path.sep.join([images_train_path, im])
        relocated_path_img = os.path.sep.join([images_validation_path, im])

        os.rename(current_path_img, relocated_path_img)

        img_split_extension = im.split(".jpg")
        filename_txt = img_split_extension[0] + ".txt"

        current_path_label = os.path.sep.join([labels_train_path, filename_txt])
        relocated_path_label = os.path.sep.join([labels_validation_path, filename_txt])

        os.rename(current_path_label, relocated_path_label)

        #TODO: move all of the validation LABEL.txt files into their directory, as well.; DONE

        #PROBLEM: one of our images cannot be found in the original directory because it is already moved to the 'val' directory; and the "rename" happens to it again.
    for img in test_split:
        current_path_img = os.path.sep.join([images_train_path, img])
        relocated_path_img = os.path.sep.join([images_test_path, img])

        os.rename(current_path_img, relocated_path_img)

        img_split_extension = img.split(".jpg")
        filename_txt = img_split_extension[0] + ".txt"

        current_path_label = os.path.sep.join([labels_train_path, filename_txt])
        relocated_path_label = os.path.sep.join([labels_test_path, filename_txt])

        os.rename(current_path_label, relocated_path_label)

rows = open(ANNOTS_PATH).read().strip().split("\n")[1:]


for i in rows:
    row_split = i.split(",")
    if(row_split == ['']):
        continue
    filename, img_width_str, img_height_str, label, xmin_str, ymin_str, xmax_str, ymax_str = row_split

    #print(ymin_str)

    ymin = int(ymin_str)
    ymax = int(ymax_str)

    xmin = int(xmin_str)
    xmax = int(xmax_str)

    img_width = int(img_width_str)
    img_height = int(img_height_str)

    box_height = int(ymax-ymin)
    box_width = int(xmax-xmin)

    box_center_x = (xmin + xmax)/2
    box_center_y = (ymin + ymax)/2

    
    labelled_target = (label, (xmin, ymin, xmax, ymax))

    if(len(filenames) == 0 or filename != filenames[-1]): # ERROR: it isn't necessarily sorted...
        filenames.append(filename)

    filename_without_extension = filename.split('.jpg')[0]
    file_opened = open(f"{labels_train_path}/{filename_without_extension}.txt", "a") #if there is a file with this path already existing, we just append to it.
    cat_id = -1

    if(label == "car"):
        cat_id = 0
    elif(label == "pedestrian"):
        cat_id = 1
    elif(label == "truck"):
        cat_id = 2
    elif(label == "biker"):
        cat_id = 3 

    if(cat_id != -1):
        file_opened.write(f"{cat_id} {box_center_x/img_width} {box_center_y/img_height} {box_width/img_width} {box_height/img_height}\n")
    file_opened.close()

organize_dataset(filenames)

#TODO: have to populate the txt files with information