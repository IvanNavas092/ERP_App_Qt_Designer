from PySide6.QtWidgets import QDialog, QApplication, QMessageBox
import sys

# Importar la clase de UI generada
from window_auto import Ui_Dialog_A

# Importar el gestor de automatizaciones
from MySQLManagerAutomatizacion import MySQLAutomatizacionesManager


class WindowAutomatizacion(QDialog):
    def __init__(self, db_manager: MySQLAutomatizacionesManager):
        super().__init__()

        # Llamar a la UI que has generado
        self.ui = Ui_Dialog_A()
        self.ui.setupUi(self)

        # Guardar la referencia de MySQLManager
        self.db_manager = db_manager

        # Conectar el botón con la función para crear la automatización
        print("Conectando el botón...")
        self.ui.boton_automatizacion.clicked.connect(self.crear_automatizacion)

    def crear_automatizacion(self):
        """
        Función que se ejecuta cuando se presiona el botón 'Crear automatización'.
        Recoge los valores de los QLineEdit y los inserta en la base de datos.
        """
        print("Botón presionado")  # Verificación de que el botón funciona correctamente

        # Obtener los datos de los QLineEdit
        destinatarios = self.ui.entry_destinatarios.text()
        campaña = self.ui.entry_campaña.text()
        envio = self.ui.entry_envio.text()

        if destinatarios and campaña and envio:  # Verificar si los campos no están vacíos
            # Insertar la automatización en la base de datos
            self.db_manager.insert_automatizacion(destinatarios, campaña, envio)
            QMessageBox.information(self, "Éxito", "Automatización creada exitosamente.")
            self.limpiar_campos()  # Limpiar los campos después de guardar
        else:
            QMessageBox.critical(self, "Error", "Todos los campos son obligatorios.")

    def limpiar_campos(self):
        """Limpiar los campos de entrada después de guardar los datos."""
        self.ui.entry_destinatarios.clear()
        self.ui.entry_campaña.clear()
        self.ui.entry_envio.clear()


# Crear la instancia de MySQLAutomatizacionesManager
db_manager = MySQLAutomatizacionesManager()

# Crear y mostrar la ventana de automatización
if __name__ == "__main__":
    app = QApplication([])
    ventana = WindowAutomatizacion(db_manager)
    ventana.show()
    app.exec()
