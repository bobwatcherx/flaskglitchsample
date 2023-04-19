import cv2
import pytesseract
import numpy as np

# Load gambar KTP
img = cv2.imread('ktp.jpg')

# Konversi gambar ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Penerapan filter Gaussian
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# OCR pada gambar yang sudah diproses
text = pytesseract.image_to_string(gray, lang='ind')

# Simpan hasil OCR ke dalam file result.txt
with open('result.txt', mode='w') as file:
    file.write(text)
