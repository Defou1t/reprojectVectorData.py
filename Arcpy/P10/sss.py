import arcpy
import os

#set up the paths
arcpy.env.workspace = r"D:\Univer\Kurs3\Programming\Prog2\Arcpy\P10"
inputFC = r"D:\Univer\Kurs3\Programming\Prog2\Arcpy\P10\CountyLines.shp"

#get spatial reference for the target feature class
inputDescribe = arcpy.Describe(inputFC)
inputSR = inputDescribe.SpatialReference
inputSRName = inputSR.Name

# Get a list of my feature classes
listOfFCs = arcpy.ListFeatureClasses()

#Loop through the list of FCs
for fc in listOfFCs:
    #Read the spatial reference of the current one
    fcDescribe = arcpy.Describe(fc)
    fcSR = fcDescribe.SpatialReference
    fcSRName = fcSR.Name

if fcSRName != inputSRName:
    print "Spatial references don't match"
else:
    print "Spatial references do match"

if fcSRName == inputSRName:
    continue
else:
    # Determine the new output feature class path and name
    outFS = fc[:-4] +"_projected.shp"
    arcpy.Project_management(fc, outFS, inputSR)
    print rootName
    print rootName +"_projected.shp" 
