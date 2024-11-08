import image_data as id
import image_rec as ir
import streamlit as st
import numpy as np

if 'database' not in st.session_state:
    st.session_state['database'] = id.load_database()

if 'master_model' not in st.session_state:
    st.session_state['master_model'] = ir.load_model_from_database("master")

if 'model' not in st.session_state:
    st.session_state['models'] = []
    st.session_state['models'].append(ir.load_model_from_database("containers"))
    st.session_state['models'].append(ir.load_model_from_database("tech_accessories"))
    st.session_state['models'].append(ir.load_model_from_database("tech_parts"))

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    image = id.to_model_img(image);
    (pr, cd) = ir.prediction(st.session_state['master_model'], image)
    (pr2, cd2) = ir.prediction(st.session_state['models'][pr], image)

    if st.session_state['database'][0][pr] == pr2:
        st.subheader("No object detected. Try again.");
    else:
        pr_actual = pr2 + 1
        for i in range(pr_type):
            pr_actual += st.session_state['database'][0][i]

        (st.session_state['database'])[pr_actual].display()
        st.caption("The above is predicted to a confidence of " + "{:3.2f}".format(cd2 * 100.0) + "%")







