# Usa una imagen base de Python con soporte mínimo
FROM python:3.12-slim

# Instalar dependencias del sistema necesarias para Pillow
RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libjpeg-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Crear un directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo requirements.txt
COPY requirements.txt .

# Actualizar pip e instalar dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar todo el código de la aplicación al contenedor
COPY . .

# Comando por defecto para ejecutar la aplicación
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
