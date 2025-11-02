import sys
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore


class SmartHealth(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Judul dan ukuran jendela utama
        self.setWindowTitle("UTS - Pengolahan Citra Digital")
        self.setGeometry(300, 200, 800, 500)

        # Label tempat gambar akan ditampilkan
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(50, 50, 400, 300)
        self.label.setStyleSheet("border: 2px solid gray;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Area Gambar")

        # Label tambahan untuk judul
        self.title = QtWidgets.QLabel("Modul UTS", self)
        self.title.setGeometry(300, 10, 300, 30)
        self.title.setStyleSheet("font-size: 16pt; font-weight: bold;")

        self.image = None  # variabel untuk menyimpan gambar

        # Load gambar langsung saat aplikasi dijalankan
        self.load_default_image("tkjc.jpg")  # <-- ganti dengan path gambar kamu

    def load_default_image(self, path):
        self.image = cv2.imread(path)
        if self.image is not None:
            # Ubah ke format RGB
            img_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

            # Konversi ke QImage
            h, w, ch = img_rgb.shape
            bytes_per_line = ch * w
            qt_image = QtGui.QImage(img_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

            # Tampilkan di QLabel
            pixmap = QtGui.QPixmap.fromImage(qt_image)
            self.label.setPixmap(pixmap.scaled(self.label.width(), self.label.height(),
                                               QtCore.Qt.KeepAspectRatio))
            self.label.setText("")
        else:
            self.label.setText("Gambar tidak ditemukan!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SmartHealth()
    window.show()
    sys.exit(app.exec_())
