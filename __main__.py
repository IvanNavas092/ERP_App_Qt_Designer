import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QDialog, QMessageBox
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QCategoryAxis, QValueAxis, QBarSet, QBarSeries, QBarCategoryAxis, QPieSeries
from PySide6.QtGui import QPainter
from interfaz import Ui_MainWindow  
from window_suministro import Ui_Window
from window_informe import Ui_Dialog
from window_filtrar import Ui_Dialog_F
from window_recordatorio import Ui_main
from window_proyecto import Ui_Dialog_P
from window_auto import Ui_Dialog_A
from PySide6.QtGui import QIcon
import os


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

        # Agregar gráfico en Inventory
        self.agregar_grafico_generico(
            datos=[10000, 12000, 9000, 15000, 11000, 13000, 14000, 16000, 18000, 17000, 16000, 22000],
            titulo="Balance de Dinero - 2024",
            eje_y_rango=(10000, 22000),
            frame=self.graphic
        )

        # Agregar gráfico lineal en Buys
        frame_lineal = self.Buys.findChild(QFrame, "frame_lineal")
        self.agregar_grafico_generico(
            datos=[2000, 4000, 2000, 1500, 2100, 2300, 2400, 1600, 3800, 4700, 5600, 5080],
            titulo="Gastos de Dinero - 2024",
            eje_y_rango=(0, 6000),
            frame=frame_lineal
        )

        # Agregar gráfico de barras en Finance
        frame_balance = self.finance.findChild(QFrame, "frame_balance")
        self.agregar_grafico_barras(
            datos=[5000, 7000, 6000, 4000, 8000, 5500, 6500, 7000, 7500, 6000, 7200, 6800],
            titulo="Balance Financiero - 2024",
            eje_y_rango=(0, 10000),
            frame=frame_balance
        )

        # Agregar gráficos en Marketing Electrónico
        frame_grafico_1 = self.marketing.findChild(QFrame, "frame_grafico_1")
        self.agregar_grafico_pie(
            datos={"Campañas Activas": 45, "Campañas Pausadas": 20, "Campañas Finalizadas": 35},
            titulo="Estado de Campañas",
            frame=frame_grafico_1
        )

        frame_grafico_2 = self.marketing.findChild(QFrame, "frame_grafico_2")
        self.agregar_grafico_barras(
            datos=[500, 700, 900, 600, 800, 1100],
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "icons/favicon.ico")))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

    
