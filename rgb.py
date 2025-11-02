import sys
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore
import numpy as np


class RGBChannelsViewer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tampilan 3 Channel RGB")
        self.setGeometry(200, 100, 1200, 500)

        # 3 Label untuk menampilkan masing-masing channel
        self.label_r = QtWidgets.QLabel("Red Channel", self)
        self.label_r.setGeometry(50, 50, 300, 300)
        self.label_r.setStyleSheet("border: 2px solid gray;")
        self.label_r.setAlignment(QtCore.Qt.AlignCenter)

        self.label_g = QtWidgets.QLabel("Green Channel", self)
        self.label_g.setGeometry(450, 50, 300, 300)
        self.label_g.setStyleSheet("border: 2px solid gray;")
        self.label_g.setAlignment(QtCore.Qt.AlignCenter)

        self.label_b = QtWidgets.QLabel("Blue Channel", self)
        self.label_b.setGeometry(850, 50, 300, 300)
        self.label_b.setStyleSheet("border: 2px solid gray;")
        self.label_b.setAlignment(QtCore.Qt.AlignCenter)

        # Tombol load image
        self.btn_load = QtWidgets.QPushButton("Load Image", self)
        self.btn_load.setGeometry(500, 370, 200, 40)
        self.btn_load.clicked.connect(self.load_image)

        self.image = None

    def load_image(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Pilih Gambar", "", "Image Files (*.jpg *.png *.bmp)"
        )
        if file:
            # Baca gambar RGB
            self.image = cv2.imread(file)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

            # Pisahkan channel
            r, g, b = cv2.split(self.image)

            # Membuat gambar 3 channel dari masing-masing channel
            red_img = cv2.merge([r, np.zeros_like(g), np.zeros_like(b)])
            green_img = cv2.merge([np.zeros_like(r), g, np.zeros_like(b)])
            blue_img = cv2.merge([np.zeros_like(r), np.zeros_like(g), b])

            # Tampilkan masing-masing channel
            self.display_image(red_img, self.label_r)
            self.display_image(green_img, self.label_g)
            self.display_image(blue_img, self.label_b)

    def display_image(self, img, label):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qt_image = QtGui.QImage(img.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qt_image)
        label.setPixmap(pixmap.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RGBChannelsViewer()
    window.show()
    sys.exit(app.exec_())
