import sys
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore

class SmartHealth(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Uts PCD - RGB di Bawah")
        self.setGeometry(150, 100, 900, 600)

        # --- Label utama ---
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(50, 50, 800, 300)
        self.label.setStyleSheet("border: 2px solid gray;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # --- Tombol ---
        self.btn_load = QtWidgets.QPushButton("Load Image", self)
        self.btn_load.setGeometry(50, 10, 150, 30)
        self.btn_load.clicked.connect(self.load_image)

        self.btn_gray = QtWidgets.QPushButton("Convert to Grayscale", self)
        self.btn_gray.setGeometry(220, 10, 150, 30)
        self.btn_gray.clicked.connect(self.convert_gray)

        self.btn_rgb = QtWidgets.QPushButton("Show RGB Channels", self)
        self.btn_rgb.setGeometry(390, 10, 150, 30)
        self.btn_rgb.clicked.connect(self.show_rgb_channels)

        # --- Labels untuk R, G, B di bawah gambar utama ---
        self.label_r = QtWidgets.QLabel("Red", self)
        self.label_r.setGeometry(50, 370, 250, 150)
        self.label_r.setStyleSheet("border: 2px solid red;")
        self.label_r.setAlignment(QtCore.Qt.AlignCenter)

        self.label_g = QtWidgets.QLabel("Green", self)
        self.label_g.setGeometry(325, 370, 250, 150)
        self.label_g.setStyleSheet("border: 2px solid green;")
        self.label_g.setAlignment(QtCore.Qt.AlignCenter)

        self.label_b = QtWidgets.QLabel("Blue", self)
        self.label_b.setGeometry(600, 370, 250, 150)
        self.label_b.setStyleSheet("border: 2px solid blue;")
        self.label_b.setAlignment(QtCore.Qt.AlignCenter)

        self.image = None

    def load_image(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)"
        )
        if file:
            self.image = cv2.imread(file)
            if self.image is not None:
                self.display_image(self.image)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Gagal membaca gambar!")

    def convert_gray(self):
        if self.image is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Load image first!")
            return
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.display_image(gray, is_gray=True)

    def show_rgb_channels(self):
        if self.image is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Load image first!")
            return

        # Pisahkan channel
        b, g, r = cv2.split(self.image)

        # Buat citra masing-masing channel
        red_img = cv2.merge([np.zeros_like(b), np.zeros_like(g), r])
        green_img = cv2.merge([np.zeros_like(b), g, np.zeros_like(r)])
        blue_img = cv2.merge([b, np.zeros_like(g), np.zeros_like(r)])

        # Tampilkan masing-masing channel di label bawah
        self.display_image(red_img, label=self.label_r)
        self.display_image(green_img, label=self.label_g)
        self.display_image(blue_img, label=self.label_b)

    def display_image(self, img, is_gray=False, label=None):
        target_label = label if label else self.label
        if is_gray:
            h, w = img.shape
            qformat = QtGui.QImage.Format_Indexed8
            qt_img = QtGui.QImage(img.data, w, h, w, qformat)
        else:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img_rgb.shape
            bytes_per_line = ch * w
            qt_img = QtGui.QImage(img_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

        pix = QtGui.QPixmap.fromImage(qt_img)
        target_label.setPixmap(pix.scaled(target_label.width(), target_label.height(), QtCore.Qt.KeepAspectRatio))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SmartHealth()
    window.show()
    sys.exit(app.exec_())
