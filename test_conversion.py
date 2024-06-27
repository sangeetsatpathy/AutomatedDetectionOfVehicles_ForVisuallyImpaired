import os
import cv2

BASE_PATH_DATA = "C:/Users/sange/OneDrive/Desktop/AAR_Project/archive"

IMAGE_FILENAME = "1478020212192080435_jpg.rf.119bed7f90320ca6d2e8ca578f3efae1"


IMAGES_PATH_INITIAL = os.path.sep.join([BASE_PATH_DATA, f"images/train/{IMAGE_FILENAME}.jpg"])
LABEL_PATH_INITIAL = os.path.sep.join([BASE_PATH_DATA, f"labels/train/{IMAGE_FILENAME}.txt"])



img_color = cv2.imread(IMAGES_PATH_INITIAL, cv2.IMREAD_COLOR)
(img_height, img_width) = (540, 540)
#img_color = cv2.resize(img_color, (1900, 1200))

file = [(40, 228, 83, 283), (42, 229, 89, 276), (81, 210, 181, 320), (168, 234, 198, 277), (177, 231, 196, 287)]

for f in file:
    (xmin, ymin, xmax, ymax) = f

    box_height = int(ymax-ymin)
    box_width = int(xmax-xmin)

    box_center_x = (xmin + xmax)/2 # the SOLUTION is HERE
    box_center_y = (ymin + ymax)/2

    norm_x_center = float(box_center_x)/img_width
    norm_y_center = float(box_center_y)/img_height

    norm_box_height = float(box_height)/img_height
    norm_box_width = float(box_width)/img_width

    ######################

    x_center = int(float(norm_x_center)*img_width)
    y_center = int(float(norm_y_center)*img_height)

    img_color = cv2.circle(img_color, (x_center, y_center), radius=0, color=(0, 0, 255), thickness=5) ##THE CENTERS OF THE BOUNDING BOXES ARE OFF!?

    width = float(norm_box_width) * img_width
    height = float(norm_box_height) * img_height

    point1 = (int(x_center - (width/2)), int(y_center - (height/2)))
    point2 = (int(x_center + (width/2)), int(y_center + (height/2)))

    img_color = cv2.rectangle(img_color, point1, point2, (0, 255, 0), 2)
cv2.imshow("random", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
