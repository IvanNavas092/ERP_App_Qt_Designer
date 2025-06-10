from PySide6.QtWidgets import QDialog, QApplication, QMessageBox
import sys

# Importar la clase MySQLInformesManager
from window_informe import Ui_Dialog
from windows.informe.MySQLManagerInforme import MySQLInformesManager
from windows.informe.window_informe import Ui_Dialog

class WindowInformes(QDialog):
    def __init__(self, db_manager: MySQLInformesManager):
        super().__init__()

        # Llamar a la UI que has generado
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Guardar la referencia de MySQLManager
        self.db_manager = db_manager

        # Conectar el botón con la función para crear el informe
        print("Conectando el botón...")
        self.ui.boton_informe.clicked.connect(self.crear_informe)

    def crear_informe(self):
        print("Botón presionado")
        """
        Función que se ejecuta cuando se presiona el botón 'Crear Informe'.
        Recoge los valores de los QLineEdit y los inserta en la base de datos.
        """
        # Obtener los datos de los QLineEdit
        nombre = self.ui.entry_nombre.text()
        autor = self.ui.entry_autor.text()
        descripcion = self.ui.entry_descripcion.text()

        if nombre and autor and descripcion:  # Verificar si los campos no están vacíos
            # Insertar el informe en la base de datos
            self.db_manager.insert_informe(nombre, autor, descripcion)
            QMessageBox.information(self, "Éxito", "Informe creado exitosamente.")
            self.limpiar_campos()  # Limpiar los campos después de guardar
        else:
            QMessageBox.critical(self, "Error", "Todos los campos son obligatorios.")

    def limpiar_campos(self):
        """Limpiar los campos de entrada después de guardar los datos."""
        self.ui.entry_nombre.clear()
        self.ui.entry_autor.clear()
        self.ui.entry_descripcion.clear()

# Crear la instancia de MySQLInformesManager
db_manager = MySQLInformesManager()

# Crear y mostrar la ventana de informes
if __name__ == "__main__":
    app = QApplication([])
    ventana = WindowInformes(db_manager)
    
    ventana.show()
    app.exec()
