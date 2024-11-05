import image_data as id
import image_rec as ir
import streamlit as st
import numpy as np

if 'database' not in st.session_state:
    st.session_state['database'] = id.load_database()
if 'model' not in st.session_state:
    st.session_state['containers_model'] = ir.load_model_from_database("containers")
    st.session_state['tech_accessories_model'] = ir.load_model_from_database("tech_accessories")
    st.session_state['tech_parts_model'] = ir.load_model_from_database("tech_parts")

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
    pr = [0] * len(st.session_state['database'][0]); cd = [0.0] * len(pr); image = id.to_model_img(image);
    (pr[0], cd[0]) = ir.prediction(st.session_state['containers_model'], image)
    (pr[1], cd[1]) = ir.prediction(st.session_state['tech_accessories_model'], image)
    (pr[2], cd[2]) = ir.prediction(st.session_state['tech_parts_model'], image)

    st.write(pr[0]);

    no_detection = True
    for i in range(len(pr)): # check if all classified as "random"
        no_detection &= st.session_state['database'][0][i] == pr[i]

    if no_detection:
        st.subheader("No object detected. Try again.");
    else:
        for i in range(len(pr)):
            cd[i] = 0.0 if st.session_state['database'][0][i] == pr[i] else cd[i]; # ignore "random"
        pr_type = np.argmax(np.array(cd))

        pr_actual = pr[pr_type] + 1
        for i in range(pr_type):
            pr_actual += st.session_state['database'][0][i]

        (st.session_state['database'])[pr_actual].display()
        st.caption("The above is predicted to a confidence of " + "{:3.2f}".format(cd[pr_type] * 100.0) + "%")







