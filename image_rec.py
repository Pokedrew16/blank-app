import tensorflow as tf
import streamlit as st
import numpy as np

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
    
class Item:
    def __init__(self, name_v = "None", link_v = "www.amazon.com/", img_v = "none.png"):
        self.name = name_v
        self.link = link_v
        self.image_name = img_v

def load_database():
    item_arr = []
    with open("./data/database.txt", "r") as file:
        strs = file.readlines()
        for s in strs:
            entry_arr = s.split(",")
            item_arr.append(Item(entry_arr[0].strip(), entry_arr[1].strip(), entry_arr[2].strip()))
    return item_arr

def process_img(img):
    if 'temp_img' not in st.session_state:
        array = np.array(Image.open(img))
        (count, width, height, channel) = array.shape()
        for x in range(0, width):
            for y in range(0, height):
                array[0, x, y, 0] = 0.0
        st.session_state['temp_img'] = array