from capstone import *
import cv2
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:/Users/USER/AppData/Local/Tesseract-OCR/tesseract.exe'
img = cv2.imread("C:/Users/khaju/Desktop/capstone/test/image1.jpg")
threshold_img = preprocess(img)
contours= extract_contours(threshold_img)
text = cleanAndRead(img,contours)
print('text:',text)
