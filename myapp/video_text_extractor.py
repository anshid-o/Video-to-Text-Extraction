import cv2
import os
from PIL import Image
import pytesseract

def split_video_to_images(video_file, output_folder, interval=100):
    """
    Split a video into images at a specified interval and save them to the output folder.
    :param video_file: Path to the video file
    :param output_folder: Path to the output folder to save images
    :param interval: Interval between frames to capture (default is 100 frames)
    """
    # Read the video
    video_capture = cv2.VideoCapture(video_file)
    print("split function")
    # Create the output folder if it doesn't exist
    

    # Initialize frame counter
    current_frame = 0

    while True:
        # Read frame
        ret, frame = video_capture.read()
        print("frames fetched")
        if not ret:
            break
        print("ok")
        # Save frame at specified interval
        if current_frame % interval == 0:
            # Save frame as image
            image_path = os.path.join(output_folder, f"frame{current_frame}.jpg")
            cv2.imwrite(image_path, frame)
            print("images saved")

        current_frame += 1

    # Release resources
    video_capture.release()
    cv2.destroyAllWindows()

def extract_text_from_images(image_folder):
    """
    Extract text from images in a folder using pytesseract.
    :param image_folder: Path to the folder containing images
    :return: Extracted text
    """
    # Initialize final text
    final_text = ""
    print("text extract function")
    # Configure pytesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    # Iterate over image files in the folder
    for filename in os.listdir(image_folder):
        print("extrating.....")
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Open image
            image_path = os.path.join(image_folder, filename)
            img = Image.open(image_path) 

            # Extract text from the image 
            text = pytesseract.image_to_string(img) 
            print("............................................."+text)

            # Add the extracted text to final_text
            final_text += '\n' + text

    return final_text

# Example usage:
# video_file = 'path_to_your_video.mp4'
# output_folder = 'data'
# split_video_to_images(video_file, output_folder)
# extracted_text = extract_text_from_images(output_folder)
# print(extracted_text)
