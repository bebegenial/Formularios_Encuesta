# Test de Inteligencias Múltiples - El Expreso de Leo 🚂

**Herramienta de observación para familias de niños de 2 a 6 años**, basada en la teoría de las Inteligencias Múltiples. Este test ayuda a reconocer cómo aprende, se expresa y se relaciona un niño, para acompañarlo mejor desde el juego y el afecto.

---

## 📌 Descripción
Este proyecto es una aplicación web desarrollada con **Streamlit** que permite a las familias responder un test sobre las inteligencias múltiples de sus hijos. Los resultados se visualizan en gráficos y se guardan automáticamente en una hoja de cálculo de Google Sheets, incluyendo datos de contacto y el comercial asignado.

---


## 📂 Estructura del proyecto
```bash
├── test.py    # Código principal de la aplicación

├── drive.py                 # Módulo para guardar datos en Google Sheets

├── .env                     # Variables de entorno (credenciales de Google)

└── README.md                # Este archivo
```

---

## 🛠 Requisitos
- Python 3.8 o superior
- Librerías requeridas:
  ```bash
  pip install streamlit pandas matplotlib gspread oauth2client python-dotenv pytz
  ```

---

## 📋 Configuración
### 1. Configurar Google Sheets

Crea una hoja de cálculo en Google Drive y comparte el enlace con el correo de servicio de tu proyecto.
Habilita la API de Google Sheets y descarga el archivo credentials.json desde Google Cloud Console.
Configura el archivo .env con las credenciales de Google y el ID de la hoja de cálculo:
```bash
# .env
GOOGLE_SHEETS_TYPE=service_account
GOOGLE_SHEETS_PROJECT_ID=tu_project_id
GOOGLE_SHEETS_PRIVATE_KEY_ID=tu_private_key_id
GOOGLE_SHEETS_PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\nTu_llave_privada\n-----END PRIVATE KEY-----\n
GOOGLE_SHEETS_CLIENT_EMAIL=tu_client_email
GOOGLE_SHEETS_CLIENT_ID=tu_client_id
GOOGLE_SHEETS_AUTH_URI=https://accounts.google.com/o/oauth2/auth
GOOGLE_SHEETS_TOKEN_URI=https://oauth2.googleapis.com/token
GOOGLE_SHEETS_AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
GOOGLE_SHEETS_CLIENT_X509_CERT_URL=tu_client_x509_cert_url
SPREADSHEET_ID=ID_de_tu_hoja_de_cálculo  # Ejemplo: 1DRhxDIDoihqafw7A8
GOOGLE_SHEETS_SPREADSHEET_NAME=Nombre_de_tu_hoja_de_cálculo # Ejemplo: Hoja1 
```



### 2. Configurar la hoja de cálculo
Asegúrate de que la hoja de cálculo tenga los siguientes encabezados en la primera fila:
```bash
Fecha y Hora | Nombre del padre o representante legal | Correo electrónico | Teléfono | Comercial | P1 | P2 | P3 | ... | P32
```
---
## 🚀 Ejecución

1. Clona este repositorio o descarga los archivos.
```bash
https://github.com/bebegenial/Formularios_Encuesta.git
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run test.py
```

4. Abre el enlace que aparece en la terminal para interactuar con el test.

---

## 📝 Uso

Aceptar el aviso de privacidad (obligatorio para continuar).
Ingresar los datos del padre o representante legal (nombre, correo, teléfono y ID del comercial).
Responder todas las preguntas del test (32 preguntas sobre las 8 inteligencias múltiples).
Presionar el botón "Procesar resultados" para ver los gráficos y guardar los datos.

---

## 📊 Funcionalidades

Test responsivo: Adaptado para tablets y celulares.
Validación de datos: Correo, teléfono y respuestas obligatorias.
Gráficos interactivos: Barras y pastel para visualizar los resultados.
Registro automático: Los datos se guardan en Google Sheets con fecha, hora y nombre del comercial.
Protección de datos: Cumple con la Ley 1581 de 2012 (Habeas Data).

---

## 📄 Licencia
Este proyecto es de uso interno para Editorial Bebe Genial. 

---

## 📧 Soporte
Para preguntas o soporte técnico, contacta a:
servicioalcliente@bebegenial.com


---
### **Notas adicionales:**
- **Seguridad**: El archivo `.env` debe estar en `.gitignore` para proteger las credenciales.
- **Zona horaria**: La fecha y hora se registran en la zona horaria de Colombia (`America/Bogota`).
- **Requisitos legales**: El aviso de privacidad cumple con la normativa colombiana.

