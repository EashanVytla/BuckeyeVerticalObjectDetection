from ultralytics import YOLO
import cv2
import imutils
import numpy as np
from easyocr import Reader
from matplotlib import pyplot as plt
import math
import statistics

def main():
    img = cv2.imread("C:\Data\Buckeye Vertical\Image Classifier\BuckeyeVerticalObjectDetection\Script Test Data\OCR5x2.png")  # list of numpy arrays

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = imutils.resize(gray, width=320)

    gray = cv2.GaussianBlur(gray,(3,3),0)

    ret3,th3 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Apply dilation to thicken the edges
    kernel = np.ones((11, 11), np.uint8)
    th3 = cv2.erode(th3, kernel, iterations=1)
    kernal_dilate = np.ones((6, 6), np.uint8)
    th3 = cv2.dilate(th3, kernal_dilate, iterations=1)

    edges = cv2.Canny(th3, 100, 200)
    #cv2.imshow("edges",edges)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,40,minLineLength=30,maxLineGap=30)
    #lines = cv2.HoughLinesP(edges,1,np.pi/180,40)

    th3 = cv2.cvtColor(th3, cv2.COLOR_BGR2RGB)

    angles = []

    closestToCenter = 0

    # Get the height and width of the image
    (h, w) = th3.shape[:2]

    # Define the center of the image
    center = (w / 2, h / 2)

    for i in range(len(lines)):
        for x1,y1,x2,y2 in lines[i]:
            #cv2.line(th3,(x1,y1),(x2,y2),(255,0,0),5)
            angles.append(math.atan2(y1 - y2, x2 - x1))
            if(abs(x1 - center[0]) < abs(lines[closestToCenter][0][0] - center[0])):
                closestToCenter = i

    angle = angles[closestToCenter]

    print(math.degrees(angle))

    # Rotate the image by 10 degrees
    rotated = cv2.warpAffine(th3, cv2.getRotationMatrix2D(center, 90-math.degrees(angle), 1.0), (w, h))

    reader = Reader(['en'])
    #   detect the text from the license plate
    #detection = reader.readtext(th3, rotation_info=[15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270])
    detection = reader.readtext(rotated)
    print(detection)

    # Convert BGR to RGB for plt.imshow
    plt.imshow(rotated)

    plt.show()
    cv2.waitKey(0)  # Wait for a key event
    cv2.destroyAllWindows()  # Destroy all windows

if __name__ == '__main__':
    main()