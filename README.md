# AutomatedDetectionOfVehicles_ForVisuallyImpaired
Code that I used to sort my image dataset and render the model outputs.


## Guide for each of the files

### Debugging Files
These files were used to debug an issue when the bounding box detections would consistently come up shifted away where it was supposed to be. It ended up being an issue with my image aspect ratios, which I had to rerun.

**test_conversion.py**

**test_source_images.py**

**test_images.py**

### Sorting my Dataset
These files were used to sort my image dataset (as well as their corresponding label files) into train, test, and validation sub-folders.

**sort_directory.py** - sorts the images

**reset_sort.py** - reset the sorted images whenever there was an error with the sorting

### Rendering the results of the model
**yolo-model.py** - This was used to take each of my video clips, run the model on it, and output a video file with the resulted bounding boxes (with their corresponding ID's).
