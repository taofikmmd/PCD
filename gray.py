import sys
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore


class GrayscaleViewer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Pengaturan jendela
        self.setWindowTitle("Tampilan Citra Keabuan (Grayscale)")
        self.setGeometry(300, 200, 800, 500)

        # Label untuk menampilkan gambar
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(50, 50, 400, 300)
        self.label.setStyleSheet("border: 2px solid gray;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Belum ada gambar")

        # Tombol untuk memuat gambar
        self.btn_load = QtWidgets.QPushButton("Load Grayscale Image", self)
        self.btn_load.setGeometry(500, 100, 200, 40)
        self.btn_load.clicked.connect(self.load_grayscale_image)

        # Variabel citra
        self.image = None

    # Fungsi untuk memuat dan menampilkan citra keabuan
    def load_grayscale_image(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Pilih Gambar", "", "Image Files (*.jpg *.png *.bmp)"
        )
        if file:
            # Baca gambar dalam format grayscale
            self.image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

            # Dapatkan ukuran gambar
            h, w = self.image.shape

            # Ubah citra ke format QImage
            qt_image = QtGui.QImage(
                self.image.data, w, h, w, QtGui.QImage.Format_Grayscale8
            )

            # Tampilkan di QLabel
            pixmap = QtGui.QPixmap.fromImage(qt_image)
            self.label.setPixmap(pixmap.scaled(
                self.label.width(), self.label.height(),
                QtCore.Qt.KeepAspectRatio
            ))
            self.label.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = GrayscaleViewer()
    window.show()
    sys.exit(app.exec_())
