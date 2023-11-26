import base64
from io import BytesIO
from PIL import Image, ImageGrab
import pytesseract
import time
import pyperclip

last_processed_content = ""  # Initialize the last processed content

def image_to_text(input_image, output_text):
    try:
        # Use pytesseract to perform OCR
        text = pytesseract.image_to_string(input_image)

        # Write the extracted text to a text file
        with open(output_text, "w") as text_file:
            text_file.write(text)

        print(f"Text file '{output_text}' created successfully.")
    except Exception as e:
        print(f"An error occurred during OCR: {e}")

def process_screenshot():
    global last_processed_content  # Use the global variable

    try:
        # Capture the screen
        screenshot = ImageGrab.grabclipboard()

        # Check if the clipboard contains an image
        if screenshot:
            # Convert image to base64-encoded string for content comparison
            current_content = ImageToBase64(screenshot)

            # Process the screenshot only if the content is different from the last processed content
            if current_content != last_processed_content:
                # Update the last processed content
                last_processed_content = current_content

                # Save the image
                timestamp = time.strftime("%Y%m%d%H%M%S")
                screenshot_path = f"C:\\Users\\Admin\\Desktop\\Personal projects\\screenshot_{timestamp}.png"
                screenshot.save(screenshot_path)

                # Process the screenshot
                output_text_path = f"C:\\Users\\Admin\\Desktop\\Personal projects\\transformed_{timestamp}.txt"
                image_to_text(screenshot, output_text_path)
                print("Image processed successfully")
    except Exception as e:
        print(f"An error occurred during processing: {e}")

def ImageToBase64(image):
    # Convert image to base64-encoded string
    image_buffer = BytesIO()
    image.save(image_buffer, format="PNG")
    return base64.b64encode(image_buffer.getvalue()).decode("utf-8")

def main():
    try:
        while True:
            # Check for changes in the clipboard every second
            time.sleep(1)
            process_screenshot()
    except KeyboardInterrupt:
        print("Script interrupted. Exiting gracefully.")

if __name__ == "__main__":
    main()
