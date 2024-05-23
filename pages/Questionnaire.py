import streamlit as st
st.title (" Questionnaire ")


st.sidebar.image('photo.webp', caption='Rodney Duranty')

title = st.text_input("Nom", "nom")

title = st.text_input("Prénom", "prénom")

age = st.slider("Age", 0, 130 )

title = st.text_input("Lieu de naissance", "ville")

title = st.text_input("Numéro de tél", "+33")

title = st.text_input("Adresse mail", "@gmail.com")

title = st.text_input("Adresse postal", "n° et voies")

title = st.text_input("complément d'adresse", "porte")

title = st.text_input("Code postal", "75000")


genre = st.radio(
    "Situation :",
    [":red[en couple]", "célibataire", "marié:"],
    captions = ["", "", ""])

if genre == ":red[en couple]":
    st.write("You selected en couple.")
else:
    st.write("You didn't select en couple.")
