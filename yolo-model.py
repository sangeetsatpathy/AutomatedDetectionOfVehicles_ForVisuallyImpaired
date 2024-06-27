import torch
import numpy as np
import cv2
import time
import os
from deep_sort_realtime.deepsort_tracker import DeepSort

class ObjectDetection:
    """
    Class implements Yolo5 model to make inferences on a youtube video using OpenCV.
    """
    
    def __init__(self):
        """
        Initializes the class with youtube url and output file.
        :param url: Has to be as youtube URL,on which prediction is made.
        :param out_file: A valid output file name.
        """
        self.model = self.load_model()
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("\n\nDevice Used:",self.device)



    def load_model(self):
        """
        Loads Yolo5 model from pytorch hub.
        :return: Trained Pytorch model.
        """
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/sange/OneDrive/Desktop/AAR_Project/yolov5/runs/train/exp5/weights/best.pt', force_reload = True) 
        return model


    def score_frame(self, frame):
        """
        Takes a single frame as input, and scores the frame using yolo5 model.
        :param frame: input frame in numpy/list/tuple format.
        :return: Labels and Coordinates of objects detected by model in the frame.
        """
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
     
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord


    def class_to_label(self, x):
        """
        For a given label value, return corresponding string label.
        :param x: numeric label
        :return: corresponding string label
        """
        return self.classes[int(x)]


    def plot_boxes(self, results, frame, confidence=0.3):
        """
        Takes a frame and its results as input, and plots the bounding boxes and label on to the frame.
        :param results: contains labels and coordinates predicted by model on the given frame.
        :param frame: Frame which has been scored.
        :return: Frame with bounding boxes and labels ploted on it.
        """
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        detections = []
        for i in range(n):
            row = cord[i]
            if row[4] >= confidence:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
            
                detections.append(([x1, y1, int(x2-x1), int(y2-y1)], row[4], 'obstacle'))

        return frame, detections




# Create a new object and execute.
detection = ObjectDetection()


object_tracker = DeepSort(max_age=5, n_init=2, nms_max_overlap=1.0, max_cosine_distance=0.3, nn_budget=None,
                        override_track_class=None, embedder="mobilenet", half=True, bgr=True,
                        embedder_gpu=True, embedder_model_name=None, embedder_wts=None, polygon=False,
                        today=None)

player = cv2.VideoCapture("C:/Users/sange/OneDrive/Desktop/AAR_Project/aar_pics/IMG_1992.MOV") #Ran this for each video clip
x_shape = int(player.get(cv2.CAP_PROP_FRAME_WIDTH))
y_shape = int(player.get(cv2.CAP_PROP_FRAME_HEIGHT))
four_cc = cv2.VideoWriter_fourcc(*"MJPG")

out = cv2.VideoWriter("C:/Users/sange/OneDrive/Desktop/AAR_Project/out_pics/IMG_1992.avi", four_cc, 20, (x_shape, y_shape)) # Outputted every video clip here

frame_no = 0
while player.isOpened():
    ret, frame = player.read()
    if not ret: # checks if the return code has been set to 0 (no more frames to process)
        break
    #print(f"for frame no {frame_no}, timestamp is: {player.get(cv2.CAP_PROP_POS_MSEC)}")
    results = detection.score_frame(frame)
    vid_frame, det = detection.plot_boxes(results, frame)
    tracks = object_tracker.update_tracks(det, frame=vid_frame)# bbs expected to be a list of detections, each in tuples of ( [left,top,w,h], confidence, detection_class )

    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        ltrb = track.to_ltrb() # converts ltwh format into ltrb format

        bbox = ltrb
        cv2.rectangle(vid_frame,(int(bbox[0]), int(bbox[1])),(int(bbox[2]), int(bbox[3])),(0,0,255),2)
        cv2.putText(vid_frame, "ID: " + str(track_id), (int(bbox[0]), int(bbox[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    out.write(frame)
    frame_no += 1
