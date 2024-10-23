import tensorflow as tf
import streamlit as st
import numpy as np
    
class Item:
    def __init__(self, name_v = "None", link_v = "www.amazon.com/", img_v = "none.png"):
        self.name = name_v
        self.link = link_v
        self.image_name = img_v

def load_database():
    item_arr = []
    with open("./data/helloworld.txt", "r") as file:
        strs = file.readlines()
        for s in strs:
            entry_arr = s.split(",")
            item_arr.append(Item(entry_arr[0].strip(), entry_arr[1].strip(), entry_arr[2].strip()))
    return item_arr

