import pytesseract
from pdf2image import convert_from_path

# Define the file path
file_path = '/Users/alexanderadams/hiddenfees'

# Convert the PDF to a list of images
images = convert_from_path(file_path)

# Loop through the images and extract text
for image in images:
    extracted_text = pytesseract.image_to_string(image)
    print(extracted_text)