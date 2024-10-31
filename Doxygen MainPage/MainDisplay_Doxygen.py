#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importing necessary libraries
# ˅
import cv2
# ˄

##
#
# @brief
# This class represents the main display functionality for projecting images. 
# It uses cv2 library to read and load images

class MainDisplay(object):
    ##
    #
    # @brief
    # Constructor initializes the MainDisplay with necessary values for its function.
    #
    def __init__(self):
        
        ## This variable wil store the image that will be displayed in the main.py file 
        self.result_image = None

    ##
    #
    # @brief 
    # Loads the image file from its image path/name.
    #
    # @param[in] image path: Path/name of the image to be read to load the images
    # to the main file for processing
    #
    # @return image: Loaded image from the image path/name 
    # 
    def loadImages(self, image_path):
        image = cv2.imread(image_path)
        return image
       

    ##
    # @brief
    # Initializes the result image to be processed
    #
    # @param[in] image: Loaded image to be processed
    #
    # @return result_image: Copy of the loaded image 
    #
    # @note result_image will used as the base of the final processed image

    def initializeImage(self, image):
        self.result_image = image.copy()
        return self.result_image

    ##
    # @brief
    # Save the processed result image.
    # 
    # @param[in] image: The final proessed image that is ready to be projected
    #
    # @param[in] image_name: The name that the image will be saved as
    #
    def saveImage(self, image, image_name):
        cv2.imwrite(f'result_{image_name}.jpg', self.result_image)

    # ˅
    
    # ˄


