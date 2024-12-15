#!/bin/bash

# Actualizar el sistema e instalar dependencias del sistema necesarias para Pillow
sudo apt-get update
sudo apt-get install -y zlib1g-dev

# Actualizar pip antes de instalar dependencias de Python
pip install --upgrade pip

# Instalar dependencias de Python especificadas en requirements.txt
pip install -r requirements.txt
