#Imports

from PIL import Image
import numpy as np

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        # Write your code here
        try:
            assert isinstance(output_size,int) or isinstance(output_size,tuple)
            self.output_size = output_size
        except AssertionError:
            print("Invalid input to constructor......")


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        # Write your code here
        currDim = image.shape
        image = Image.fromarray(image)
        h = w = None
        if isinstance(self.output_size,int):
            h0 = currDim[0]
            w0 = currDim[1]
            if h0<w0:
                h = self.output_size
                w = int(h * (w0/h0))
            else:
                w = self.output_size
                h = int(w * (h0/w0))
        else:
            h,w = self.output_size
        fin_image = image.resize((h,w))
        fin_image.show()
        return np.array(fin_image)