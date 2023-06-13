# TensorFlow Object Counting API
The TensorFlow Object Counting API is an open source framework built on top of TensorFlow and Keras that makes it easy to develop object counting systems. ***Please contact if you need professional object detection & tracking & counting project with the super high accuracy and reliability!***

## QUICK DEMO

---
### Cumulative Counting Mode (TensorFlow implementation):
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/107875666-4da86080-6ed2-11eb-9be8-cdd0815897cd.gif" | width=418> <img src="https://user-images.githubusercontent.com/22610163/43166945-c0744de0-8fa0-11e8-8985-9f863c59e859.gif" | width=400>
</p>

---
### Real-Time Counting Mode (TensorFlow implementation):
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/42237325-1f964e82-7f06-11e8-966b-dfde98701c66.gif" | width=410> <img src="https://user-images.githubusercontent.com/22610163/42238435-77ac0d34-7f09-11e8-9609-e7c3c2c5af74.gif" | width=410>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/42241094-14163cc8-7f12-11e8-83ed-68021b5e3b33.gif" | width=410><img src="https://user-images.githubusercontent.com/22610163/42237904-d6a3ac22-7f07-11e8-88f8-5f21430d9503.gif" | width=410>
</p>

---

---
### Object Tracking Mode (TensorFlow implementation):
<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/70389634-4682ea00-19d3-11ea-84a2-3996a43e98fe.gif" | width=410> <img src="https://user-images.githubusercontent.com/22610163/70389738-6bc42800-19d4-11ea-971f-f19cb5b90140.gif" | width=410>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/70389764-e9883380-19d4-11ea-8c54-80935811c3fa.gif" | width=825>
</p>

## USAGE

### 1.) Usage of "Cumulative Counting Mode"

#### 1.1) For detecting, tracking and counting *the pedestrians* with disabled color prediction

*Usage of "Cumulative Counting Mode" for the "pedestrian counting" case:*

    is_color_recognition_enabled = False # set it to true for enabling the color prediction for the detected objects
    roi = 385 # roi line position
    deviation = 1 # the constant that represents the object counting area

    object_counting_api.cumulative_object_counting_x_axis(input_video, detection_graph, category_index, is_color_recognition_enabled, roi, deviation) # counting all the objects
    
*Result of the "pedestrian counting" case:*
 
 <p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/43166945-c0744de0-8fa0-11e8-8985-9f863c59e859.gif" | width=700>
</p>

---

**1.2)** For detecting, tracking and counting *the vehicles* with enabled color prediction

*Usage of "Cumulative Counting Mode" for the "vehicle counting" case:*

    is_color_recognition_enabled = True # set it to true for enabling the color prediction for the detected objects
    roi = 200 # roi line position
    deviation = 3 # the constant that represents the object counting area

    object_counting_api.cumulative_object_counting_y_axis(input_video, detection_graph, category_index, is_color_recognition_enabled, roi, deviation) # counting all the objects
    
*Result of the "vehicle counting" case:*
 
 <p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/43166455-45964aac-8f9f-11e8-9ddf-f71d05f0c7f5.gif" | width=700>
</p>

---

### 2.) Usage of "Real-Time Counting Mode"

#### 2.1) For detecting, tracking and counting the *targeted object/s* with disabled color prediction
 
 *Usage of "the targeted object is bicycle":*
 
    is_color_recognition_enabled = False # set it to true for enabling the color prediction for the detected objects
    targeted_objects = "bicycle" 

    object_counting_api.targeted_object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled, targeted_objects) # targeted objects counting
    
 *Result of "the targeted object is bicycle":*
 
 <p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/42411751-1ae1d3f0-820a-11e8-8465-9ec9b44d4fe7.gif" | width=700>
</p>

*Usage of "the targeted object is person":*

    is_color_recognition_enabled = False # set it to true for enabling the color prediction for the detected objects
    targeted_objects = "person"

    object_counting_api.targeted_object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled, targeted_objects) # targeted objects counting
 
 *Result of "the targeted object is person":*

 <p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/42411749-1a80362c-820a-11e8-864e-acdeed85b1f2.gif" | width=700>
</p>

*Usage of "detecting, counting and tracking all the objects":*

    is_color_recognition_enabled = False # set it to true for enabling the color prediction for the detected objects

    object_counting_api.object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled) # counting all the objects
 
 *Result of "detecting, counting and tracking all the objects":*

 <p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/42411750-1aae0d72-820a-11e8-8726-4b57480f4cb8.gif" | width=700>
</p>

