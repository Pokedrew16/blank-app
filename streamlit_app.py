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

if ('temp_img' not in st.session_state):
    if image is not None:
        st.session_state['temp_img'] = ir.run_over_all_pixels_np(invert_colour, ir.to_numpy_img_conventional_axes(image))
else:
    ir.display_numpy_img_conventional_axes(st.session_state['temp_img'])
    if image is None:
        st.session_state['temp_img'] = None







