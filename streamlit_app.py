import image_data as id
import image_rec as ir
import streamlit as st
import numpy as np

if 'database' not in st.session_state:
    st.session_state['database'] = id.load_database()
if 'model' not in st.session_state:
    st.session_state['model'] = ir.load_model_from_database()

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    (pr,cd) = ir.prediction(st.session_state['model'], id.to_model_img(image))
    (st.session_state['database'])[pr].display(additional_info = "Prediction Confidence: " + "{:3.2f}".format(cd * 100.0) + "%")







