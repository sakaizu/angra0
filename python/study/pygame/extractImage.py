import os
from PIL import Image
import numpy as np

datapath = os.path.join(os.getcwd(), 'data')

img = Image.open(os.path.join(datapath, 'BG_test_01.png')).convert('RGB')

pixeldata = np.array(img, dtype='uint8')

#print(pixeldata[0][0][0])


def getdatafrompixel(file):
    img = Image.open(os.path.join(datapath, file)).convert('RGB')
    data = np.array(img, dtype='uint8')
    return data


