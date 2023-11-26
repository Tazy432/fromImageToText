from PIL import Image
import os

def image_to_text(input_image_path, output_text_path):
    try:
        # Open the image file
        image = Image.open(input_image_path)

        # Get image dimensions
        width, height = image.size

        # Convert image to grayscale
        grayscale_image = image.convert("L")

        # Create a list to store characters representing pixel intensity
        char_list = []

        # Define a set of characters to represent intensity
        intensity_chars = "@%#*+=-:. "

        # Normalize pixel intensity to the range [0, 255]
        pixel_values = list(grayscale_image.getdata())
        normalized_values = [int((pixel_value / 255.0) * (len(intensity_chars) - 1)) for pixel_value in pixel_values]

        # Loop through each pixel intensity and map to a character
        for i, intensity in enumerate(normalized_values):
            char_list.append(intensity_chars[intensity])
            
            # Add a newline at the end of each row
            if (i + 1) % width == 0:
                char_list.append("\n")

        # Write the characters to a text file
        with open(output_text_path, "w") as text_file:
            text_file.writelines(char_list)

        print(f"Text file '{output_text_path}' created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_image_path = "C:\\Users\\Admin\\Desktop\\Personal projects\\aboutToBeTransformed.jpeg"
output_text_path = "C:\\Users\\Admin\\Desktop\\Personal projects\\transformed.txt"

# Ensure the image file exists before processing
if os.path.exists(input_image_path):
    image_to_text(input_image_path, output_text_path)
else:
    print("The specified image file does not exist.")
