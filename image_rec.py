import tensorflow as tf
import image_data as id
import numpy as np

from keras.models import load_model
from PIL import Image, ImageOps
    
def load_model_from_database(model_name):
    return load_model("./data/" + model_name + ".h5", compile=False)

def prediction(model, img_dat):
    confidences = model.predict(img_dat)
    predicted = np.argmax(confidences)
    return (predicted, confidences[0][predicted])