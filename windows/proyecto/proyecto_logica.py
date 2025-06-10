from PySide6.QtWidgets import QDialog, QApplication, QMessageBox
import sys

# Importar la clase de UI generada
from window_proyecto import Ui_Window

# Importar el gestor de proyectos
from MySQLManagerProyecto import MySQLProyectosManager


class WindowProyecto(QDialog):
    def __init__(self, db_manager: MySQLProyectosManager):
        super().__init__()

        # Llamar a la UI que has generado
        self.ui = Ui_Window()
        self.ui.setupUi(self)

        # Guardar la referencia de MySQLManager
        self.db_manager = db_manager

        # Conectar el botón con la función para crear el proyecto
        print("Conectando el botón...")
        self.ui.boton_proyecto.clicked.connect(self.crear_proyecto)

    def crear_proyecto(self):
        """
        Función que se ejecuta cuando se presiona el botón 'Crear proyecto'.
        Recoge los valores de los QLineEdit y los inserta en la base de datos.
        """
        print("Botón presionado")  # Verificación de que el botón funciona correctamente

        # Obtener los datos de los QLineEdit
        autor = self.ui.entry_autor.text()
        nombre = self.ui.entry_nombre.text()
        descripcion = self.ui.entry_descripcion.text()

        if autor and nombre and descripcion:  # Verificar si los campos no están vacíos
            # Insertar el proyecto en la base de datos
            self.db_manager.insert_proyecto(autor, nombre, descripcion)
            QMessageBox.information(self, "Éxito", "Proyecto creado exitosamente.")
            self.limpiar_campos()  # Limpiar los campos después de guardar
        else:
            QMessageBox.critical(self, "Error", "Todos los campos son obligatorios.")

    def limpiar_campos(self):
        """Limpiar los campos de entrada después de guardar los datos."""
        self.ui.entry_autor.clear()
        self.ui.entry_nombre.clear()
        self.ui.entry_descripcion.clear()


# Crear la instancia de MySQLProyectosManager
db_manager = MySQLProyectosManager()

# Crear y mostrar la ventana del proyecto
if __name__ == "__main__":
    app = QApplication([])
    ventana = WindowProyecto(db_manager)
    ventana.show()
    app.exec()
