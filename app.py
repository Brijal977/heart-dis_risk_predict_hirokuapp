import streamlit as st
from streamlit_option_menu import option_menu
from prediction import show_predict_page
from explore import show_explore_page
#from pillow import Image

st.set_page_config(
    page_title="Predict Heart Disease",

)

with st.sidebar:
    page = option_menu("", ["Facts and figures", 'Predict'],
                       icons=['card-image', 'eyeglasses'], menu_icon="cast", default_index=1)


if page == "Predict":
    show_predict_page()

elif page == "Facts and figures":
    show_explore_page()

else:
    st.write("UNKNOWN ERROR OCCURRED !!")

    # image = Image.open('heart.png')
    # st.image(image, caption='heart')
