from ultralytics import YOLO
import cv2
import imutils
from easyocr import Reader
from matplotlib import pyplot as plt

model = YOLO('runs\\detect\\BVTargetModel16\\weights\\best.pt')  # load a pretrained model (recommended for training)

# Open the video file
video_path = "C:\\Data\\Buckeye Vertical\\Prelim Detection Dataset\\test\\images\\IMG_4422.MOV"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    frame = imutils.resize(frame, width=640)

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        box = results[0].boxes[0]
        
        pos = (int(box.xyxy[0][0].item()), int(box.xyxy[0][1].item()))

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        x = int(box.xyxy[0][0].item()) + 30
        y = int(box.xyxy[0][1].item()) + 30
        width = int(box.xywh[0][2].item() - 50)
        height = int(box.xywh[0][3].item() - 50)
        cropped_image = annotated_frame[y:y+height, x:x+width]

        # Convert the image to grayscale
        gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

        gray = imutils.resize(gray, width=320)

        ret3,th3 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        th3 = cv2.GaussianBlur(th3,(11,11),0)

        reader = Reader(['en'])
        detection = reader.readtext(th3, rotation_info=[15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270])
        print(detection)

        # Display the annotated frame
        plt.imshow(annotated_frame)
        plt.pause(0.001)

    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
plt.close()