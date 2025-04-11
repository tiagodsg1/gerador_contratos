import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gráficos com QtCharts")
        self.resize(800, 400)

        layout = QVBoxLayout()

        # Gráfico de Pizza
        pie_series = QPieSeries()
        pie_series.append("A", 10)
        pie_series.append("B", 30)
        pie_series.append("C", 25)
        pie_series.append("D", 35)

        pie_chart = QChart()
        pie_chart.addSeries(pie_series)
        pie_chart.setTitle("Gráfico de Pizza")
        pie_chart.legend().setAlignment(Qt.AlignRight)

        pie_view = QChartView(pie_chart)
        pie_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(pie_view)

        # Gráfico de Barras
        bar_set = QBarSet("Valores")
        bar_set << 10 << 30 << 25 << 35

        bar_series = QBarSeries()
        bar_series.append(bar_set)

        bar_chart = QChart()
        bar_chart.addSeries(bar_series)
        bar_chart.setTitle("Gráfico de Barras")
        bar_chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = ["A", "B", "C", "D"]
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        bar_chart.createDefaultAxes()
        bar_chart.setAxisX(axisX, bar_series)

        bar_chart.legend().setVisible(False)

        bar_view = QChartView(bar_chart)
        bar_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(bar_view)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ChartWindow()
    win.show()
    sys.exit(app.exec_())
