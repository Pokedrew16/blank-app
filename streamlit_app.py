import streamlit as st
import numpy as np
import random
import time


#if 'image' not in st.session_state:
#    st.session_state['image'] = None

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    bytes_data = image.getvalue()
    st.image(bytes_data)
    float_array = bytes_data.astype(np.float)
    st.write(float_array[len(float_array) >> 1])
    st.write(len(float_array))








