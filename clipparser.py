import json
import cv2
import time
import os 
import numpy as np
from itertools import count
import matplotlib.image as mpimg
from tqdm import tqdm

class ClipParser:

    """ Summary: This class is used to process individual video clip
        assets into NumPy array files. This allows Perception IO's 
        eye tracking visualization software to instanly read in video
        frame image coordinates.
        
        Arguments:
            clip: video assets you wish to extract frame coordinates from
            filename: the filename you wish to name the output NumPy array file  """

    def __init__(self, clip, filename):
        self.clip = clip
        self.filename = filename 
        self.__parseClip()

    def __parseClip(self):

        print("Reading video: %s" % self.clip)
        vidcap = cv2.VideoCapture(self.clip)
        success, image = vidcap.read()
        num_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        print("There are %d frames in this asset: " % num_frames)

        array_to_save = []
        
        for video_frame in tqdm(range(num_frames)):
            cv2.imwrite("frame%d.jpg" % video_frame, image)    
            success, image = vidcap.read()
            try:
                coordinates = mpimg.imread('frame%d.jpg' % video_frame)
                array_to_save.append(coordinates)
            except:
                pass
            os.remove('frame%d.jpg' % video_frame)

        print("Saving video coordinates into %s.npy...\n" % self.filename)
        np.save(self.filename, array_to_save)

if __name__ == "__main__":

    # Path to subclips
    path = 'filmclips'

    for filename in os.listdir(path):
       # Path to individual subclip
       path = "/Users/tomshannon/Documents/movieclipper/filmclips/%s" % filename

       # Place to put numpy array file
       descriptor = "filmframes/" + filename.split('.')[0]

       # Take subclip and make numpy array of it 
       ClipParser(path, descriptor)

