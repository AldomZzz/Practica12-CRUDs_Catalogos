import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QDialog, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt

class ConsultaWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consulta de Empleados - oxxo")
        self.setGeometry(150, 150, 500, 400)
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        
        layout = QVBoxLayout()
        
        lbl_titulo = QLabel("LISTADO DE EMPLEADOS:")
        lbl_titulo.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(lbl_titulo)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        
        self.lbl_resultados = QLabel()
        self.lbl_resultados.setWordWrap(True)
        self.lbl_resultados.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.lbl_resultados.setStyleSheet("font-family: monospace;")
        
        scroll.setWidget(self.lbl_resultados)
        layout.addWidget(scroll)
        
        self.setLayout(layout)

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("CRUD Empleados - oxxo")
ventana.setGeometry(500, 500, 400, 350)
qr = ventana.frameGeometry()
cp = app.primaryScreen().availableGeometry().center()
qr.moveCenter(cp)
ventana.move(qr.topLeft())


lbl_id = QLabel("Telefono:", ventana)
lbl_id.move(30, 30)
txt_id = QLineEdit(ventana)
txt_id.move(150, 30)
txt_id.resize(200, 25)

lbl_nombre = QLabel("Nombre:", ventana)
lbl_nombre.move(30, 70)
txt_nombre = QLineEdit(ventana)
txt_nombre.move(150, 70)
txt_nombre.resize(200, 25)

lbl_puesto = QLabel("Puesto:", ventana)
lbl_puesto.move(30, 110)
combo_puesto = QComboBox(ventana)
combo_puesto.move(150, 110)
combo_puesto.resize(200, 25)
combo_puesto.addItems(['gerente', 'cajero', 'almacen'])

lbl_fecha = QLabel("Fecha Contratación:", ventana)
lbl_fecha.move(30, 150)
txt_fecha = QLineEdit(ventana)
txt_fecha.move(150, 150)
txt_fecha.resize(200, 25)
txt_fecha.setPlaceholderText("YYYY-MM-DD")

lbl_sueldo = QLabel("Sueldo:", ventana)
lbl_sueldo.move(30, 190)
txt_sueldo = QLineEdit(ventana)
txt_sueldo.move(150, 190)
txt_sueldo.resize(200, 25)

btn_agregar = QPushButton("Agregar", ventana)
btn_agregar.move(30, 250)
btn_actualizar = QPushButton("Actualizar", ventana)
btn_actualizar.move(150, 250)
btn_eliminar = QPushButton("Eliminar", ventana)
btn_eliminar.move(270, 250)
btn_consultar = QPushButton("Consultar", ventana)
btn_consultar.move(30, 290)
btn_consultar.resize(340, 25)

btn_consultar.clicked.connect(lambda: ConsultaWindow().exec())

ventana.show()
sys.exit(app.exec())