---
*Usage of "detecting, counting and tracking **the multiple targeted objects**":*

    targeted_objects = "person, bicycle" # (for counting targeted objects) change it with your targeted objects
    is_color_recognition_enabled = False # set it to true for enabling the color prediction for the detected objects

    object_counting_api.targeted_object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled, targeted_objects) # targeted objects counting
---
 
#### 2.2) For detecting, tracking and counting "all the objects with disabled color prediction"

*Usage of detecting, counting and tracking "all the objects with disabled color prediction":*
    
    is_color_recognition_enabled = False # set it to true for enabling the color prediction for the detected objects

    object_counting_api.object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled) # counting all the objects
    
 *Result of detecting, counting and tracking "all the objects with disabled color prediction":*

 <p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/42411748-1a5ab49c-820a-11e8-8648-d78ffa08c28c.gif" | width=700>
</p>


*Usage of detecting, counting and tracking "all the objects with enabled color prediction":*

    is_color_recognition_enabled = True # set it to true for enabling the color prediction for the detected objects

    object_counting_api.object_counting(input_video, detection_graph, category_index, is_color_recognition_enabled) # counting all the objects
    
 *Result of detecting, counting and tracking "all the objects with enabled color prediction":*

 <p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/42411747-1a215e4a-820a-11e8-8aef-faa500df6836.gif" | width=700>
</p>

*The default minimum object detecion threshold is 0.5!*

## General Capabilities of The TensorFlow Object Counting API

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/48421361-6662c280-e76d-11e8-9680-ec86e245fdac.jpg" | width = 720>
</p>

Here are some cool capabilities of TensorFlow Object Counting API:

- Detect just the targeted objects
- Detect all the objects
- Count just the targeted objects
- Count all the objects
- Predict color of the targeted objects
- Predict color of all the objects
- Predict speed of the targeted objects
- Predict speed of all the objects
- Print out the detection-counting result in a .csv file as an analysis report
- Save and store detected objects as new images under [detected_object folder](www)
- Select, download and use state of the art [models that are trained by Google Brain Team](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)
- Use [your own trained models](https://www.tensorflow.org/guide/keras) or [a fine-tuned model](https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/10_Fine-Tuning.ipynb) to detect spesific object/s
- Save detection and counting results as a new video or show detection and counting results in real time
- Process images or videos depending on your requirements

Here are some cool architectural design features of TensorFlow Object Counting API:

- Lightweigth, runs in real-time
- Scalable and well-designed framework, easy usage
- Gets "Pythonic Approach" advantages
- It supports REST Architecture and RESTful Web Services

TODOs:

- TensorFlox2.x support will be provided.
- Autonomus Training Image Annotation Tool will be developed.
- GUI will be developed.

## Theory

### System Architecture

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/48421362-6662c280-e76d-11e8-9b63-da9698626f75.jpg" | width=720>
</p>

- Object detection and classification have been developed on top of TensorFlow Object Detection API.

- Object color prediction has been developed using OpenCV via K-Nearest Neighbors Machine Learning Classification Algorithm is Trained Color Histogram Features.

[TensorFlow™](https://www.tensorflow.org/) is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) communicated between them.

[OpenCV (Open Source Computer Vision Library)](https://opencv.org/about.html) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products.

### Tracker

<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/41812993-a4b5a172-7735-11e8-89f6-083ec0625f21.png" | width=700>
</p>

Source video is read frame by frame with OpenCV. Each frames is processed by ["SSD with Mobilenet" model](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2017_11_17) is developed on TensorFlow. This is a loop that continue working till reaching end of the video. The main pipeline of the tracker is given at the above Figure.

## Installation

### Dependencies

Tensorflow Object Counting API depends on the following libraries (see [requirements.txt]()):

- [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)
- **tensorflow==1.5.0**
- **keras==2.0.8**
- **opencv-python==4.4.0.42**
- Protobuf 3.0.0
- Python-tk
- Pillow 1.0
- lxml
- tf Slim (which is included in the "tensorflow/models/research/" checkout)
- Jupyter notebook
- Matplotlib
- Cython
- contextlib2
- cocoapi

For detailed steps to install Tensorflow, follow the [Tensorflow installation instructions](https://www.tensorflow.org/install/). 

### Important: Compatibility problems caused by TensorFlow2 version.

This project developed with TensorFlow 1.5.0 version. If you need to run this project with TensorFlow 2.x version, just replace tensorflow imports with tensorflow.compat.v1, and add tf.disable_v2_behavior that's all. 

Instead of this import statement:

    import tensorflow

use this:

    import tensorflow.compat.v1 as tf
    tf.disable_v2_behavior()

## Author
Yana Derevianko

## License
This system is available under the MIT license. See the LICENSE file for more info.
