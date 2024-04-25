from MongoActions import MongoActions
from dotenv import load_dotenv
import os

class Main:
    def __init__(self):
        # Cargar las variables de entorno al instanciar la clase
        load_dotenv()

        # Obtener las variables de entorno necesarias
        self.connection_string = os.getenv("CONNECTION_STRING")
        self.database_name = os.getenv("DATABASE_NAME")
        self.collection_name = os.getenv("COLLECTION_NAME")

        # Crear una instancia de MongoActions
        self.actions = MongoActions(self.connection_string, self.database_name, self.collection_name)

    def run(self):
        # Ejecutar las acciones necesarias
        self.actions()

if __name__ == "__main__":
    main = Main()
    main.run()
