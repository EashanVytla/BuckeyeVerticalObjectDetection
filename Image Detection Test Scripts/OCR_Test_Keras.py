import matplotlib.pyplot as plt
import keras_ocr
import cv2

def detect_characters(image_path):
    # Load the recognizer and detector
    pipeline = keras_ocr.pipeline.Pipeline()

    # Read the image
    image = keras_ocr.tools.read(image_path)

    # Get predictions
    predictions = pipeline.recognize([image])

    # Display the image with bounding boxes around detected characters
    fig, ax = plt.subplots(figsize=(10, 10))

    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions[0], ax=ax)
    plt.show()

if __name__ == "__main__":
    # Specify the path to your image
    image_path = "C:\Data\Buckeye Vertical\Image Classifier\BuckeyeVerticalObjectDetection\Script Test Data\OCR5x1.png"

    # Call the function to detect characters
    detect_characters(image_path)
