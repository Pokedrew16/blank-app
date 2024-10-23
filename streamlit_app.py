import image_rec as ir
import streamlit as st
import numpy as np
import time

image = None

if 'database' not in st.session_state:
    st.session_state['database'] = ir.load_database()
st.title("♻️ Welcome to our responsible helper app ✅")

if 'temp_img' not in st.session_state:
    image = st.camera_input("Take a photo")

if image is not None:
    st.session_state['temp_img'] = ir.to_numpy_img_conventional_axes(image)
elif 'temp_img' in st.session_state:
    st.image(ir.display_numpy_img_conventional_axes(st.session_state['temp_img']))







