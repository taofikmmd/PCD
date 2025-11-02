import sys
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore


class SmartHealth(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Judul dan ukuran jendela utama
        self.setWindowTitle("Smart Health - Pengolahan Citra Digital")
        self.setGeometry(300, 200, 800, 500)

        # Label tempat gambar akan ditampilkan
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(50, 50, 400, 300)
        self.label.setStyleSheet("border: 2px solid gray;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Area Gambar")

        # Tombol Load Image
        self.btn_load = QtWidgets.QPushButton("Load Image", self)
        self.btn_load.setGeometry(500, 100, 200, 40)
        self.btn_load.clicked.connect(self.load_image)  # <-- Hubungkan tombol ke fungsi

        # Label tambahan untuk judul
        self.title = QtWidgets.QLabel("Modul Smart Health", self)
        self.title.setGeometry(300, 10, 300, 30)
        self.title.setStyleSheet("font-size: 16pt; font-weight: bold;")

        self.image = None  # variabel untuk menyimpan gambar

    def load_image(self):
        # Membuka file dialog untuk memilih gambar
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Pilih Gambar", "", "Image Files (*.jpg *.png *.bmp)"
        )
        if file:
            # Baca gambar dengan OpenCV (format BGR)
            self.image = cv2.imread(file)
            # Ubah ke format RGB untuk PyQt
            img_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

            # Konversi ke QImage
            h, w, ch = img_rgb.shape
            bytes_per_line = ch * w
            qt_image = QtGui.QImage(img_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

            # Tampilkan di QLabel
            pixmap = QtGui.QPixmap.fromImage(qt_image)
            self.label.setPixmap(pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio))
            self.label.setText("")  # hapus tulisan awal


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SmartHealth()
    window.show()
    sys.exit(app.exec_())
