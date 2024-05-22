import streamlit as st 

good_password = "1234"

password = st.text_input("Tapez votre mot de passe")
st.sidebar.image('photo.JPG', caption='Rodney Duranty')
st.sidebar.link_button("Go to linkedin", "https://www.linkedin.com/in/rodney-duranty/")
if good_password == password :
    st.write("Accès Autorisé")
    picture = st.camera_input("Take a picture")

    if picture:
        st.image()

elif password == "":
    st.write("Tapez votre mot de passe")

else:
    st.write("Accès refusé") 
    st.write("Votre mot de passe : ",password)
    st.image('image.png', caption='Refusé')
