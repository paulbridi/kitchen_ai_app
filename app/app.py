import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from io import StringIO, BytesIO
import cv2
from packages.crop_fridge import crop_fridge

import requests
url = "https://kitchen-api-hebwau5dkq-ew.a.run.app"
res = requests.get(url + "/")

## TODO: import preproc and model function

## Cropping fridge into objects, return cropped images
## Pass cropped images to ingredient CNN model, return list of ingredients, w confidence
## Run NLP model with ingredients and user preferences as input, return top recipes

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("app/style.css")

uploaded_file = st.sidebar.file_uploader("Fridge:", type=['jpg','jpeg'])
if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Display the image:
    st.image(opencv_image, channels="BGR")

    cropped_images = crop_fridge(uploaded_file,30)
    for img in cropped_images:
        st.image(img, channels="BGR")

prefs = ['healthy', 'quick', 'mexican','..']

user_prefs = st.sidebar.multiselect(
    'Preferences:',
    prefs,
    [])

custom_input = ""
custom_input = st.sidebar.text_input('Freestyle:')

## Change background color of text box
# components.html(
#     """
# <script>
# const elements = window.parent.document.querySelectorAll('.stTextInput div[data-baseweb="input"] > div')
# console.log(elements)
# elements[0].style.backgroundColor = 'red'
# </script>
# """,
#     height=0,
#     width=0,
# )

if (st.sidebar.button('Go') or (user_prefs != "")) and uploaded_file is not None:
    # Display search results for user_query
    st.write(f"File: {uploaded_file}, Preferences: {user_prefs}, Custom input: {custom_input}")
    ## make request to predict ingredient

    res1 = requests.get(url + "/")
    st.write(res1.content)

    res = requests.post(url + "/upload_image", files={'img': cropped_images[0].tobytes()})
    st.write(res.content)
