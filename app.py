import streamlit as st


st.title (" Apprentissage de python ")

st.sidebar.image('photo.JPG', caption='Rodney Duranty')


# Tyoe de données : entier naturel et les float 

variable_1 = 10
st.write(" Créatin de la variable :",variable_1)

# multiplication 
st.write(" Multiplication de la variable :",variable_1*2)

# division 
st.write(" Division de la variable :",variable_1/2)
#affichage du type de variable
 
#st.write(type(variable_1/2))
st.write(" Retenir que les entier :",variable_1//2)
# puissance 
st.write(" Puissance de la variable :",variable_1**2)

#Type de données : string (chaine de carractere )
variable_2 = " hello world "
#st.write(type(variable_2))

#Multiolication de chaine de carractére 
st.write (" multiplication de chaine de carractére :",variable_2*2)

#adition de chaine de carractére
st.write (" Aditon de la chaine de caractére :",variable_2+ "!")

