#Imports
import json
from PIL import Image
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms = None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_file = annotation_file
        self.transforms = transforms
        self.data = []
        with open(self.annotation_file) as f:
            for line in f:
                self.data.append(json.loads(line))

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.data)

        

    def __getitem__(self, idx):
        '''
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each 
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following, 
            1. Extract the correct annotation using the idx provided.
            2. Read the image and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the array would be (3, H, W).
            3. Scale the values in the array to be with [0, 1].
            4. Create a dictonary with both the image and annotations
            4. Perform the desired transformations.
            5. Return the transformed image and annotations as specified.
        '''
        curr_dict = {}
        curr_data = self.data[idx]
        curr_dir = '/home/rrohit2901/Software_lab_assns/Assn3/AssignmentQs2/data/'
        curr_img = Image.open(curr_dir + curr_data['img_fn'])
        gt_bboxes = [[] for i in range(0, len(curr_data['bboxes']))]
        for i, box in enumerate(curr_data['bboxes']):
            gt_bboxes[i].append(box['category']) 
            gt_bboxes[i] += box['bbox']
        gt_bboxes = np.array(gt_bboxes)
        if self.transforms is not None:
            for transform in self.transforms:
                curr_img = transform(curr_img)
        curr_dict['image'] = curr_img
        curr_dict['gt_bboxes'] = gt_bboxes
        return curr_dict
        

fil_path  ='/home/rrohit2901/Software_lab_assns/Assn3/AssignmentQs2/data/annotations.jsonl'
data = Dataset(fil_path,)
print(data.__getitem__(0))