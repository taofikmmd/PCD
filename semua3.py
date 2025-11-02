import sys
import cv2
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore

class SmartHealth(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Health - RGB Combined")
        self.setGeometry(200, 100, 1000, 400)

        # Label untuk menampilkan gambar
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(50, 50, 900, 300)
        self.label.setStyleSheet("border: 2px solid gray;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # Tombol
        self.btn_load = QtWidgets.QPushButton("Load Image", self)
        self.btn_load.setGeometry(50, 10, 150, 30)
        self.btn_load.clicked.connect(self.load_image)

        self.btn_rgb = QtWidgets.QPushButton("Show RGB Channels", self)
        self.btn_rgb.setGeometry(220, 10, 150, 30)
        self.btn_rgb.clicked.connect(self.show_rgb_combined)

        # Variabel citra
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

    def show_rgb_combined(self):
        if self.image is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Load image first!")
            return

        # Pisahkan channel BGR
        b, g, r = cv2.split(self.image)

        # Buat visualisasi masing-masing channel
        red_img = cv2.merge([np.zeros_like(b), np.zeros_like(g), r])
        green_img = cv2.merge([np.zeros_like(b), g, np.zeros_like(r)])
        blue_img = cv2.merge([b, np.zeros_like(g), np.zeros_like(r)])

        # Gabungkan ketiga channel secara horizontal
        combined = np.hstack((red_img, green_img, blue_img))

        # Tampilkan di QLabel
        self.display_image(combined)

    def display_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img_rgb.shape
        bytes_per_line = ch * w
        qt_img = QtGui.QImage(img_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(qt_img)
        self.label.setPixmap(pix.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SmartHealth()
    window.show()
    sys.exit(app.exec_())
