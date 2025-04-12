import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                            QPushButton, QMessageBox, QDialog, QScrollArea, QVBoxLayout)
from PyQt6.QtCore import Qt

class ConsultaWindow(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Consulta de Categorias - oxxo")
            self.setGeometry(150, 150, 500, 400)
            qr = self.frameGeometry()
            cp = QApplication.primaryScreen().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

            
            layout = QVBoxLayout()
            
            lbl_titulo = QLabel("LISTADO DE CATEGORIAS:")
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
ventana.setWindowTitle("CRUD Categorías - oxxo")
ventana.setGeometry(100, 100, 400, 250)
qr = ventana.frameGeometry()
cp = app.primaryScreen().availableGeometry().center()
qr.moveCenter(cp)
ventana.move(qr.topLeft())


lbl_id = QLabel("ID Categoría:", ventana)
lbl_id.move(30, 30)
txt_id = QLineEdit(ventana)
txt_id.move(150, 30)
txt_id.resize(200, 25)

lbl_nombre = QLabel("Nombre:", ventana)
lbl_nombre.move(30, 70)
txt_nombre = QLineEdit(ventana)
txt_nombre.move(150, 70)
txt_nombre.resize(200, 25)

btn_agregar = QPushButton("Agregar", ventana)
btn_agregar.move(30, 130)
btn_actualizar = QPushButton("Actualizar", ventana)
btn_actualizar.move(150, 130)
btn_eliminar = QPushButton("Eliminar", ventana)
btn_eliminar.move(270, 130)
btn_consultar = QPushButton("Consultar", ventana)
btn_consultar.move(30, 180)
btn_consultar.resize(340, 25)

btn_consultar.clicked.connect(lambda: ConsultaWindow().exec())

ventana.show()
sys.exit(app.exec())