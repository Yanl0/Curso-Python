from PIL import Image
import pywhatkit

Image.open("logo.png")
pywhatkit.image_to_ascii_art("logo.png", "Arte")
read_file = open("Arte.txt", "r")
print(read_file.read())