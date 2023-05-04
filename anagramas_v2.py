import os
import streamlit as st

# Ruta de la carpeta que contiene los archivos de texto del diccionario
path_diccionario = "C:/Users/raul.camara/Proyectos/Anagramas_v2/dict_rae_txt/dics"

# Función que devuelve una lista de anagramas de una palabra
def encontrar_anagramas(palabra, archivos):
    # Eliminamos los caracteres no alfabéticos de la palabra y la convertimos a minúsculas
    palabra = "".join(filter(str.isalpha, palabra)).lower()
    # Buscamos anagramas en cada archivo
    anagramas = []
    for archivo in archivos:
        with open(os.path.join(path_diccionario, archivo), "r", encoding="utf-8") as f:
            for linea in f:
                # Eliminamos los caracteres no alfabéticos de la palabra del archivo y la convertimos a minúsculas
                palabra_archivo = "".join(filter(str.isalpha, linea)).lower()
                # Si ambas palabras tienen la misma longitud y las mismas letras, son anagramas exactos
                if sorted(palabra) == sorted(palabra_archivo) and len(palabra) == len(palabra_archivo):
                    anagramas.append(linea.strip())
    return anagramas

# Configuración de la aplicación Streamlit
st.set_page_config(page_title="Anagramas de palabras en el diccionario", page_icon=":memo:", layout="wide")

# Título de la aplicación
st.title("Anagramas exactos de palabras del diccionario de la Real Academia Española de la Lengua")

# Campo de entrada para la palabra
palabra = st.text_input("Ingresa una palabra -sin acentos- para buscar sus anagramas:")

# Validación de la palabra ingresada
if not palabra:
    st.warning("Por favor ingresa una palabra")
elif len(palabra) > 26:
    st.warning("La longitud de la palabra no puede ser mayor que la cantidad de letras contenidas en cualquier archivo del diccionario")
else:
    # Obtenemos la lista de archivos del diccionario
    archivos = os.listdir(path_diccionario)
    # Buscamos anagramas de la palabra
    anagramas = encontrar_anagramas(palabra, archivos)
    # Mostramos los anagramas encontrados
    if not anagramas:
        st.write("No se han encontrado anagramas para la palabra ingresada")
    else:
        st.write(f"Se han encontrado {len(anagramas)} anagramas para la palabra '{palabra}':")
        for anagrama in anagramas:
            st.write(anagrama)
