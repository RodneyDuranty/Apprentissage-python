import streamlit as st
st.title (" Questionnaire ")


st.sidebar.image('photo.webp', caption='Rodney Duranty')

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)