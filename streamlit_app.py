import image_rec as ir
import streamlit as st
import time

if 'database' not in st.session_state:
    st.session_state['database'] = ir.load_database()

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

#if image is not None:
#    bytes_data = image.getvalue()
#    st.image(bytes_data)
#    float_arr = np.array(list(bytes_data)).astype(dtype = np.float32)
#    st.write(float_arr[len(float_arr) >> 1])







