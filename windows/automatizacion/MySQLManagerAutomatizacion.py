import mysql.connector
from mysql.connector import Error

class MySQLAutomatizacionesManager:
    def __init__(self):
        """
        Inicializa la conexión a MySQL y selecciona la base de datos y tabla.
        """
        self.connection = None
        self.cursor = None
        self.db_name = "acceso"  # Nombre de la base de datos
        self.table_name = "automatizaciones"  # Nombre de la tabla
        self.connect_to_mysql(
            host="localhost",      # Dirección del servidor MySQL
            user="root",           # Usuario para autenticar
            password="1234"  # Contraseña para autenticar
        )

    def connect_to_mysql(self, host: str, user: str, password: str):
        """
        Establece una conexión con el servidor MySQL.
        """
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=self.db_name
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("Conexión a MySQL exitosa.")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            raise

    def insert_automatizacion(self, destinatarios: str, campaña: str, envio: str):
        """
        Inserta una automatización en la tabla.
        :param destinatarios: Lista de destinatarios.
        :param campaña: Nombre de la campaña.
        :param envio: Fecha de envío (YYYY-MM-DD).
        :return: El id de la automatización insertada.
        """
        query = f"INSERT INTO {self.table_name} (destinatarios, campaña, envio) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (destinatarios, campaña, envio))
        self.connection.commit()  # Commitear la transacción
        print("Automatización insertada con éxito.")
        return self.cursor.lastrowid  # Devuelve el ID de la automatización insertada

    def find_automatizaciones(self, campaña: str = None):
        """
        Encuentra automatizaciones en la tabla.
        :param campaña: Nombre de la campaña (opcional).
        :return: Lista de automatizaciones encontradas.
        """
        try:
            if campaña:
                query = f"SELECT * FROM {self.table_name} WHERE campaña = %s"
                self.cursor.execute(query, (campaña,))
            else:
                query = f"SELECT * FROM {self.table_name}"
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error al buscar automatizaciones: {e}")
            return []

    def update_automatizacion(self, campaña: str, new_values: dict):
        """
        Actualiza una automatización en la tabla.
        :param campaña: Nombre de la campaña a actualizar.
        :param new_values: Diccionario con los nuevos valores.
        :return: Número de registros modificados.
        """
        try:
            set_clause = ", ".join([f"{k} = %s" for k in new_values.keys()])
            query = f"UPDATE {self.table_name} SET {set_clause} WHERE campaña = %s"
            self.cursor.execute(query, tuple(new_values.values()) + (campaña,))
            self.connection.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f"Error al actualizar la automatización: {e}")
            return 0

    def delete_automatizacion(self, campaña: str):
        """
        Elimina una automatización de la tabla.
        :param campaña: Nombre de la campaña a eliminar.
        :return: Número de registros eliminados.
        """
        try:
            query = f"DELETE FROM {self.table_name} WHERE campaña = %s"
            self.cursor.execute(query, (campaña,))
            self.connection.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f"Error al eliminar la automatización: {e}")
            return 0

    def close_connection(self):
        """
        Cierra la conexión a MySQL.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Conexión a MySQL cerrada.")
