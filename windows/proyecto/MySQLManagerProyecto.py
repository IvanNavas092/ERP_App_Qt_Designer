import mysql.connector
from mysql.connector import Error

class MySQLProyectosManager:
    def __init__(self):
        """
        Inicializa la conexión a MySQL y selecciona la base de datos y tabla.
        """
        self.connection = None
        self.cursor = None
        self.db_name = "acceso"  # Nombre de la base de datos
        self.table_name = "proyectos"  # Nombre de la tabla
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

    def insert_proyecto(self, autor: str, nombre: str, descripcion: str):
        """
        Inserta un proyecto en la tabla.
        :param autor: Autor del proyecto.
        :param nombre: Nombre del proyecto.
        :param descripcion: Descripción del proyecto.
        :return: El id del proyecto insertado.
        """
        query = f"INSERT INTO {self.table_name} (autor, nombre, descripcion) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (autor, nombre, descripcion))
        self.connection.commit()  # Commitear la transacción
        print("Proyecto insertado con éxito.")
        return self.cursor.lastrowid  # Devuelve el ID del proyecto insertado

    def find_proyectos(self, nombre: str = None):
        """
        Encuentra proyectos en la tabla.
        :param nombre: Nombre del proyecto (opcional).
        :return: Lista de proyectos encontrados.
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
            print(f"Error al buscar proyectos: {e}")
            return []

    def update_proyecto(self, nombre: str, new_values: dict):
        """
        Actualiza un proyecto en la tabla.
        :param nombre: Nombre del proyecto a actualizar.
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
            print(f"Error al actualizar el proyecto: {e}")
            return 0

    def delete_proyecto(self, nombre: str):
        """
        Elimina un proyecto de la tabla.
        :param nombre: Nombre del proyecto a eliminar.
        :return: Número de registros eliminados.
        """
        try:
            query = f"DELETE FROM {self.table_name} WHERE nombre = %s"
            self.cursor.execute(query, (nombre,))
            self.connection.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f"Error al eliminar el proyecto: {e}")
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
