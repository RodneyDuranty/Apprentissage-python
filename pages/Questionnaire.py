import streamlit as st
st.title (" Questionnaire ")


st.sidebar.image('photo.webp', caption='Rodney Duranty')

title = st.text_input("Nom", "")

title = st.text_input("Prénom", "")

age = st.slider("How old are you?", 0, 130 )
