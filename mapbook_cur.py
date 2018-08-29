#python snippet to create a pdfmapbook using da.cursor as the parameter to loop through.
#For end of the term Assignment of Application Development IP
#Submitted by Noufa Cheerakkollil Konath and Venkatesh Nitchenakolla 

import arcpy

aprx= arcpy.mp.ArcGISProject(r"G:\AppDevIP\India\India2.aprx")

#list method for listing map, layers and layouts in the project 
Maps = aprx.listMaps()[0]
lyrInBoun = Maps.listLayers()[0]
lyrInStates= Maps.listLayers()[1]
lyrMaxTemp= Maps.listLayers()[2]
lyt = aprx.listLayouts()[0]

 
#define various elements to be used in the snippet later on
mapFrame = lyt.listElements("MAPFRAME_ELEMENT")[0]
Title_elm= lyt.listElements("TEXT_ELEMENT")
Legend=lyt.listElements("LEGEND_ELEMENT","Legend")

#Create an empty pdf document into which the different .pdf files will be added.
outPath = "G:\\AppDevIP\\Mapbooks" 
pdfDoc = arcpy.mp.PDFDocumentCreate(outPath  + "StateTemp2.pdf")

#append the title page to the mapbook
Layout1 = aprx.listLayouts()[1]
Layout1.exportToPDF(outPath + "first page" + ".PDF", 100)
pdfDoc.appendPages (outPath + "first page" + ".PDF")

#change name of the title of the maps 
for txt in lyt.listElements("TEXT_ELEMENT"):
    if txt.text == "TITLE":
         Title = txt
        
#change name of the title of the maps according to the name of the states from the table
cur = arcpy.da.SearchCursor(lyrInStates.dataSource, ["SHAPE@", "ST_NAME"]) 
#loop through the table, set extend using camera object, and change the name according to the name of the state (field)
for item in cur:
    for layer in Maps.listLayers("INDIAStates"):
        mapFrame.camera.setExtent(item[0].extent)
        txt.text = item[1] + " temperature"
        name = item[1]
        aprx.save
        lyt.exportToPDF(outPath + name +".PDF", 100)
        pdfDoc.appendPages (outPath + name +".PDF")
    
    

txt.text = "TITLE"          

pdfDoc.saveAndClose ()
print ("PDF Mapbook created")
del pdfDoc
del aprx
del Maps
del lyt
del item
del Layout1
del cur