#import onnx
import tensorflow as tf
import json
from processing import ImageProcessor
from modelhublib.model import ModelBase
import PIL
import tensorflow as tf
import numpy as np
from tensorflow.python.saved_model import tag_constants

class Model(ModelBase):

    def __init__(self):
        # load config file
        config = json.load(open("model/config.json"))
        # get the image processor
        self._imageProcessor = ImageProcessor(config)
        # load the DL model (change this if you are not using ONNX)
        #self._model = onnx.load('model/model.onnx')
        #self._model = sfm


    def infer(self, input):
        inputAsNpArr = self._imageProcessor.loadAndPreprocess(input)
        # load preprocessed input
        graph = tf.Graph()
        with graph.as_default():
            with tf.Session(graph=graph) as sess:
                tf.saved_model.loader.load(
                    sess,
                    [tag_constants.SERVING],
                    'model/',
                )
                input_uint8 = graph.get_tensor_by_name('raw_input:0')
                prediction = graph.get_tensor_by_name('pose_prediction/pose_exp_net/pose/mul:0')

                pred = sess.run(prediction, feed_dict={input_uint8: inputAsNpArr[None,:,:,:]})

        output = self._imageProcessor.computeOutput(pred)
        return output
