import arcpy

aprx= arcpy.mp.ArcGISProject(r"G:\AppDevIP\India\India2.aprx")

Maps = aprx.listMaps()[0]
lyrInBoun = Maps.listLayers()[0]
lyrInStates= Maps.listLayers()[1]
lyrMaxTemp= Maps.listLayers()[2]
lyt = aprx.listLayouts()[0]
print(lyt.name)

 
#Create an empty PDF document
mapFrame = lyt.listElements("MAPFRAME_ELEMENT")[0]
Title_elm= lyt.listElements("TEXT_ELEMENT")
Legend=lyt.listElements("LEGEND_ELEMENT")
outPath = "G:\\AppDevIP\\Mapbooks" 
pdfDoc = arcpy.mp.PDFDocumentCreate(outPath  + "StateTemp.pdf")


Layout1 = aprx.listLayouts()[1]
Layout1.exportToPDF(outPath + "first page" + ".PDF", 100)
pdfDoc.appendPages (outPath + "first page" + ".PDF")

#change name of the title of the map

for txt in lyt.listElements("TEXT_ELEMENT"):
    if txt.text == "TITLE":
         Title = txt
        

bookmarks= mapFrame.map.listBookmarks()
for bm in bookmarks:
    mapFrame.zoomToBookmark(bm)
    for layer in Maps.listLayers("INDIAStates"):
        txt.text = bm.name + "temperature"
        name = bm.name
        aprx.save
        lyt.exportToPDF(outPath + name +".PDF", 100)
        pdfDoc.appendPages (outPath + name +".PDF")
        

    
  

pdfDoc.saveAndClose ()
print ("PDF Mapbook created")
del pdfDoc
del aprx
del Maps
del lyt
del Layout1
del bm
