from PySide6.QtWidgets import QDialog, QApplication, QMessageBox
import sys

# Importar la clase MySQLSuministrosManager

from window_suministro import Ui_Window

from windows.suministro.MySQLManager import MySQLSuministrosManager




class WindowSuministro(QDialog):
    def __init__(self, db_manager: MySQLSuministrosManager):
        super().__init__()

        # Llamar a la UI que has generado
        self.ui = Ui_Window()
        self.ui.setupUi(self)

        # Guardar la referencia de MySQLManager
        self.db_manager = db_manager

        # Conectar el botón con la función para crear el suministro
        print("Conectando el botón...")
        
        

    def crear_suministro(self):
        print("Botón presionado")
        """
        Función que se ejecuta cuando se presiona el botón 'Crear suministro'.
        Recoge los valores de los QLineEdit y los inserta en la base de datos.
        """
        print("Botón presionado")  # Verificación de que el botón funciona correctamente
        # Obtener los datos de los QLineEdit
        nombre = self.ui.entry_nombre.text()
        ubicacion = self.ui.entry_ubicacion.text()
        stock = int(self.ui.entry_stock.text())  # Asumimos que es un número entero
        peso = float(self.ui.entry_peso.text())  # Asumimos que es un número decimal

        if nombre and ubicacion:  # Verificar si los campos no están vacíos
            # Insertar el suministro en la base de datos
            self.db_manager.insert_suministro(nombre, ubicacion, stock, peso)
            QMessageBox.information(self, "Éxito", "Suministro creado exitosamente.")
            self.limpiar_campos()  # Limpiar los campos después de guardar
        else:
            QMessageBox.critical(self, "Error", "Todos los campos son obligatorios.")


    def limpiar_campos(self):
        """Limpiar los campos de entrada después de guardar los datos."""
        self.ui.entry_nombre.clear()
        self.ui.entry_ubicacion.clear()
        self.ui.entry_stock.clear()
        self.ui.entry_peso.clear()


# Crear la instancia de MySQLSuministrosManager
db_manager = MySQLSuministrosManager()

# Crear y mostrar la ventana del suministro
if __name__ == "__main__":
    app = QApplication([])
    ventana = WindowSuministro(db_manager)
    
    ventana.show()
    app.exec()
