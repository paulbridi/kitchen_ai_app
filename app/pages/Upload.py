import streamlit as st
import numpy as np
from PIL import Image
import os
from packages.crop_fridge import crop_fridge
import cv2
import requests

#### set favicon and title of the page in the browser tab
st.set_page_config(
            page_title="RECIPE RACCOON",
            page_icon=":raccoon:",
            layout="wide",
            initial_sidebar_state="collapsed")

url = 'http://127.0.0.1:8003'
# url = "https://kitchen-api-hebwau5dkq-ew.a.run.app"


st.title("Upload an image of your food ingredients here!")
## image uploader tab
uploaded_file = st.file_uploader("Upload your image here", type=['jpg','jpeg','png'])

# preference drop down menu
prefs = ["Easy" ,"< 30 Mins","< 60 Mins","< 4 Hours","Meat","Vegetable",\
    "Fruit","Healthy","Inexpensive","Dessert","Beverages"]

user_prefs = st.multiselect('Preferences:', prefs)
custom_input = st.text_input("Any other keywords you would like to add? (Separate each keyword with a comma)", label_visibility="visible")

if uploaded_file is not None:
    MAX_SIZE = (2000,2000)

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    image = Image.open(uploaded_file)
    image.thumbnail(MAX_SIZE)
    image.save(os.path.join("fridge_results","results.jpg"))

    # Crop ingredients from fridge using roboflow model and display
    cropped_images_data = crop_fridge()
    roboflow_ingredients = [item['class'] for item in cropped_images_data[0]['predictions']]
    roboflow_confidences = [item['confidence'] for item in cropped_images_data[0]['predictions']]

    ## make request to predict ingredients
    img_shape=opencv_image.shape
    dtype_arr=opencv_image.dtype
    byte_arr=opencv_image.tobytes()
    from_bytes = np.frombuffer(byte_arr, dtype = opencv_image.dtype)
    files = {'my_file': byte_arr}


# col1, col2, col3 = st.columns(3)
if st.button('Ready, steady, cook!'):

    # send the POST request with the request body as multipart/form-data
    response = requests.post(
    url + '/predict_ingreds',
    files=files,
    data={'shape': str(img_shape), 'dtype': str(dtype_arr)}
    )

    # Get ingredients returned from model and prefences, store both as strings
    ingredients_list = [ingredient_data[0] for ingredient_data in response.json()['list']]
    ingredients_list_str = ','.join(ingredients_list)

    preferences_list = user_prefs + custom_input.split()
    preferences_list_str = ','.join(preferences_list)

    params = {"ingredients": ingredients_list_str, "preferences": preferences_list_str}

    # Loop through cropped images, returning image, ingredient, and confidence


    # for i, ingredient in enumerate(column_names['ingredients']):
    # st.markdown(ingredient.capitalize())

    num_ingredients = len(roboflow_ingredients)
    images = cropped_images_data[1]

    # Divide the screen width into `len(images)` columns
    cols = st.columns(num_ingredients)

    # Display each image in a separate column
    # with st.container():
    #     for i, image in enumerate(images):
    #         with cols[i]:
    #             # st.write(f"{response.json()['list'][i][0].capitalize()} ({response.json()['list'][i][1]}%)")
    #             st.write(f"{roboflow_ingredients[i].capitalize()} {'{:.1%}'.format(roboflow_confidences[i])}")
    #             st.image(image[0], use_column_width=True)
    #             st.write(type(image[0]))

    for i in range(0,num_ingredients): # number of rows in your table! = 2
        cols = st.columns(4) # number of columns in each row! = 2
        # first column of the ith row
        try:
            cols[0].write(f"{roboflow_ingredients[4*i].capitalize()} {'{:.0%}'.format(roboflow_confidences[i])}")
            cols[0].image(images[4*i][0])
        except:
            pass

        try:
            cols[1].write(f"{roboflow_ingredients[(4*i)+1].capitalize()} {'{:.0%}'.format(roboflow_confidences[i])}")
            cols[1].image(images[(4*i)+1][0])
        except:
            pass

        try:
            cols[2].write(f"{roboflow_ingredients[(4*i)+2].capitalize()} {'{:.0%}'.format(roboflow_confidences[i])}")
            cols[2].image(images[(4*i)+2][0])

        except:
            pass

        try:
            cols[3].write(f"{roboflow_ingredients[(4*i)+3].capitalize()} {'{:.0%}'.format(roboflow_confidences[i])}")
            cols[3].image(images[(4*i)+3][0])
        except:
            pass


    st.session_state['ings'] = ingredients_list_str
    st.session_state['prefs'] = preferences_list_str
