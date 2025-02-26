# API REST de OCR

## Descripción

Esta API REST permite recibir una imagen codificada en formato base64, la cual es procesada mediante OpenCV y EasyOCR para extraer el texto contenido en la imagen como una cadena de caracteres.

---

## Características

- Decodificacion de imagenes en formato base64 con OpenCV
- Extraccion de texto mediante EasyOCR.

---

## Tecnologías Utilizadas

- **Fastapi**

---

## Instalación

### Requisitos Previos
- Fastapi (v0.115.8 o superior)
- Uvicorn (v0.34.0 o superior)
- python y pip instalado

### Pasos

1. Clona este repositorio:
   git clone https://github.com/shaitansix/OCR_Backend.git
2. Entra en el directorio del proyecto:
   cd server
3. Instala las dependencias:
   pip install -r requirements.txt
5. Inicia el servidor:
   py main.py