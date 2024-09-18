import streamlit as st
import random
st.write("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
  bytes_data = image.getvalue()
  st.write(bytes_data)











