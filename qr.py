import pyqrcode
from PIL import Image
import cv2

link = input("Inserta en enlace para convertir a QR: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCode.png").show()