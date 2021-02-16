#Imports
from PIL import Image
import numpy as np

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

        # Write your code here
        self.flip_type = flip_type

        
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        image = Image.fromarray(image, 'RGB')
        fin_image = None
        try:
            assert self.flip_type == 'horizontal' or self.flip_type == 'vertical'
            if self.flip_type == 'horizontal':
                fin_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            elif self.flip_type == 'vertical':
                fin_image = image.transpose(Image.FLIP_TOP_BOTTOM)
            fin_image.show()
            return np.array(fin_image)
        except AssertionError:
            print("Invalid flip type provided as argument...")





       