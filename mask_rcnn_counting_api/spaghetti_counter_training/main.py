#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import backbone

image = cv2.imread('input3.jpg')

backbone.predict(image)
