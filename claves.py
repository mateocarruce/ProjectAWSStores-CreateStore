import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Claves específicas que quieres revisar
claves_interes = ['DB_USER', 'DB_PASSWORD', 'DB_SERVER', 'DB_NAME']

for clave in claves_interes:
    valor = os.getenv(clave)
    print(f"{clave}: {valor}")
