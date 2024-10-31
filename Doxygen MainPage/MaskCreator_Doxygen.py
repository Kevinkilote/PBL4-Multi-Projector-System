
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#˅

# Importing necessary libraries
# ˅
import cv2
import numpy as np

# ˄

##
# 
# @brief 
# 
# This class handles the image processing functions
# for modyfing projected images
#
class MaskCreator(object):

    ##
    #
    # @brief
    #
    # Constructor initializes values necessary for the
    # image processing
    #
    # @param[in] image: The image processed
    # 
    def __init__(self, image):
        ## This is the image that will be processed
        self.__image = image
        ## This is the alpha blending gradient that will be applied to the masked region
        self.__alpha_gradient = None
        ## This is the gamma value that will be used to correct the image
        self.__gamma_corrected = None
        ## This is the only public attribute in the class
        ## as it recieves non-masked image that gets overlayed with the masked region to
        ## create result image 
        self.result_image = None
        ## This is the masked region
        self.__mask = None
    
    ##
    #
    # @brief 
    #
    # This function creates the masked region and applies alpha gradient 
    # to it depending on the projected side of the image
    #
    # @param[in] image_side: The projected side of the image (left or right) as integer
    #
    # @param[in] image_width: The width of the image as integer
    #
    # @param[in] mask_width: The width of the mask as integer
    #
    # @note Masked region represents projected overlap region 
    # of the projected images
    #
    
    def createMask(self, image_side, mask_width, image_width):
        self.__mask = self.__image.shape[1] * mask_width // image_width
        if image_side == 1:
            self.__alpha_gradient = np.linspace(1, 0, self.__mask)
        elif image_side == 0:
            self.__alpha_gradient = np.linspace(0, 1, self.__mask)
    ##
    #
    #
    # @brief 
    # This function applies gamma correction to the image 
    #
    # @param[in] gamma: The gamma values as float
    #
    #
    #
    def gammaCorrection(self, gamma):
            self.__gamma_corrected = np.uint8(cv2.pow(self.__image / 255.0, gamma) * 255)
        
    ##
    #
    # @brief 
    # The function modifies the `result_image` attribute of the class by blending it with the gamma corrected image. 
    # The blending is done column by column, and the degree of blending is determined by the alpha gradient. 
    #
    # @param[in] image_side: The projected side of the image (left or right) as integer
    #
    # @note  If `image_side` is 1, the blending is applied from left to right. 
    # If `image_side` is 0, the blending is applied from right to left. 
    #
    #
    def alphaBlending(self, image_side):
        if image_side == 1:
            for col in range(self.__mask):
                alpha = self.__alpha_gradient[-self.__mask + col]
                self.result_image[:, col] = alpha * self.__gamma_corrected[:, col] + (1 - alpha) * self.result_image[:, col]
        elif image_side == 0:
            for col in range(self.__mask):
                alpha = self.__alpha_gradient[-self.__mask + col]
                self.result_image[:, -self.__mask + col] = alpha * self.__gamma_corrected[:, -self.__mask + col] + (1 - alpha) * self.result_image[:, -self.__mask + col]
        
    ##
    #
    # @brief
    # This function modifies the intensity of the image stored in `self.result_image` based on the `image_side` parameter. 
    # The intensity modification is performed column by column, starting from the edge and moving towards the center of the image. 
    # The intensity of each pixel in the column is multiplied by an `intensity_factor` which decreases linearly from 1 to 0 over the range of `self.__mask`.
    #
    # @param[in] image_side: The projected side of the image (left or right) as integer
    #
    # @note  If `image_side` is 1, the function modifies the intensity of the left side of the image. 
    # If `image_side` is 0, the function modifies the intensity of the right side of the image. 
    #
    def modifyIntensity(self, image_side):
        if image_side == 1:
            for col in range(self.__mask):
                intensity_factor = 1.0 - (self.__mask - col) / self.__mask
                self.result_image[:, col] = (self.result_image[:, col] * intensity_factor).astype(np.uint8)
        elif image_side == 0:
            for col in range(self.__mask):
                intensity_factor = 1.0 - col / self.__mask
                self.result_image[:, -self.__mask + col] = (self.result_image[:, -self.__mask + col] * intensity_factor).astype(np.uint8)


 
