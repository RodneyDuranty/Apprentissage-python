import streamlit as st
st.title (" Questionnaire ")


st.sidebar.image('photo.webp', caption='Rodney Duranty')

title = st.text_input("Nom", "nom")

title = st.text_input("Prénom", "prénom")

age = st.slider("Age", 0, 130 )

title = st.text_input("Adresse", "n° et voies")

title = st.text_input("complément d'adresse", "porte")

title = st.text_input("Code postale", "75000")