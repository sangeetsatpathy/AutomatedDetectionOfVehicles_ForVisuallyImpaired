
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


#move all images from this to the image path
for filename in os.listdir(images_validation_path):
    current_path = os.path.sep.join([images_validation_path, filename])
    destination_path = os.path.sep.join([images_train_path, filename])

    os.rename(current_path, destination_path)

for filename_2 in os.listdir(images_test_path):
    current_path = os.path.sep.join([images_test_path, filename_2])
    destination_path = os.path.sep.join([images_train_path, filename_2])

    os.rename(current_path, destination_path)

for label_train in os.listdir(labels_train_path):
    c_path = os.path.sep.join([labels_train_path, label_train])
    os.remove(c_path)
for label_val in os.listdir(labels_validation_path):
    c_path_2 = os.path.sep.join([labels_validation_path, label_val])
    os.remove(c_path_2)

for label_tst in os.listdir(labels_test_path):
    c_path_3 = os.path.sep.join([labels_test_path, label_tst])
    os.remove(c_path_2)