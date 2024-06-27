import os
import cv2

BASE_PATH_DATA = "C:/Users/sange/OneDrive/Desktop/AAR_Project/archive"

IMAGE_FILENAME = "1478020212192080435_jpg.rf.119bed7f90320ca6d2e8ca578f3efae1"


IMAGES_PATH_INITIAL = os.path.sep.join([BASE_PATH_DATA, f"images/train/{IMAGE_FILENAME}.jpg"])


img_color = cv2.imread(IMAGES_PATH_INITIAL, cv2.IMREAD_COLOR)
(img_height, img_width) = (1200, 1900)
#img_color = cv2.resize(img_color, (1900, 1200))

file = [(40, 228, 83, 283), (42, 229, 89, 276), (81, 210, 181, 320), (168, 234, 198, 277), (177, 231, 196, 287)]

for f in file:
    (xmin, ymin, xmax, ymax) = f

    point1 = (xmin, ymin)
    point2 = (xmax, ymax)

    img_color = cv2.rectangle(img_color, point1, point2, (0, 255, 0), 2)
cv2.imshow("random", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()