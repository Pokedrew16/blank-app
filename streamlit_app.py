import image_rec as ir
import streamlit as st
import numpy as np
import time

if 'database' not in st.session_state:
    st.session_state['database'] = ir.load_database()

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    if 'temp_img' not in st.session_state:
        bytes_data = image.getvalue()
        float_arr = np.array(list(bytes_data)).astype(dtype = np.float32)
        for i in range(int(len(float_arr) / 3)):
            float_arr[i * 3] = 0
        bytes_data = float_arr.astype(dtype = np.dtype('B')).tobytes()
        st.session_state['temp_img'] = bytes_data
    else:
        st.image(st.session_state['temp_img'])







