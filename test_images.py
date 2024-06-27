import os
import cv2

BASE_PATH_DATA = "C:/Users/sange/OneDrive/Desktop/AAR_Project/archive"

IMAGE_FILENAME = "1478020212192080435_jpg.rf.119bed7f90320ca6d2e8ca578f3efae1"


IMAGES_PATH_INITIAL = os.path.sep.join([BASE_PATH_DATA, f"images/train/{IMAGE_FILENAME}.jpg"])
LABEL_PATH_INITIAL = os.path.sep.join([BASE_PATH_DATA, f"labels/train/{IMAGE_FILENAME}.txt"])

file = open(LABEL_PATH_INITIAL, "r")

img_color = cv2.imread(IMAGES_PATH_INITIAL, cv2.IMREAD_COLOR)
(img_height, img_width) = (540, 540)
#img_color = cv2.resize(img_color, (1900, 1200))


for f in file:
    (class_id, x_center, y_center, width, height) = f.split(" ")
    x_center = int(float(x_center)*img_width)
    y_center = int(float(y_center)*img_height)

    img_color = cv2.circle(img_color, (x_center, y_center), radius=0, color=(0, 0, 255), thickness=5) ##THE CENTERS OF THE BOUNDING BOXES ARE OFF!?

    width = float(width) * img_width
    height = float(height) * img_height

    point1 = (int(x_center - (width/2)), int(y_center - (height/2)))
    point2 = (int(x_center + (width/2)), int(y_center + (height/2)))

    img_color = cv2.rectangle(img_color, point1, point2, (0, 255, 0), 2)
cv2.imshow("random", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

file.close()