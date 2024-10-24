import image_data as id
import image_rec as ir
import streamlit as st
import numpy as np

if 'database' not in st.session_state:
    st.session_state['database'] = id.load_database()

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    temp = id.to_numpy_img(image)
    id.display_numpy_img(temp)

    for i in st.session_state['database']:
        i.display()







