import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                            QPushButton, QMessageBox, QDialog, 
                            QVBoxLayout, QScrollArea)
from PyQt6.QtCore import Qt

class ConsultaProveedoresWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consulta de Proveedores - oxxo")
        self.setGeometry(150, 150, 500, 400)
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
        layout = QVBoxLayout()
        
        lbl_titulo = QLabel("LISTADO DE PROVEEDORES:")
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
        
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.clicked.connect(self.close)
        layout.addWidget(btn_cerrar)
        
        self.setLayout(layout)

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("CRUD Proveedores - oxxo")
ventana.setGeometry(500, 500, 400, 350)
qr = ventana.frameGeometry()
cp = app.primaryScreen().availableGeometry().center()
qr.moveCenter(cp)
ventana.move(qr.topLeft())


lbl_nombre = QLabel("Nombre:", ventana)
lbl_nombre.move(30, 30)
txt_nombre = QLineEdit(ventana)
txt_nombre.move(150, 30)
txt_nombre.resize(200, 25)

lbl_contacto = QLabel("Contacto:", ventana)
lbl_contacto.move(30, 70)
txt_contacto = QLineEdit(ventana)
txt_contacto.move(150, 70)
txt_contacto.resize(200, 25)

lbl_telefono = QLabel("Teléfono:", ventana)
lbl_telefono.move(30, 110)
txt_telefono = QLineEdit(ventana)
txt_telefono.move(150, 110)
txt_telefono.resize(200, 25)

lbl_email = QLabel("Email:", ventana)
lbl_email.move(30, 150)
txt_email = QLineEdit(ventana)
txt_email.move(150, 150)
txt_email.resize(200, 25)

btn_agregar = QPushButton("Agregar", ventana)
btn_agregar.move(30, 200)
btn_actualizar = QPushButton("Actualizar", ventana)
btn_actualizar.move(150, 200)
btn_eliminar = QPushButton("Eliminar", ventana)
btn_eliminar.move(270, 200)
btn_consultar = QPushButton("Consultar Proveedores", ventana)
btn_consultar.move(30, 240)
btn_consultar.resize(340, 25)

btn_consultar.clicked.connect(lambda: ConsultaProveedoresWindow().exec())

ventana.show()
sys.exit(app.exec())