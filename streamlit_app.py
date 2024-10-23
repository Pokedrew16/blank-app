import image_rec as ir
import streamlit as st
import numpy as np
import time

def invert_colour(np_arr, x, y):
    np_arr[x,y,0] = 1.0 - np_arr[x,y,0];
    np_arr[x,y,1] = 1.0 - np_arr[x,y,1];
    np_arr[x,y,2] = 1.0 - np_arr[x,y,2];

if 'database' not in st.session_state:
    st.session_state['database'] = ir.load_database()

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    st.title("Temp")
    temp = ir.to_numpy_img_conventional_axes(image)
    ir.run_over_all_pixels_np(invert_colour, temp)
    ir.display_numpy_img_conventional_axes(temp)







