
import numpy as np
import cv2
import backbone

from utils.object_tracking_module import tracking_layer
                     
# cap = cv2.VideoCapture("./input_images_and_videos/vehicle_survaillance.mp4")
cap = cv2.VideoCapture(0)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('the_output.avi',fourcc, fps, (width, height))

while(True):            
    ret, frame = cap.read()           
    np.asarray(frame)
    processed_frame = backbone.processor(frame)
    # out.write(processed_frame)
    # print("writing frame...")
    
    cv2.imshow("", processed_frame)
        
print("end of the video!")
