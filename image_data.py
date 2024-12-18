import streamlit as st
import numpy as np
from PIL import Image, ImageOps
    
class Item:
    def __init__(self, name_v = "None", message_v = "",  link_v = "www.amazon.com/", img_v = "none.png"):
        self.name = name_v
        self.message = message_v
        self.link = link_v
        self.image_name = img_v

    def display(self):
        st.header("Common Name: " + self.name, divider="gray")
        if self.message is not "":
            st.subheader(self.message)
        st.image("./data/" + self.image_name)
        st.caption("A product of this category may be bought online at: " + self.link)

def load_database():
    item_arr = []
    with open("./data/database.txt", "r") as file:
        strs = file.readlines()
        for s in strs:
            entry_arr = s.split(",")
            item_arr.append(Item(entry_arr[0].strip(), entry_arr[1].strip(), entry_arr[2].strip(), entry_arr[3].strip()))
    return item_arr

def to_model_img(img):
    if img is None:
        return None
    img = Image.open(img)
    img = ImageOps.fit(img, (224,224), Image.Resampling.LANCZOS)
    img = np.array(img).reshape((1, 224, 224, 3)).astype(np.float32)
    return (img / 127.5) - 1.0

def display_model_img(np_arr):
    if (np_arr is not None):
        st.image(np_arr.reshape((224, 224, 3)) * .5 + .5)