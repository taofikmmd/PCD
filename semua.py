import sys
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore


class SmartHealth(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Health - Image Processing")
        self.setGeometry(300, 150, 800, 500)

        # --- Komponen GUI ---
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(50, 50, 400, 300)
        self.label.setStyleSheet("border: 2px solid gray;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.btn_load = QtWidgets.QPushButton("Load Image", self)
        self.btn_load.setGeometry(500, 80, 200, 40)
        self.btn_load.clicked.connect(self.load_image)

        self.btn_gray = QtWidgets.QPushButton("Convert to Grayscale", self)
        self.btn_gray.setGeometry(500, 140, 200, 40)
        self.btn_gray.clicked.connect(self.convert_gray)

        self.btn_matrix = QtWidgets.QPushButton("Show RGB Matrix", self)
        self.btn_matrix.setGeometry(500, 200, 200, 40)
        self.btn_matrix.clicked.connect(self.show_matrix)

        # --- Variabel citra ---
        self.image = None
        self.file_path = None

    # (2) Tampilkan gambar saat tombol ditekan
    def load_image(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)"
        )
        if file:
            self.file_path = file
            self.image = cv2.imread(file)
            self.display_image(self.image)

    # (3) Ubah ke citra keabuan (grayscale)
    def convert_gray(self):
        if self.image is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Load image first!")
            return
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.display_image(gray, is_gray=True)

    # (4) Tampilkan matriks piksel RGB di console
    def show_matrix(self):
        if self.image is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Load image first!")
            return
        print("=== Matriks Piksel RGB ===")
        print(self.image)  # Menampilkan matriks piksel RGB di terminal
        print("==========================")

    # Fungsi menampilkan citra di QLabel
    def display_image(self, img, is_gray=False):
        if is_gray:
            qformat = QtGui.QImage.Format_Indexed8
            h, w = img.shape
            img = QtGui.QImage(img.data, w, h, w, qformat)
        else:
            qformat = QtGui.QImage.Format_RGB888
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            bytes_per_line = ch * w
            img = QtGui.QImage(img.data, w, h, bytes_per_line, qformat)

        pix = QtGui.QPixmap.fromImage(img)
        self.label.setPixmap(pix.scaled(self.label.width(), self.label.height(),
                                        QtCore.Qt.KeepAspectRatio))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SmartHealth()
    window.show()
    sys.exit(app.exec_())
