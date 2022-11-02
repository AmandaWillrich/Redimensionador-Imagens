import sys
from arquivobruto.newrawfile import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseFile.clicked.connect(self.open_picture)
        self.btnResizePicture.clicked.connect(self.resize_picture)
        self.btnSave.clicked.connect(self.save_picture)

    def open_picture(self):
        picture, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Escolher Arquivo',
            r'/Users/Amand/Pictures'
        )
        self.inputOpenFile.setText(picture)
        self.original_picture = QPixmap(picture)
        self.LabelImg.setPixmap(self.original_picture)
        self.inputWidth.setText(str(self.original_picture.width()))
        self.inputHeight.setText(str(self.original_picture.height()))

    def resize_picture(self):
        width = int(self.inputWidth.text())
        self.new_picture = self.original_picture.scaledToWidth(width)
        self.LabelImg.setPixmap(self.new_picture)
        self.inputWidth.setText(str(self.new_picture.width()))
        self.inputHeight.setText(str(self.new_picture.height()))

    def save_picture(self):
        picture, _ = QFileDialog.getSaveFileName(
        self.centralwidget,
        'Salvar',
        r'/Users/Amand/Desktop'
        )
        self.new_picture.save(picture, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()