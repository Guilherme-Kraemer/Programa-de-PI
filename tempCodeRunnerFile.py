image = cv2.imread(image_location)
print(pytesseract.image_to_string(image))