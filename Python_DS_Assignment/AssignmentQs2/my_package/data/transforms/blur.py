#Imports
from PIL import Image, ImageFilter
import numpy as np

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''

        # Write your code here
        try:
            self.radius = radius
            assert isinstance(self.radius, int)
        except AssertionError:
            print("Invalid argument type....")
        

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

        # Write your code here
        image = Image.fromarray(image)
        fin_image = image.filter(ImageFilter.GaussianBlur(radius = self.radius))
        return np.array(fin_image)
        
