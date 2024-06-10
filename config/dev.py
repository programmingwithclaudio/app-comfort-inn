from .default import *
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class Config:
    # Otras configuraciones por defecto
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Asignar la variable de entorno a la configuración
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')