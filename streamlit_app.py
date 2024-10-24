import image_data as id
import image_rec as ir
import streamlit as st
import numpy as np

if 'database' not in st.session_state:
    st.session_state['database'] = id.load_database()

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    id.display_model_img(id.to_model_img(image))

    for i in st.session_state['database']:
        i.display()







