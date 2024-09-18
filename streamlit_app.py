import streamlit as st
import numpy as np
import random
st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")

if image is not None:
  bytes_data = image.getvalue()
  st.image(bytes_data)
  float_array = np.frombuffer(bytes_data, dtype=np.float32)/255.0
  st.write(float_array)










