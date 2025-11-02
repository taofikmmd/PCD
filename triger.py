import sys
import cv2
from PyQt5 import QtWidgets, QtGui, QtCore


class SmartHealth(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Judul dan ukuran jendela utama
        self.setWindowTitle("Smart Health - Menampilkan Gambar")
        self.setGeometry(300, 200, 800, 500)

        # Label tempat gambar akan muncul
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(50, 50, 400, 300)
        self.label.setStyleSheet("border: 2px solid gray;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Belum ada gambar")

        # Tombol untuk memuat gambar
        self.btn_load = QtWidgets.QPushButton("Load Image", self)
        self.btn_load.setGeometry(500, 100, 200, 40)
        self.btn_load.clicked.connect(self.load_image)  # <--- Trigger tombol

        # Variabel untuk menyimpan citra
        self.image = None

    # Fungsi untuk memuat gambar
    def load_image(self):
        # Pilih file gambar
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Pilih Gambar", "", "Image Files (*.jpg *.png *.bmp)"
        )
        if file:
            # Baca gambar dengan OpenCV
            self.image = cv2.imread(file)

            # Konversi dari BGR ke RGB
            image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

            # Ubah ke QImage agar bisa ditampilkan di PyQt
            h, w, ch = image_rgb.shape
            bytes_per_line = ch * w
            qt_image = QtGui.QImage(
                image_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888
            )

            # Tampilkan gambar di QLabel
            pixmap = QtGui.QPixmap.fromImage(qt_image)
            self.label.setPixmap(pixmap.scaled(
                self.label.width(), self.label.height(),
                QtCore.Qt.KeepAspectRatio
            ))
            self.label.setText("")  # hapus tulisan awal


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SmartHealth()
    window.show()
    sys.exit(app.exec_())
