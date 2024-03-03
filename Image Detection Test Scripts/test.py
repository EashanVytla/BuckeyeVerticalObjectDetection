from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('runs\\detect\\OCR.pt')

# Load the video file
video_file = "C:\Data\Buckeye Vertical\Image Classifier\BuckeyeVerticalObjectDetection\Script Test Data\OCR5x2.png"

# Validate the model with the video and save the output video
model.predict(video_file, save=False, imgsz=320, conf=0.5)