from ultralytics import YOLO
import cv2
import imutils
import numpy as np
from easyocr import Reader
from matplotlib import pyplot as plt

def main():
    model = YOLO('runs\\detect\\BVTargetModel16\\weights\\best.pt')  # load a pretrained model (recommended for training)
    #results = model.predict(source=, save=True, imgsz=640, conf=0.5)
    img = cv2.imread("C:\\Data\\Buckeye Vertical\\Prelim Detection Dataset\\test\images\\5_38.png")  # list of numpy arrays
    #img = imutils.resize(img, width=1080)
    res = model(img)
    box = res[0].boxes[0]
    res_plotted = res[0].plot()
    
    pos = (int(box.xyxy[0][0].item()), int(box.xyxy[0][1].item()))
    annotated = cv2.putText(res_plotted, str(pos), pos, cv2.FONT_HERSHEY_SIMPLEX, 1, 
                    (0, 0, 255), 2, cv2.LINE_AA, False)
    
    x = int(box.xyxy[0][0].item()) + 30
    y = int(box.xyxy[0][1].item()) + 30
    width = int(box.xywh[0][2].item() - 50)
    height = int(box.xywh[0][3].item() - 50)
    cropped_image = res_plotted[y:y+height, x:x+width]

    # Convert the image to grayscale
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    #gray = cv2.GaussianBlur(gray,(3,3),0)

    gray = imutils.resize(gray, width=320)

    # Apply dilation to thicken the edges
    #kernel = np.ones((21, 21), np.uint8)
    #gray = cv2.dilate(gray, kernel, iterations=1)

    ret3,th3 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    th3 = cv2.GaussianBlur(th3,(11,11),0)
    
    
    #th3 = imutils.rotate(th3, 100)

    reader = Reader(['en'])
    #   detect the text from the license plate
    detection = reader.readtext(th3, rotation_info=[15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270])
    print(detection)

    # Find the contours in the image
    #contours, hierarchy = cv2.findContours(th3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #print(contours)

    # Fill the contours with white color
    #cv2.drawContours(cropped_image, contours, -1, 255, -1)

    # Convert BGR to RGB for plt.imshow
    th3 = cv2.cvtColor(th3, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.imshow(cropped_image)
    plt.imshow(th3)
    plt.show()
    cv2.waitKey(0)  # Wait for a key event
    cv2.destroyAllWindows()  # Destroy all windows

if __name__ == '__main__':
    main()