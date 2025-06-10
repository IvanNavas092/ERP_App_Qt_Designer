import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QDialog, QMessageBox
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QCategoryAxis, QValueAxis, QBarSet, QBarSeries, QBarCategoryAxis, QPieSeries
from PySide6.QtGui import QPainter
from interfaz import Ui_MainWindow  

from windows.suministro.window_suministro import Ui_Window
from windows.informe.window_informe import Ui_Dialog
from windows.filtrar.window_filtrar import Ui_Dialog_F
from windows.recordatorio.window_recordatorio import Ui_main
from windows.proyecto.window_proyecto import Ui_Dialog_P
from windows.automatizacion.window_auto import Ui_Dialog_A
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFileDialog
import shutil
import os
import pandas as pd




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # Crear frame para el gráfico en Inventory
        self.graphic = QFrame(self.Inventory)
        self.graphic.setObjectName(u"graphic")
        self.graphic.setFrameShape(QFrame.Shape.StyledPanel)
        self.graphic.setFrameShadow(QFrame.Shadow.Raised)
        layout_inventory = QVBoxLayout(self.graphic)
        self.graphic.setLayout(layout_inventory)
        self.GRID.addWidget(self.graphic, 1, 1, 1, 1)  # Añadir frame al GRID layout

        # Agregar gráficos genéricos, pero sin datos ficticios
        self.agregar_grafico_generico(
            datos=[],  # Vacío por ahora, se actualizará después
            titulo="Balance de Dinero Mensual - 2024",
            eje_y_rango=(10000, 22000),
            frame=self.graphic
        )

        # Agregar gráfico lineal en Buys
        frame_lineal = self.Buys.findChild(QFrame, "frame_lineal")
        self.agregar_grafico_generico(
            datos=[],  # Vacío por ahora, se actualizará después
            titulo="Gastos de Dinero",
            eje_y_rango=(0, 6000),
            frame=frame_lineal
        )

        # Agregar gráfico de barras en Finance
        frame_balance = self.finance.findChild(QFrame, "frame_balance")
        self.agregar_grafico_barras(
            datos=[],  # Vacío por ahora, se actualizará después
            titulo="Balance Financiero - 2024",
            eje_y_rango=(0, 10000),
            frame=frame_balance
        )

        # Agregar gráficos en Marketing Electrónico
        frame_grafico_1 = self.marketing.findChild(QFrame, "frame_grafico_1")
        self.agregar_grafico_pie(
            datos={},  # Vacío por ahora, se actualizará después
            titulo="Estado de Campañas",
            frame=frame_grafico_1
        )

        frame_grafico_2 = self.marketing.findChild(QFrame, "frame_grafico_2")
        self.agregar_grafico_barras(
            datos=[],  # Vacío por ahora, se actualizará después
            titulo="Dinero ganado con automatizaciones Mensuales",
            eje_y_rango=(0, 1200),
            frame=frame_grafico_2
        )

        # Conectar señales para las ventanas
        self.crear_suministro.clicked.connect(self.abrir_ventana_suministro)
        self.crear_informe.clicked.connect(self.abrir_ventana_informe)
        self.crear_informe_3.clicked.connect(self.abrir_ventana_informe)
        self.crear_informe_4.clicked.connect(self.abrir_ventana_informe)
        self.crear_informe_5.clicked.connect(self.abrir_ventana_informe)
        self.boton_filtrar.clicked.connect(self.abrir_ventana_filtrar)
        self.boton_filtrar_2.clicked.connect(self.abrir_ventana_filtrar)
        self.boton_filtrar_3.clicked.connect(self.abrir_ventana_filtrar)
        self.crear_informe_2.clicked.connect(self.abrir_ventana_informe)
        self.crear_informe_7.clicked.connect(self.abrir_ventana_informe)
        self.crear_recordatorio.clicked.connect(self.abrir_ventana_recortatorio)
        self.crear_recordatorio_4.clicked.connect(self.abrir_ventana_recortatorio)
        self.crear_proyecto.clicked.connect(self.abrir_ventana_proyecto)
        self.crear_auto.clicked.connect(self.abrir_ventana_auto)
        self.boton_actualizacion.clicked.connect(self.mostrar_mensaje_actualizacion)
        # Logica
        self.descargar_documentacion.clicked.connect(self.guardar_documentacion)
        self.boton_subir_archivo.clicked.connect(self.subir_archivo)
        

    def abrir_ventana_filtrar(self):
        self.ventana_filtrar = QDialog()
        self.ui_filtrar = Ui_Dialog_F()  
        self.ui_filtrar.setupUi(self.ventana_filtrar)  
        self.ventana_filtrar.exec()

    def abrir_ventana_auto(self):
        self.ventana_auto = QDialog()
        self.ui_auto = Ui_Dialog_A()  
        self.ui_auto.setupUi(self.ventana_auto)  
        self.ventana_auto.exec()

    def abrir_ventana_proyecto(self):
        self.ventana_proyecto = QDialog()
        self.ui_proyecto = Ui_Dialog_P()  
        self.ui_proyecto.setupUi(self.ventana_proyecto)  
        self.ventana_proyecto.exec()

    def abrir_ventana_suministro(self):
        self.ventana_suministro = QDialog() 
        self.ui_suministro = Ui_Window()  
        self.ui_suministro.setupUi(self.ventana_suministro)  
        self.ventana_suministro.exec()

    def abrir_ventana_informe(self):
        self.ventana_informe = QDialog() 
        self.ui_informe = Ui_Dialog()  
        self.ui_informe.setupUi(self.ventana_informe)  
        self.ventana_informe.exec()

    def abrir_ventana_recortatorio(self):
        self.ventana_recortatorio = QDialog() 
        self.ui_recortatorio = Ui_main()  
        self.ui_recortatorio.setupUi(self.ventana_recortatorio)  
        self.ventana_recortatorio.exec()

    def agregar_grafico_generico(self, datos, titulo, eje_y_rango, frame):
        """Función genérica para agregar gráficos a un QFrame."""
        layout = frame.layout() or QVBoxLayout(frame)
        frame.setLayout(layout)

        series = QLineSeries()
        for x, y in enumerate(datos):
            series.append(x, y)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(titulo)

        axis_x = QCategoryAxis()
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        for i, mes in enumerate(meses[:len(datos)]):
            axis_x.append(mes, i)

        axis_y = QValueAxis()
        axis_y.setRange(*eje_y_rango)
        axis_y.setLabelFormat("$%d")

        chart.setAxisX(axis_x, series)
        chart.setAxisY(axis_y, series)
        chart.legend().setVisible(False)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)
        layout.addWidget(chart_view)

    def agregar_grafico_barras(self, datos, titulo, eje_y_rango, frame):
        """Función para agregar un gráfico de barras a un QFrame."""
        layout = frame.layout() or QVBoxLayout(frame)
        frame.setLayout(layout)

        bar_set = QBarSet("2024")
        bar_set.append(datos)

        bar_series = QBarSeries()
        bar_series.append(bar_set)

        chart = QChart()
        chart.addSeries(bar_series)
        chart.setTitle(titulo)

        axis_x = QBarCategoryAxis()
        categorias = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
        axis_x.append(categorias[:len(datos)])

        axis_y = QValueAxis()
        axis_y.setRange(*eje_y_rango)
        axis_y.setLabelFormat("$%d")

        chart.setAxisX(axis_x, bar_series)
        chart.setAxisY(axis_y, bar_series)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)
        layout.addWidget(chart_view)

    def agregar_grafico_pie(self, datos, titulo, frame):
        """Función para agregar un gráfico de pastel a un QFrame."""
        layout = frame.layout() or QVBoxLayout(frame)
        frame.setLayout(layout)

        series = QPieSeries()
        for categoria, valor in datos.items():
            series.append(categoria, valor)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(titulo)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        for i in reversed(range(layout.count())):
            widget_to_remove = layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)
        layout.addWidget(chart_view)

    def mostrar_mensaje_actualizacion(self):
        """Muestra un mensaje indicando que la función estará disponible en el futuro."""
        mensaje = QMessageBox(self)
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setWindowTitle("Actualización")
        mensaje.setText("Esta función estará habilitada en la siguiente actualización.")
        mensaje.setStandardButtons(QMessageBox.Ok)
        mensaje.exec()

    def guardar_documentacion(self):
        # Nombre del archivo PDF original
        ruta_original_pdf = "Instrucciones_para_ingresar_archivos.pdf"  # Cambia esta ruta según corresponda
        
        # Extraer solo el nombre del archivo sin la ruta
        nombre_pdf = os.path.basename(ruta_original_pdf)
        
        # Abrir un cuadro de diálogo para guardar el archivo PDF, con el nombre por defecto del archivo original
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar Documentación", nombre_pdf, "Archivos PDF (*.pdf)")
        
        if ruta:
            if not ruta.endswith('.pdf'):
                ruta += '.pdf'  # Asegurarse de que termine con .pdf

            try:
                # Copiar el archivo PDF a la ruta seleccionada
                shutil.copy(ruta_original_pdf, ruta)
                
                QMessageBox.information(self, "Éxito", f"Documentación guardada en: {ruta}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo:\n{str(e)}")

    def subir_archivo(self):
        # Abrir cuadro de diálogo para seleccionar archivo CSV o TXT
        ruta, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar Archivo", "", "Archivos CSV (*.csv);;Archivos de Texto (*.txt)"
        )
        if ruta:
            try:
                # Si es CSV, cargarlo con pandas
                if ruta.endswith('.csv'):
                    datos = pd.read_csv(ruta)

                    # Procesar los datos del CSV
                    self.procesar_datos_csv(datos)

                    QMessageBox.information(self, "Archivo Cargado", f"Archivo CSV cargado: {ruta}")

                # Si es TXT, leer el archivo como texto
                elif ruta.endswith('.txt'):
                    with open(ruta, 'r') as archivo:
                        contenido = archivo.read()
                        QMessageBox.information(self, "Archivo Cargado", f"Archivo TXT cargado:\n{contenido[:100]}...")  # Muestra los primeros 100 caracteres

            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo cargar el archivo:\n{str(e)}")


    def procesar_datos_csv(self, datos_csv):
        """Procesa los datos del CSV y genera los gráficos."""
        try:
            # Limpiar los nombres de las columnas eliminando espacios extra
            datos_csv.columns = datos_csv.columns.str.strip()
            
            # Verificar las cabeceras del CSV
            print("Cabeceras del archivo CSV:", datos_csv.columns)

            # Imprimir las primeras filas de datos para verificar
            print("Primeras filas de datos:")
            print(datos_csv.head())

            # Verificar que todas las columnas esperadas están presentes
            if "Balance de Dinero Mensual" not in datos_csv.columns:
                raise ValueError("La columna 'Balance de Dinero Mensual' no se encuentra en el CSV.")
            if "Gastos de Dinero" not in datos_csv.columns:
                raise ValueError("La columna 'Gastos de Dinero' no se encuentra en el CSV.")
            if "Balance Financiero" not in datos_csv.columns:
                raise ValueError("La columna 'Balance Financiero' no se encuentra en el CSV.")
            if "Balance de Campañas" not in datos_csv.columns:
                raise ValueError("La columna 'Balance de Campañas' no se encuentra en el CSV.")
            if "Dinero Ganado con Automatizaciones" not in datos_csv.columns:
                raise ValueError("La columna 'Dinero Ganado con Automatizaciones' no se encuentra en el CSV.")

            # Obtener los datos de cada columna
            balance_mensual = datos_csv['Balance de Dinero Mensual'].tolist()
            gastos = datos_csv['Gastos de Dinero'].tolist()
            balance_financiero = datos_csv['Balance Financiero'].tolist()
            balance_campanas = datos_csv['Balance de Campañas'].tolist()
            dinero_automatizaciones = datos_csv['Dinero Ganado con Automatizaciones'].tolist()

            # Verifica que las listas no estén vacías
            if not balance_mensual or not gastos or not balance_financiero or not balance_campanas or not dinero_automatizaciones:
                raise ValueError("Los datos del CSV no pueden estar vacíos.")

            # Generar gráficos con los datos procesados
            self.agregar_grafico_generico(
                datos=balance_mensual,
                titulo="Balance de Dinero Mensual",
                eje_y_rango=(min(balance_mensual), max(balance_mensual)),
                frame=self.graphic
            )

            frame_lineal = self.Buys.findChild(QFrame, "frame_lineal")
            self.agregar_grafico_generico(
                datos=gastos,
                titulo="Gastos de Dinero",
                eje_y_rango=(0, max(gastos) + 500),
                frame=frame_lineal
            )

            frame_balance = self.finance.findChild(QFrame, "frame_balance")
            self.agregar_grafico_generico(
                datos=balance_financiero,
                titulo="Balance Financiero",
                eje_y_rango=(0, max(balance_financiero) + 500),
                frame=frame_balance
            )

            frame_grafico_1 = self.marketing.findChild(QFrame, "frame_grafico_1")
            self.agregar_grafico_pie(
                datos=dict(zip(["Campaña 1", "Campaña 2", "Campaña 3"], balance_campanas)),
                titulo="Estado de Campañas",
                frame=frame_grafico_1
            )

            frame_grafico_2 = self.marketing.findChild(QFrame, "frame_grafico_2")
            self.agregar_grafico_barras(
                datos=dinero_automatizaciones,
                titulo="Dinero Ganado con Automatizaciones",
                eje_y_rango=(0, max(dinero_automatizaciones) + 500),
                frame=frame_grafico_2
            )

        except Exception as e:
            QMessageBox.critical(self, "Error de procesamiento", f"Hubo un error procesando el archivo CSV:\n{str(e)}")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "icons/favicon.ico")))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
