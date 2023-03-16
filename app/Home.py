import streamlit as st
from streamlit_extras.switch_page_button import switch_page

import requests


################## WEBPAGE LAYOUT ###########################
# set favicon and title of the page in the browser tab
st.set_page_config(
            page_title="RECIPE RACCOON",
            page_icon=":raccoon:",
            layout="wide",
            initial_sidebar_state="collapsed")

#### Usable background images
# "https://images.pexels.com/photos/12221953/pexels-photo-12221953.jpeg"
# "https://images.pexels.com/photos/3952055/pexels-photo-3952055.jpeg"

#### CSS Styles ####
st.markdown("""
<meta charset="UTF-8">
<style>
.stApp {
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("https://images.pexels.com/photos/2074130/pexels-photo-2074130.jpeg");
    background-size: 1500px 1000px;
    position: fixed;
    background-color: #77AF9C
}
.header {
    font-size:100px;
    text-align:center;
    color: #F1E9DA
}
.sub_header {
    font-size:50px;
    text-align:center;
    color: #F1E9DA
}
</style>
""", unsafe_allow_html=True)

# Title
for i in range(5):
    st.markdown("")
st.markdown('<p class="header"><b>&#127859 RECIPE RACCOON<b> &#129437</p>', unsafe_allow_html=True)
st.markdown('<p class="sub_header"><b>Unleash Your Inner Chef<b></p>', unsafe_allow_html=True)


st.markdown("----")
columns = st.columns((2, 1, 2))
get_started = columns[1].button("Let's Get Started !")
if get_started:
    switch_page("Intro")
st.markdown("----")
