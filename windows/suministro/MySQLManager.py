import mysql.connector
from mysql.connector import Error


class MySQLSuministrosManager:
    def __init__(self):
        """
        Inicializa la conexión a MySQL y selecciona la base de datos y tabla.
        """
        self.connection = None
        self.cursor = None
        self.db_name = "acceso"  # Nombre de la base de datos
        self.table_name = "suministros"  # Nombre de la tabla
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

    def insert_suministro(self, nombre: str, ubicacion: str, stock: int, peso: float):
        """
        Inserta un suministro en la tabla.
        :param nombre: Nombre del suministro.
        :param ubicacion: Ubicación del suministro.
        :param stock: Cantidad en stock.
        :param peso: Peso del suministro.
        :return: El id del suministro insertado.
        """
        query = f"INSERT INTO {self.table_name} (nombre, ubicacion, stock, peso) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (nombre, ubicacion, stock, peso))
        self.connection.commit()  # Commitear la transacción
        print("Suministro insertado con éxito.")
        return self.cursor.lastrowid  # Devuelve el ID del suministro insertado

    def find_suministros(self, nombre: str = None):
        """
        Encuentra suministros en la tabla.
        :param nombre: Nombre del suministro (opcional).
        :return: Lista de suministros encontrados.
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
            print(f"Error al buscar suministros: {e}")
            return []

    def update_suministro(self, nombre: str, new_values: dict):
        """
        Actualiza un suministro en la tabla.
        :param nombre: Nombre del suministro a actualizar.
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
            print(f"Error al actualizar el suministro: {e}")
            return 0

    def delete_suministro(self, nombre: str):
        """
        Elimina un suministro de la tabla.
        :param nombre: Nombre del suministro a eliminar.
        :return: Número de registros eliminados.
        """
        try:
            query = f"DELETE FROM {self.table_name} WHERE nombre = %s"
            self.cursor.execute(query, (nombre,))
            self.connection.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f"Error al eliminar el suministro: {e}")
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
