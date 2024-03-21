from ultralytics import YOLO
import cv2
import imutils
import numpy as np
#from easyocr import Reader
from matplotlib import pyplot as plt

def main():
    img = cv2.imread("C:\Data\Buckeye Vertical\Image Classifier\BuckeyeVerticalObjectDetection\Script Test Data\OCR5x1.png")  # list of numpy arrays

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray,(3,3),0)

    gray = imutils.resize(gray, width=320)

    ret3,th3 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Apply dilation to thicken the edges
    kernel = np.ones((9, 9), np.uint8)
    th3 = cv2.erode(th3, kernel, iterations=2)
    kernal_dilate = np.ones((6, 6), np.uint8)
    th3 = cv2.dilate(th3, kernal_dilate, iterations=1)

    #th3 = cv2.GaussianBlur(gray,(11,11),0)
    
    
    #th3 = imutils.rotate(th3, 100)

    #reader = Reader(['en'])
    #   detect the text from the license plate
    #detection = reader.readtext(th3, rotation_info=[15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270])
    #detection = reader.readtext(th3)
    #print(detection)

    # Find the contours in the image
    #contours, hierarchy = cv2.findContours(th3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #print(contours)

    # Fill the contours with white color
    #cv2.drawContours(cropped_image, contours, -1, 255, -1)

    # Convert BGR to RGB for plt.imshow
    th3 = cv2.cvtColor(th3, cv2.COLOR_BGR2RGB)
    #plt.imshow(img)
    plt.imshow(th3)
    
    #plt.hist(th3.ravel(),256)


    plt.show()
    cv2.waitKey(0)  # Wait for a key event
    cv2.destroyAllWindows()  # Destroy all windows

if __name__ == '__main__':
    main()