import image_rec as ir
import streamlit as st
import numpy as np
from PIL import Image, ImageOps  # Install pillow instead of PIL
import time

if 'database' not in st.session_state:
    st.session_state['database'] = ir.load_database()

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    if 'temp_img' not in st.session_state:
        pil_img = Image.open(image)
        array = np.array(pil_img)
        st.session_state['temp_img'] = array
elif 'temp_img' in st.session_state:
    st.write(st.session_state['temp_img'])







