# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:28:11 2019

@author: GELab
"""

import cv2
from pyzbar import pyzbar
import numpy as np

def getPolygonContours(barcode):
    
    
    
    pol = [[point.x,point.y] for point in barcode.polygon]
    
    polArray = np.array(pol)
    return polArray






def getAngle(line1,line2):
    
    
    
    
    pass



camera = cv2.VideoCapture(1)


while True:
    
    
    
    
    (cap , frame) = camera.read()
    frame = cv2.resize(frame,(480,480))
    barcodes = pyzbar.decode(frame)
    
# loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw
        # the bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        rectangleCoords = np.array([[x, y],
                                    [x, y + h],
                                    [x + w, y + h],
                                    [x + w, y]])
                           
        
        
        ##the actual polygon of the QR Code without parallel coords
        
        
        
        
        polygonCoords = getPolygonContours(barcode)
        cv2.drawContours(frame, [polygonCoords], -1, (0, 255, 0), 2)
        
        aligned = np.all(np.abs(polygonCoords-rectangleCoords)<40)
        
        
        # the barcode data is a bytes object so if we want to draw it
        # on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
 
        # draw the barcode data and barcode type on the image
#        text = "{} ({})  {}".format(barcodeData, barcodeType,aligned)

        text = "isAligned? {}".format(aligned)

        cv2.putText(frame, text, (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
 
    
    
        
    if cv2.waitKey(1) == 27: 
        break
    

    cv2.imshow('LiveFeed', frame)

camera.release()   
cv2.destroyAllWindows()
    
    
    
barcode.polygon
    
    
    
    
    
    
    
    
    