from PySide6.QtWidgets import QDialog, QApplication, QMessageBox
import sys

# Importar la clase de UI generada
from window_recordatorio import Ui_Window

# Importar el gestor de recordatorios
from MySQLManagerRecordatorio import MySQLRecordatoriosManager


class WindowRecordatorio(QDialog):
    def __init__(self, db_manager: MySQLRecordatoriosManager):
        super().__init__()

        # Llamar a la UI que has generado
        self.ui = Ui_Window()
        self.ui.setupUi(self)

        # Guardar la referencia de MySQLManager
        self.db_manager = db_manager

        # Conectar el botón con la función para crear el recordatorio
        print("Conectando el botón...")
        self.ui.boton_recordatorio.clicked.connect(self.crear_recordatorio)

    def crear_recordatorio(self):
        """
        Función que se ejecuta cuando se presiona el botón 'Crear recordatorio'.
        Recoge los valores de los QLineEdit y los inserta en la base de datos.
        """
        print("Botón presionado")  # Verificación de que el botón funciona correctamente

        # Obtener los datos de los QLineEdit
        nombre = self.ui.entry_nombre.text()
        fecha = self.ui.entry_fecha.text()
        hora = self.ui.entry_hora.text()

        if nombre and fecha and hora:  # Verificar si los campos no están vacíos
            # Insertar el recordatorio en la base de datos
            self.db_manager.insert_recordatorio(nombre, fecha, hora)
            QMessageBox.information(self, "Éxito", "Recordatorio creado exitosamente.")
            self.limpiar_campos()  # Limpiar los campos después de guardar
        else:
            QMessageBox.critical(self, "Error", "Todos los campos son obligatorios.")

    def limpiar_campos(self):
        """Limpiar los campos de entrada después de guardar los datos."""
        self.ui.entry_nombre.clear()
        self.ui.entry_fecha.clear()
        self.ui.entry_hora.clear()


# Crear la instancia de MySQLRecordatoriosManager
db_manager = MySQLRecordatoriosManager()

# Crear y mostrar la ventana del recordatorio
if __name__ == "__main__":
    app = QApplication([])
    ventana = WindowRecordatorio(db_manager)
    ventana.show()
    app.exec()
