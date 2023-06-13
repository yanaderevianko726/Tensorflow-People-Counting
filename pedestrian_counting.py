
import tensorflow as tf

from utils import backbone
from api import object_counting_api

# By default I use an "SSD with Mobilenet" model here. See the detection model zoo 
# (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) 
# for a list of other models that can be run out-of-the-box with varying speeds and accuracies.

detection_graph, category_index = backbone.set_model('ssd_mobilenet_v1_coco_2018_01_28', 'mscoco_label_map.pbtxt')

# set it to true for enabling the color prediction for the detected objects
is_color_recognition_enabled = False 

# roi line position
roi = 385 

# the constant that represents the object counting area
deviation = 1 

custom_object_name = 'Pedestrian' 
targeted_objects_name = "person"

# counting all the objects
object_counting_api.cumulative_object_counting_x_axis(detection_graph, 
                                                    category_index, 
                                                    is_color_recognition_enabled, 
                                                    roi, 
                                                    deviation, 
                                                    custom_object_name, 
                                                    targeted_objects_name) 
