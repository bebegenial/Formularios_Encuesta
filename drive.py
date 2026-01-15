import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from datetime import datetime
import pytz
import streamlit as st


# Cargar variables de entorno desde el archivo .env
load_dotenv()

def guardar_en_google_sheets(nombre, correo, telefono, comercial, respuestas):
    """
    Guarda los datos del test en una hoja de cálculo de Google Sheets.

    Args:
        nombre (str): Nombre del niño.
        correo (str): Correo electrónico.
        telefono (str): Teléfono.
        respuestas (dict): Diccionario con las respuestas del test.
    """
    # Configurar credenciales desde variables de entorno desde el archivo .env
    '''creds_dict = {
        "type": os.getenv("GOOGLE_SHEETS_TYPE"),
        "project_id": os.getenv("GOOGLE_SHEETS_PROJECT_ID"),
        "private_key_id": os.getenv("GOOGLE_SHEETS_PRIVATE_KEY_ID"),
        "private_key": os.getenv("GOOGLE_SHEETS_PRIVATE_KEY").replace('\\n', '\n'),
        "client_email": os.getenv("GOOGLE_SHEETS_CLIENT_EMAIL"),
        "client_id": os.getenv("GOOGLE_SHEETS_CLIENT_ID"),
        "auth_uri": os.getenv("GOOGLE_SHEETS_AUTH_URI"),
        "token_uri": os.getenv("GOOGLE_SHEETS_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("GOOGLE_SHEETS_AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("GOOGLE_SHEETS_CLIENT_X509_CERT_URL"),
        "universe_domain": "googleapis.com"
    }'''
    # Para utilizar desde streamlit
    creds_dict = {
        "type": st.secrets["GOOGLE_SHEETS_TYPE"],
        "project_id": st.secrets["GOOGLE_SHEETS_PROJECT_ID"],
        "private_key_id": st.secrets["GOOGLE_SHEETS_PRIVATE_KEY_ID"],
        "private_key": st.secrets["GOOGLE_SHEETS_PRIVATE_KEY"].replace('\\n', '\n'),
        "client_email": st.secrets["GOOGLE_SHEETS_CLIENT_EMAIL"],
        "client_id": st.secrets["GOOGLE_SHEETS_CLIENT_ID"],
        "auth_uri": st.secrets["GOOGLE_SHEETS_AUTH_URI"],
        "token_uri": st.secrets["GOOGLE_SHEETS_TOKEN_URI"],
        "auth_provider_x509_cert_url": st.secrets["GOOGLE_SHEETS_AUTH_PROVIDER_X509_CERT_URL"],
        "client_x509_cert_url": st.secrets["GOOGLE_SHEETS_CLIENT_X509_CERT_URL"],
        "universe_domain": "googleapis.com"
    }

    # Configuración de Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    # Abrir la hoja de cálculo usando el ID y el nombre de la pestaña
    spreadsheet = client.open_by_key(os.getenv("SPREADSHEET_ID"))
    sheet = spreadsheet.worksheet(os.getenv("GOOGLE_SHEETS_SPREADSHEET_NAME"))

    # Obtener la fecha y hora actual en la zona horaria de Colombia
    bogota_tz = pytz.timezone("America/Bogota")
    fecha_hora = datetime.now(bogota_tz).strftime("%d/%m/%Y %H:%M:%S")

    # Preparar los datos para guardar
    datos = [fecha_hora, nombre, correo, telefono, comercial] + [respuestas[f"pregunta_{i+1}"] for i in range(32)]

    # Guardar en Google Sheets
    sheet.append_row(datos)

