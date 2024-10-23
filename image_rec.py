import tensorflow as tf
import streamlit as st
import numpy as np

def load_database():
    with open("./data/helloworld.txt", "r") as file:
        return file.read()