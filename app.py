import streamlit as st
import streamlit_authenticator as stauth
import matplotlib.pyplot as plt

# Usuarios y contraseñas
names = ['AmBar']
usernames = ['ambarviole']
passwords = ['1234']  # Cambia esta contraseña

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    'cookie_name',
    'secret_signature_key',
    cookie_expiry_days=1
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.title("Hola, esta es mi app web con Streamlit")
    st.write("Puedes mostrar gráficos, datos, texto, imágenes y más.")
    
    # Datos de ejemplo para gráfico de barras
    categorias = ['Manzanas', 'Bananas', 'Cerezas', 'Dátiles']
    valores = [10, 15, 7, 12]

    fig, ax = plt.subplots()
    ax.bar(categorias, valores, color='skyblue')
    ax.set_ylabel('Cantidad')
    ax.set_title('Gráfico de barras de frutas')

    st.pyplot(fig)
    
    if st.button('Cerrar sesión'):
        authenticator.logout('Logout', 'main')
        st.experimental_rerun()

elif authentication_status == False:
    st.error('Usuario o contraseña incorrectos')
elif authentication_status == None:
    st.warning('Por favor ingresa tus credenciales')
