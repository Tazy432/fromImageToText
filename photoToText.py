from PIL import Image
import pytesseract
import os

def image_to_text(input_image_path, output_text_path):
    try:
        # Open the image file
        image = Image.open(input_image_path)

        # Use pytesseract to perform OCR
        text = pytesseract.image_to_string(image)

        # Write the extracted text to a text file
        with open(output_text_path, "w") as text_file:
            text_file.write(text)

        print(f"Text file '{output_text_path}' created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_image_path = "C:\\Users\\Admin\\Desktop\\Personal projects\\aboutToBeTransformed2.jpeg"
output_text_path = "C:\\Users\\Admin\\Desktop\\Personal projects\\transformed.txt"

# Ensure the image file exists before processing
if os.path.exists(input_image_path):
    image_to_text(input_image_path, output_text_path)
else:
    print("The specified image file does not exist.")
