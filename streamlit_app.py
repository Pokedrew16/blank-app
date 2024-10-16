import streamlit as st
import numpy as np
import random
import time


if 'count' not in st.session_state:
    st.session_state['frameTemp'] = 0
    st.session_state['image'] = None

st.title("♻️ Welcome to our responsible helper app ✅")
st.session_state['image'] = st.camera_input("Take a photo")

if st.session_state['image'] is not None:
    if st.session_state['frameTemp'] != 0:
        bytes_data = st.session_state['image'].getvalue()
        st.image(bytes_data)
        float_array = np.frombuffer(bytes_data, dtype=np.float32)/255.0
        st.write(float_array)
        st.session_state['frameTemp'] = 0
    st.session_state['frameTemp'] += 1

st.write(st.session_state['frameTemp'])
  






