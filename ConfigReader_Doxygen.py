#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#˅

# Importing necessary libraries
# ˅
import configparser
# ˄


##
#
# @brief
#
# This class reads necessary configuration values for image processing
# from the config file
# It uses configparser library to read configuration values
#
class ConfigReader:
    ##
    #
    # @brief
    #
    # Constructor reads and initializes the config file for other functions
    # in the class
    #
    def __init__(self,config_path): 

        # This is the config file
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
    
    ##
    #
    # @brief
    #
    # This function extracts image name from the config file
    #
    # @return image name as String
    #
    def getImageName(self):
        return self.config['DEFAULT']['image_name']

    ##
    #
    # @brief
    #
    # This function extracts image width from the config file
    #
    # @return image width as int
    #
    def getProjectedImageWidth(self):
        return int(self.config['DEFAULT']['projected_image_width'])

    ##
    #
    # @brief
    #
    # This function extracts image overlap width from the config file
    #
    # @return image overlap width as int
    #
    def getProjectedOverlapWidth(self):
        return int(self.config['DEFAULT']['projected_overlap_width'])
    ##
    #
    # @brief
    #
    # This function extracts the gamma value from the config file
    #
    # @return gamma value as float
    #
    def getGamma(self):
        return float(self.config['DEFAULT']['gamma'])

    ##
    #
    # @brief
    #
    # This function extracts the projected image side value from the config file
    #
    # @return side as int
    #
    # @note if returned value is 0 image is the left image
    #       if returned value is 1 image is the right image
    #
    def getSide(self):
        return int(self.config['DEFAULT']['image_side'])

     # ˅
    
    # ˄


# ˅

# ˄

