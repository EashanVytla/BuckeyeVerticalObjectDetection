import cv2
import torch
from ultralytics import YOLO

torch.cuda.set_device(0)

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

# Define paths to your model and image
model_path = r"C:\Data\Buckeye Vertical\Image Classifier\BuckeyeVerticalObjectDetection\runs\detect\OCR.pt"
image_path = r"C:\Data\Buckeye Vertical\Image Classifier\BuckeyeVerticalObjectDetection\Script Test Data\OCR5x1.png"

# Load the YOLOv8 model
model = YOLO(model_path)

# Read the image
image = cv2.imread(image_path)

# Perform inference
results = model(image)

for r in results:
    #r.show()
    print(arr[int(r.boxes.cls[0].item())])
    #pos = r.boxes.xywh
    #cv2.rectangle(image, (int(pos[0][0]), int(pos[0][1])), (int(pos[0][0] + pos[0][2]), int(pos[0][1] + pos[0][3])), (255, 0, 0), 2)

#cv2.imshow("Image", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()