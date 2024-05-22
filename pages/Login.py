import streamlit as st 

good_password = "1234"

password = st.text_input("tapper votre mot de passe")
st.sidebar.write("Rodney Duranty")

if good_password == password :
    st.write("Accès Autorisé")
    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)

elif password == "0000":
    st.write("mot de passe incorrect")
else:
    st.write("accès refusé")
st.write(password)


