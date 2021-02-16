#Imports
import PIL
from PIL import Image
import numpy as np
import random


class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        
        # Write your code here
        self.shape = shape
        self.cropType = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        currDims = image.shape
        image = Image.fromarray(image,'RGB')
        try:
            assert currDims[0]>=self.shape[0] and currDims[1]>=self.shape[1]
            assert self.cropType=='center' or self.cropType=='random'
            box = None
            if self.cropType=='center':
                centX = self.shape[0]//2
                centY = self.shape[1]//2
                box = (((currDims[0]-self.shape[0])//2, (currDims[1]-self.shape[1])//2, (currDims[0]+self.shape[0])//2, (currDims[1]+self.shape[1])//2))
            else:
                lowX, lowY = self.shape
                lowX //= 2
                lowY //= 2
                hiX = currDims[0]//2 + lowX
                hiY = currDims[1]//2 + lowY
                centX =  random.randint(lowX, hiX)
                centY = random.randint(lowY, hiY)
                box = ((centX-currDims[0]//2), (centY-currDims[1]//2), (centX+currDims[0]//2), (centY+currDims[1]//2))
            fin_image = image.crop(box)
            fin_image.show()
            return np.array(fin_image)
        except AssertionError:
            print("Invalid arguments...")

