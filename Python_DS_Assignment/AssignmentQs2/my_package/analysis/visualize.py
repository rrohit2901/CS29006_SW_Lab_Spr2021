#Imports
import PIL
from PIL import Image, ImageDraw
import numpy as np

def plot_boxes(input_dict): # Write the required arguments

  # The function should plot the predicted boxes on the images and save them.
  # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
  my_image = input_dict['image']
  draw = ImageDraw.Draw(my_image)
  for bbox in input_dict['gt_bboxes']:
    text, x0, y0, x1, y1 = bbox
    x0 = int(float(x0))
    x1 = int(float(x1))
    y0 = int(float(y0))
    y1 = int(float(y1))
    draw.rectangle([x0, y0, x1, y1])
    draw.text((x0,y0), text)

  my_image.show()
  return np.asarray(my_image)

  
# input_dict = {}
# input_dict['image'] = Image.open('/home/rrohit2901/Software_lab_assns/Assn3/AssignmentQs2/data/imgs' + '/0.jpg')
# input_dict['gt_bboxes'] = np.array([['dog', '74.9525', '19.349288702928867', '121.89099999999999', '114.24000000000001']], dtype='<U18')

# plot_boxes(input_dict)