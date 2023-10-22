import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QWidget, QApplication, QScrollArea, \
    QGridLayout, QButtonGroup, QPushButton

import  math


class Ventana1(QMainWindow):

    def __init__(self,parent=None):
        super(Ventana1,self).__init__(parent=parent)

        self.setWindowTitle("Ventana Clase6")

        self.setStyleSheet("background-color: grey;")

        self.ancho = 1100
        self.alto = 700

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())


        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.interna = QWidget()
        self.interna.setContentsMargins(20, 20, 20, 20)
        self.setCentralWidget(self.interna)

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Menú de elementos")

        self.letrero1.setFont(QFont("Arial", 20))

        self.letrero1.setAlignment(Qt.AlignCenter)


        self.letrero1.setStyleSheet("background-color: #FFFFFF; color: #000000; padding: 30px;"
                                    "border:solid; border-width:3px; border-color:#000000;"
                                    "border-radius:5px; margin_bottom:50px;")

        self.vertical.addWidget(self.letrero1)

        self.scrollArea = QScrollArea()

        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        self.vertical.addWidget(self.scrollArea)

        self.numeroElementos = 20

        self.contador = 0

        self.elementosPorColumna = 5


        #print( math.ceil(13/4) )

        self.numeroFilas = math.ceil(self.numeroElementos / self.elementosPorColumna) + 1


        self.interna.setLayout(self.vertical)

        self.botones = QButtonGroup()

        #self.botones.setExclusive(True)



        for fila in range (1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):
                if self.contador < self.numeroElementos:

                    self.ventanaAux = QWidget()

                    self.ventanaAux.setFixedHeight(200)
                    self.ventanaAux.setFixedWidth(200)

                    self.verticalCuadricula = QVBoxLayout()

                    self.labelImagen = QLabel()

                    self.labelImagen.setFixedWidth(128)
                    self.labelImagen.setFixedHeight(128)

                    self.Imagen = QPixmap("imagenes/burguer.png")

                    self.labelImagen.setPixmap(self.Imagen)

                    self.labelImagen.setScaledContents(True)

                    self.verticalCuadricula.addWidget(self.labelImagen)

                    self.verticalCuadricula.addStretch()

                    self.labelNombre = QLabel('Item n. ' + str(self.contador +1))

                    self.verticalCuadricula.addWidget(self.labelNombre)

                    self.verticalCuadricula.addStretch()

                    self.botonAccion = QPushButton('Visitar elemento ' + str(self.contador + 1))

                    self.botonAccion.setFixedWidth(100)

                    self.verticalCuadricula.addWidget(self.botonAccion)

                    self.botones.addButton(self.botonAccion, self.contador + 1)

                    self.verticalCuadricula.addStretch()


                    self.ventanaAux.setLayout(self.verticalCuadricula)

                    self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                    self.contador += 1

            self.botones.idClicked.connect(self.metodo_accion_boton)

    def metodo_accion_boton(self, idBoton):
        print(idBoton)







                    













if __name__ == '__main__':

    app = QApplication(sys.argv)


    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())