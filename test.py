import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from drive import guardar_en_google_sheets
#pip freeze > requirements.txt
#streamlit run test.py

# Configuración de la página para que sea responsiva
st.set_page_config(layout="wide")

# Estilo CSS para mejorar la visualización en móviles y tablets
st.markdown("""
<style>
    .stRadio > label {
        font-size: 1.2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .stTextInput>div>div>input {
        font-size: 1.3rem;
    }
    .stMarkdown {
        font-size: 1.3rem;
    }
</style>
""", unsafe_allow_html=True)

# Título y descripción
st.title("🧠 Test de Inteligencias Múltiples - El Expreso de Leo 🚂")
st.markdown("""
Este test es una herramienta de observación para familias de niños de 2 a 6 años.
Su propósito es ayudar a reconocer cómo aprende, se expresa y se relaciona su hijo.
""")

# Aviso de Habeas Data
st.header("📜 Aviso de Privacidad y Tratamiento de Datos")
acepto = st.checkbox("""
Este formulario tiene como finalidad recoger sus datos personales necesarios para el proceso de envío de sus productos. Los datos que solicitamos incluyen información de contacto, dirección de envío y cualquier dato pertinente para garantizar una correcta entrega.

La información recolectada será tratada bajo los principios de confidencialidad y seguridad, conforme a la **Ley 1581 de 2012 de Protección de Datos Personales (Habeas Data)** en Colombia. El responsable del tratamiento de estos datos es **Editorial Bebe Genial**.

Sus datos serán usados exclusivamente para gestionar el envío del producto adquirido y envío de publicidad de nuestros productos y servicios y no serán compartidos con terceros no autorizados. Usted tiene derecho a acceder, corregir o solicitar la eliminación de sus datos en cualquier momento, contactándonos a través del correo **servicioalcliente@bebegenial.com**.

Para continuar, debe aceptar nuestra Política de Privacidad, la cual puede consultar [aquí](https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49921).

**Al marcar esta casilla, usted acepta el tratamiento de sus datos conforme a lo descrito.**

*Marque la casilla para continuar:*
""")

# Si no acepta, no se muestra el formulario
if not acepto:
    st.stop()

# Diccionario para mapear ID a nombre del comercial
comerciales = {
    "0490": "Paula",
    "8971": "Pilar",
    "8949": "Lorena",
    "8870": "Sebastian",
    "7171": "Angelo",
    "9043": "Martha",
    "0640": "Edgar",
    "0080": "Estefania",
    "7863": "Eliana",
    "7509": "Sandra",
    "0048": "Nataly"
}

# Recolección de datos
st.header("✨ Recolección de datos")
nombre = st.text_input("Nombre del padre o representante legal:")
correo = st.text_input("Correo electrónico:")
telefono = st.text_input("Teléfono:")
id_comercial = st.selectbox("ID del comercial:", index=None ,options=list(comerciales.keys()))

# Validación de correo y teléfono
def validar_correo(correo):
    return "@" in correo and "." in correo.split("@")[-1]

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) >= 7

# Sección de preguntas
st.header("📝 Test de Inteligencias Múltiples")
inteligencias = [
    "Lingüística", "Lógico-Matemática", "Espacial",
    "Corporal-Kinestésica", "Musical", "Interpersonal", "Intrapersonal", "Naturalista"
]

