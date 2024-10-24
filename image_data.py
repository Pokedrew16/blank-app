import streamlit as st
import numpy as np
from PIL import Image, ImageOps
    
class Item:
    def __init__(self, name_v = "None", link_v = "www.amazon.com/", img_v = "none.png"):
        self.name = name_v
        self.link = link_v
        self.image_name = img_v

    def display(self):
        st.subheader("Common Name: " + self.name)
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

def to_numpy_img(img):
    if img is None:
        return None
    img = Image.open(img)
    img = ImageOps.fit(img, (224,224), Image.Resampling.LANCZOS)
    return np.array(img).reshape((1, 224, 224, 3))

def display_numpy_img(np_arr):
    if (np_arr is not None):
        st.image(np_arr.reshape((224, 224, 3)))