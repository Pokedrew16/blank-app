import torchvision as tv
from torchvision.models import resnet50, ResNet50_Weights
import streamlit as st
import numpy as np
import random
import time

#if 'image' not in st.session_state:
#    st.session_state['image'] = None

st.title("♻️ Welcome to our responsible helper app ✅")
image = st.camera_input("Take a photo")
st.write("./data/helloworld.txt")

#if image is not None:
#    bytes_data = image.getvalue()
#    st.image(bytes_data)
#    float_arr = np.array(list(bytes_data)).astype(dtype = np.float32)
#    st.write(float_arr[len(float_arr) >> 1])







