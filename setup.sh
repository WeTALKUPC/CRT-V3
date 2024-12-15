#!/bin/bash

# Instalar dependencias del sistema para Pillow
sudo apt-get update
sudo apt-get install -y zlib1g-dev libjpeg-dev

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias de Python
pip install -r requirements.txt
