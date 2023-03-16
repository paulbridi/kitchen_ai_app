import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
            page_title="RECIPE RACCOON",
            page_icon=":raccoon:",
            layout="wide",
            initial_sidebar_state="collapsed")

#### CSS Styles ####
st.markdown("""
<meta charset="UTF-8">
<style>
.stApp {
        background-color: #DCEAB2
}

</style>
""", unsafe_allow_html=True)


st.markdown(f"# Objective")
st.markdown(f"### Using a deep learning model to identify images of food ingredients \
            and suggest customised recipes")
for i in range(3):
    st.markdown("")

col1, col2, col3 = st.columns(3, gap="medium")
col1.markdown(f" ### :one:\n ### Object Detection Model")
col2.markdown(f" ### :two: \n ### CNN Model \n ### Identify food ingredients")
col3.markdown(f" ### :three: \n ### NLP Model \n ### Suggest recipes based on\
                ingredients and preferences provided by user")

st.markdown(f"#### Benefits : ")
col4, col5 = st.columns(2, gap="medium")
col4.markdown(f"#### :stew: Easier brainstorming of lunch/dinner/dessert")
col4.markdown(f"#### :bento: Allow users to experiment new recipes")
col5.markdown(f"#### :leafy_green: Better utilisation of ingredients")
col5.markdown(f"#### :wastebasket: Prevents food waste")

st.markdown("----")
columns = st.columns((2, 1, 2))
get_started = columns[1].button("How does it work ?")
if get_started:
    switch_page("Intro")
st.markdown("----")
