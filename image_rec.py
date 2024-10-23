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

    def display(self):
        st.header("Result:")
        st.subheader("Name: " + self.name)
        st.image("./data/" + self.image_name)
        st.caption("This product may be bought online at: " + self.link)

def load_database():
    item_arr = []
    with open("./data/database.txt", "r") as file:
        strs = file.readlines()
        for s in strs:
            entry_arr = s.split(",")
            item_arr.append(Item(entry_arr[0].strip(), entry_arr[1].strip(), entry_arr[2].strip()))
    return item_arr

def to_numpy_img_conventional_axes(img):
    return np.array(Image.open(img)).transpose((1,0,2)) if (img is not None) else None

def run_over_all_pixels_np(func, np_arr_inout):
    if (np_arr_inout is None):
        return

    (width, height, channel) = np_arr_inout.shape
    for x in range(width):
        for y in range(height):
            func(np_arr_inout, x, y)

def display_numpy_img_conventional_axes(np_arr):
    st.image(np_arr.transpose((1,0,2)))