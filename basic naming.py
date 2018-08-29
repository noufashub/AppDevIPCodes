#python snippet to get the names of layers and elements used in the project to use in the mapping code.
#For end of the term Assignment of Application Development IP
#Submitted by Noufa Cheerakkollil Konath and Venkatesh Nitchenakolla

import arcpy

aprx= arcpy.mp.ArcGISProject(r"G:\AppDevIP\India\India2.aprx")

Maps = aprx.listMaps()

#name of the map
for m in Maps:
    print(m.name)

#list of layers in the map 
India_Temp= aprx.listMaps()[0]
layers= India_Temp.listLayers()
for layer in layers:
    print (layer.name)

#if the layers are either vector file or raster file, responses are true and false    
for layer in layers:
    print(layer.isFeatureLayer)
    
for layer in layers:
    print (layer.isRasterLayer)

#lists the datasource of the layers    
for layer in layers:
    print (layer.dataSource)

#name of the layouts in the project    
layouts= aprx.listLayouts()
for layout in layouts:
    print(layout.name)
 
#list of elements in bothe the layouts   
Layout = aprx.listLayouts()[0]
Layout1 = aprx.listLayouts()[1]
    
for elm in Layout.listElements():
    print (elm.name)    

for elm in Layout1.listElements():
    print (elm.name)