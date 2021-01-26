# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:53:56 2021

@author: 17037
"""

#This script uses map algebra to find values in an
# elevation raster greater than 3500 (meters).

import arcpy 
from arcpy.sa import *

# Specify the input raster
inRaster = "D:/Projects/GISData/Geog485/Lesson1/foxlake"
cutoffElevation = 3500

# Check out the Spatial Analyst Extension
arcpy.CheckOutExtension("Spatial")

# Make a map algebra expression and save the resulting raster
outRaster = Raster(inRaster) > cutoffElevation
outRaster.save("D:/Projects/GISData/Geog485/Lesson1/foxlake_hi_10")
               
#Check in the Spatial Analyst extension how that youre done
arcpy.CheckInExtension ("Spatial")