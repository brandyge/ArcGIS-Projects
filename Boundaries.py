# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:09:03 2021

@author: 17037
"""

#opens a feature class from a geodatabase
#and prints the spatal reference

import arcpy

featureClass = "D:/Projects/GISData/Geog485/Lesson1/USAgdb/USA.gdb/Boundaries"

#describe the feature class and its spatial reference
desc = arcpy.Describe(featureClass)
spatialRef = desc.spatialReference

# print the spatial reference
print (spatialRef.name)