preguntas = [
    # Lingüística
    "Disfruta que le lean cuentos o historias.",
    "Intenta contar lo que ve o lo que siente.",
    "Juega con sonidos, palabras o canciones.",
    "Usa gestos, sonidos o palabras para comunicarse.",
    # Lógico-Matemática
    "Le gusta clasificar objetos por color, forma o tamaño.",
    "Disfruta juegos de encajar, armar o resolver retos.",
    "Nota cuando algo cambia o no está como siempre.",
    "Explora relaciones de causa y efecto.",
    # Espacial
    "Reconoce espacios y lugares conocidos.",
    "Disfruta dibujar, armar rompecabezas o mirar imágenes.",
    "Observa detalles en su entorno.",
    "Usa el juego simbólico (casitas, carros, muñecos).",
    # Corporal-Kinestésica
    "Aprende mejor moviéndose y explorando.",
    "Disfruta correr, saltar, bailar o trepar.",
    "Expresa emociones con su cuerpo.",
    "Tiene buena coordinación para su edad.",
    # Musical
    "Reacciona positivamente a la música o sonidos.",
    "Tararea, canta o sigue ritmos.",
    "La música lo calma o lo activa.",
    "Reconoce canciones o sonidos familiares.",
    # Interpersonal
    "Busca interactuar con otros niños o adultos.",
    "Percibe emociones en los demás.",
    "Disfruta juegos en grupo.",
    "Muestra interés por ayudar o acompañar.",
    # Intrapersonal
    "Expresa lo que siente a su manera.",
    "A veces prefiere jugar solo.",
    "Tiene claras sus preferencias.",
    "Se siente seguro con rutinas.",
    # Naturalista
    "Muestra curiosidad por animales o plantas.",
    "Disfruta estar al aire libre.",
    "Observa cambios en la naturaleza.",
    "Cuida su entorno."
]

# Diccionario para almacenar respuestas
respuestas = {}

# Mostrar preguntas y opciones (sin valores numéricos y sin preselección)
for i, pregunta in enumerate(preguntas):
    respuestas[f"pregunta_{i+1}"] = st.radio(
        f"**{i+1}. {pregunta}**",
        options=["Nunca", "Rara vez", "A veces", "Siempre o casi siempre"],
        index=None,  # Evita que esté preseleccionado
        key=f"pregunta_{i+1}"
    )

# Botón para procesar resultados
procesado = st.button("Procesar resultados", key="boton_procesar_1")

if procesado:
    # Validar datos
    if not validar_correo(correo):
        st.error("Por favor, ingresa un correo electrónico válido.")
    elif not validar_telefono(telefono):
        st.error("Por favor, ingresa un número de teléfono válido.")
    elif any(respuesta is None for respuesta in respuestas.values()):
        st.error("Por favor, responde todas las preguntas.")
    elif id_comercial is None or id_comercial == "":
        st.error("Por favor, selecciona el ID de un comercial.")
    else:
        # Asignar valores numéricos según la respuesta seleccionada
        valores_respuestas = {
            "Nunca": 0,
            "Rara vez": 1,
            "A veces": 2,
            "Siempre o casi siempre": 3
        }

        # Calcular subtotales
        subtotales = {}
        for idx, inteligencia in enumerate(inteligencias):
            inicio = idx * 4
            fin = inicio + 4
            subtotales[inteligencia] = sum(
                valores_respuestas[respuestas[f"pregunta_{i+1}"]] for i in range(inicio, fin)
            )

        # Obtener el nombre del comercial a partir del ID seleccionado
        nombre_comercial = comerciales[id_comercial]

        # Guardar en Google Sheets
        guardar_en_google_sheets(nombre, correo, telefono, nombre_comercial, respuestas)

        # Mostrar resultados
        st.header("📊 Resultados")
        st.write("### Subtotales por inteligencia:")
        for inteligencia, puntaje in subtotales.items():
            st.write(f"- **{inteligencia}**: {puntaje}/12")

        # Gráfico de barras con etiquetas inclinadas
        fig, ax = plt.subplots(figsize=(10, 6))
        barras = ax.bar(subtotales.keys(), subtotales.values(), color=[
            "#9b59b6", "#3498db", "#2ecc71", "#e74c3c",
            "#f1c40f", "#e67e22", "#1abc9c", "#34495e"
        ])
        ax.set_ylabel("Puntuación")
        ax.set_title("Puntuación por Inteligencia")
        ax.bar_label(barras, labels=[f"{valor}" for valor in subtotales.values()], padding=3)
        plt.xticks(rotation=45, ha='right')  # Inclinar etiquetas a 45 grados
        st.pyplot(fig)

        # Gráfico general
        fig2, ax2 = plt.subplots(figsize=(8, 8))
        ax2.pie(subtotales.values(), labels=subtotales.keys(), autopct="%1.1f%%")
        ax2.set_title("Distribución de Inteligencias")
        st.pyplot(fig2)

        # Deshabilitar botón
        st.success("¡Resultados procesados y guardados con éxito!")
        st.button("Procesar resultados", disabled=True, key="boton_procesar_deshabilitado")

