import streamlit as st
st.title (" Questionnaire ")


st.sidebar.image('photo.webp', caption='Rodney Duranty')

title = st.text_input("Nom", "")

title = st.text_input("Prénom", "")

age = st.slider("Age", 0, 130 )
import datetime
import streamlit as st

d = st.date_input("Né le :",)
