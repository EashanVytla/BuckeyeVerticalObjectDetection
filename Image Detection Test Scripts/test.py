from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('runs\\detect\\BVTargetModel16\\weights\\best.pt')

# Load the video file
video_file = "C:\\Data\\Buckeye Vertical\\Prelim Detection Dataset\\test\\images\\IMG_4422.MOV"

# Validate the model with the video and save the output video
model.predict(video_file, save=True, imgsz=640, conf=0.5)