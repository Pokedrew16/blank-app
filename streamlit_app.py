import image_data as id
import tensorflow as tf
import image_rec as ir
import streamlit as st
import numpy as np

if 'database' not in st.session_state:
    st.session_state['database'] = id.load_database()
#if 'model' not in st.session_state:
#    st.session_state['model'] = ir.load_model_from_database()

st.title("♻️ Welcome to our responsible helper app ✅")
#image = st.camera_input("Take a photo")
st.write(tf.__version__)

#if image is not None:
#    (pr,cd) = prediction(st.session_state['model'], id.to_model_img(image))
#    (st.session_state['database'])[pr].display()







