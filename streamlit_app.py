import streamlit as st
import numpy as np
import random
import time


if 'image' not in st.session_state:
    st.session_state['image'] = None

st.title("♻️ Welcome to our responsible helper app ✅")
if st.session_state['image'] is None:
    st.session_state['image'] = st.camera_input("Take a photo")
else:
    bytes_data = st.session_state['image'].getvalue()
    st.image(bytes_data)
    float_array = np.frombuffer(bytes_data, dtype=np.float32)/255.0
    st.write(float_array)







