import streamlit as st 

good_password = "1234"

password = st.text_input("tapper votre mot de passe")
st.sidebar.image('photo.JPG', caption='Rodney Duranty')

if good_password == password :
    st.write("Accès Autorisé")
    picture = st.camera_input("Take a picture")

    if picture:
        st.image()

elif password == "":
    st.write("Tapez votre mot de passe")

else:
    st.write("accès refusé") 
    st.write(password)
    st.image('image.png', caption='Refusé')
