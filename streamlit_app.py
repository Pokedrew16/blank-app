import image_data as id
import image_rec as ir
import streamlit as st
import numpy as np

if 'database' not in st.session_state:
    st.session_state['database'] = id.load_database()

if 'master_model' not in st.session_state:
    st.session_state['master_model'] = ir.load_model_from_database("master")

st.title("♻️ Welcome to ScanSuggest! Take a photo and a corresponding alternative will be provided.")
image = st.camera_input("Take a photo")

if image is not None:
    image = id.to_model_img(image);
    (pr, cd) = ir.prediction(st.session_state['master_model'], image)

    if len(st.session_state['database']) == pr:
        st.subheader("No object detected. Try again.");
    else:
        (st.session_state['database'])[pr].display()
        st.caption("The above is predicted to a confidence of " + "{:3.2f}".format(cd * 100.0) + "%")







