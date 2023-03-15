import streamlit as st
from streamlit_extras.switch_page_button import switch_page

################## WEBPAGE LAYOUT ###########################
# set favicon and title of the page in the browser tab
st.set_page_config(
            page_title="Your Kitchen AI",
            page_icon=":cooking:",
            # layout="centered",
            # initial_sidebar_state="auto"
)

# Load local css file to apply custom styling
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# local_css("style.css")

# Title
st.title(f"YOUR KITCHEN AI :cooking:")
st.write(f"Use your food ingredients in a smarter way\n")

# How it works
st.header("How it works")
col_a, col_b, col_c = st.columns(3)
col_a.markdown(f":one:\n Upload an image of your fridge and our AI will identify the food ingredients inside")
col_b.markdown(f":two:\n Specify your preferences and keywords")
col_c.markdown(f":three:\n Our app will suggest recipes based on ingredients and preferences you provide")

get_started = st.button("Let's Get Started !")
if get_started:
    switch_page("Step_1_Upload_Image")
