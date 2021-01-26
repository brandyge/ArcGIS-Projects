# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:45:25 2021

@author: 17037
"""

#opens a feature class from a geodatabase
#and prints the spatal reference

import arcpy

featureClass = "D:/Projects/GISData/PlanningCartoProject/PetrolPlanning/NewValve.gdb/PotentialValveSites"

#describe the feature class and its spatial reference
desc = arcpy.Describe(featureClass)
spatialRef = desc.spatialReference

# print the spatial reference
print (spatialRef.name)