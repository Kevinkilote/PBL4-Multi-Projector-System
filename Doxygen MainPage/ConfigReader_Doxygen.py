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
class ConfigReader(object):
    ##
    #
    # @brief
    #
    # Constructor reads and initializes the config file for other functions
    # in the class
    #
    def __init__(self,config_path): 

        # This is the config file
        self.__config = configparser.ConfigParser()
        self.__config.read(config_path)
    
    ##
    #
    # @brief
    #
    # This function extracts image name from the config file
    #
    # @return Image name as String value
    #
    def getImageName(self):
        return self.__config['DEFAULT']['image_name']

    ##
    #
    # @brief
    #
    # This function extracts image width from the config file
    #
    # @return Image width as int
    #
    def getProjectedImageWidth(self):
        return int(self.__config['DEFAULT']['projected_image_width'])

    ##
    #
    # @brief
    #
    # This function extracts image overlap width from the config file
    #
    # @return Image overlap width as integer value
    #
    def getProjectedOverlapWidth(self):
        return int(self.__config['DEFAULT']['projected_overlap_width'])
    ##
    #
    # @brief
    #
    # This function extracts the gamma value from the config file
    #
    # @return Gamma value as float value
    #
    def getGamma(self):
        return float(self.__config['DEFAULT']['gamma'])

    ##
    #
    # @brief
    #
    # This function extracts the projected image side value from the config file
    #
    # @return Side as integer value
    #
    # @note If returned value is 0, image is the left image.
    #       If returned value is 1, image is the right image.
    #
    def getSide(self):
        return int(self.__config['DEFAULT']['image_side'])

     # ˅
    
    # ˄


# ˅

# ˄

