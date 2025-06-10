import mysql.connector
from mysql.connector import Error

class MySQLInformesManager:
    def __init__(self):
        """
        Inicializa la conexión a MySQL y selecciona la base de datos y tabla.
        """
        self.connection = None
        self.cursor = None
        self.db_name = "acceso"  # Nombre de la base de datos
        self.table_name = "informes"  # Nombre de la tabla
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

    def insert_informe(self, nombre: str, autor: str, descripcion: str):
        """
        Inserta un informe en la tabla.
        :param nombre: Nombre del informe.
        :param autor: Autor del informe.
        :param descripcion: Descripción del informe.
        :return: El id del informe insertado.
        """
        query = f"INSERT INTO {self.table_name} (nombre, autor, descripcion) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (nombre, autor, descripcion))
        self.connection.commit()  # Commitear la transacción
        print("Informe insertado con éxito.")
        return self.cursor.lastrowid  # Devuelve el ID del informe insertado

    def find_informes(self, nombre: str = None):
        """
        Encuentra informes en la tabla.
        :param nombre: Nombre del informe (opcional).
        :return: Lista de informes encontrados.
        """
        try:
            if nombre:
                query = f"SELECT * FROM {self.table_name} WHERE nombre = %s"
                self.cursor.execute(query, (nombre,))
            else:
                query = f"SELECT * FROM {self.table_name}"
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error al buscar informes: {e}")
            return []

    def update_informe(self, nombre: str, new_values: dict):
        """
        Actualiza un informe en la tabla.
        :param nombre: Nombre del informe a actualizar.
        :param new_values: Diccionario con los nuevos valores.
        :return: Número de registros modificados.
        """
        try:
            set_clause = ", ".join([f"{k} = %s" for k in new_values.keys()])
            query = f"UPDATE {self.table_name} SET {set_clause} WHERE nombre = %s"
            self.cursor.execute(query, tuple(new_values.values()) + (nombre,))
            self.connection.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f"Error al actualizar el informe: {e}")
            return 0

    def delete_informe(self, nombre: str):
        """
        Elimina un informe de la tabla.
        :param nombre: Nombre del informe a eliminar.
        :return: Número de registros eliminados.
        """
        try:
            query = f"DELETE FROM {self.table_name} WHERE nombre = %s"
            self.cursor.execute(query, (nombre,))
            self.connection.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f"Error al eliminar el informe: {e}")
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
