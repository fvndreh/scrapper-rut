# scrapper-rut
Este proyecto proporciona una API para validar y obtiene información relacionada utilizando una API externa devolviendo un objeto JSON con la información obtenida.

## Características

- Validación y formato de RUT.
- Obtención de datos desde una API externa basada en el RUT validado.

## Requisitos

- Python 3.x
- Flask
- cloudscraper
- BeautifulSoup
- Requests

## Configuración

### 1. Clonar el repositorio

git clone https://github.com/fvndreh/scrapper-rut

cd scrapper-rut

### 2. Crear un entorno virtual

python -m venv venv

### 3. Instalar dependencias

pip install -r requirements.txt

### 4. Ejecutar la aplicación

py run.py

### Uso

Endpoint: /rut
Este endpoint permite validar y formatear un RUT, y obtener datos de una API externa en formato JSON.

Método: GET
URL: /rut?rut=<RUT>
Reemplaza <RUT> con el RUT que deseas validar (sin puntos y con guion, por ejemplo, 11111111-1).
