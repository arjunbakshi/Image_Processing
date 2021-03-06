#!/usr/bin/env python
import Image
import numpy as np
tab='\t'

BLUE = 0
GREEN = 1
RED = 2
ALPHA = 3

def arrayToImage(arr):
    return Image.fromarray(np.uint8(arr))
    
def Imagetoarray(img):
    return np.array(img)
    
def getImageAsArray(path):
    return np.array(imread(path).astype(float))
    
