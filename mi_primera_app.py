import streamlit as st

st.title("Mi primera app")
st.write("Autor: Esta app fue elaborada por “Luis Felipe Moreno Chamorro”")

nombre_usuario = st.text_input("Ingresa tu nombre:")
mensaje = f"{nombre_usuario}, te doy la bienvenida a mi primera app."

st.write(mensaje)
