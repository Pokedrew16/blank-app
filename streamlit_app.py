import image_rec as ir
import streamlit as st
import numpy as np
import time

if 'database' not in st.session_state:
    st.session_state['database'] = ir.load_database()

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    process_img(image)
else:
    st.write(st.session_state['temp_img'])







