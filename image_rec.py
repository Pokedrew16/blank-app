import tensorflow as tf
import image_data as id
import numpy as np

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
    
# insert functions

def load_model_from_database():
    return load_model("./data/keras_model.h5", compile=False)

def prediction(model, img_dat):
    confidences = model.predict(img_dat)
    predicted = np.argmax(confidences)
    return (predicted, confidences[0][predicted])