import image_data as id
import image_rec as ir
import streamlit as st
import numpy as np
import time

def invert_colour(np_arr, x, y):
    np_arr[x,y,0] = 1.0 - np_arr[x,y,0];
    np_arr[x,y,1] = 1.0 - np_arr[x,y,1];
    np_arr[x,y,2] = 1.0 - np_arr[x,y,2];

if 'database' not in st.session_state:
    st.session_state['database'] = id.load_database()

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    temp = id.to_numpy_img_conventional_axes(image)
    id.run_over_all_pixels_np(invert_colour, temp)
    id.display_numpy_img_conventional_axes(temp)

    for i in st.session_state['database']:
        i.display()







