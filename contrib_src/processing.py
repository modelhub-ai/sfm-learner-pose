from modelhublib.processor import ImageProcessorBase
import PIL
import SimpleITK
import numpy as np
import json
from utils import *

class ImageProcessor(ImageProcessorBase):

    # OPTIONAL: Use this method to preprocess images using the image objects
    #           they've been loaded into automatically.
    #           You can skip this and just perform the preprocessing after
    #           the input image has been convertet to a numpy array (see below).
    def _preprocessBeforeConversionToNumpy(self, image):
        if isinstance(image, PIL.Image.Image):
            # TODO: implement preprocessing of PIL image objects
            pass
        elif isinstance(image, SimpleITK.Image):
            # TODO: implement preprocessing of SimpleITK image objects
            pass
        else:
            raise IOError("Image Type not supported for preprocessing.")
        return image


    def _preprocessAfterConversionToNumpy(self, npArr):
        # TODO: implement preprocessing of image after it was converted to a numpy array
        npArr = np.squeeze(npArr)
        npArr = np.moveaxis(npArr, 0, -1)
        #raise IOError(npArr)
        return npArr


    def computeOutput(self, inferenceResults):
        # TODO: implement postprocessing of inference results
        # Insert the target pose [0, 0, 0, 0, 0, 0]
        pred_poses=inferenceResults.squeeze()
        pred_poses = np.insert(pred_poses, 1, np.zeros((1,6)), axis=0)
        printpose=-1*pred_poses[0];
        tx = printpose[0];
        ty = printpose[1];
        tz = printpose[2];
        qw, qx, qy, qz = euler2quat(printpose[5], printpose[4], printpose[3])
        result = np.array([tx, ty, tz, qx, qy, qz, qw])
        return result
