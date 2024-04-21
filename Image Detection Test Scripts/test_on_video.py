from ultralytics import YOLO
import torch
import cv2
import imutils

torch.cuda.set_device(0)
cls_arr = ['Black_Rectangle',
 'Red_Rectangle',
 'Blue_Rectangle',
 'Green_Rectangle',
 'White_Rectangle',
 'Purple_Rectangle',
 'Brown_Rectangle',
 'Orange_Rectangle',
 'Black_Circle',
 'Red_Circle',
 'Blue_Circle',
 'Green_Circle',
 'White_Circle',
 'Purple_Circle',
 'Brown_Circle',
 'Orange_Circle',
 'Black_Triangle',
 'Red_Triangle',
 'Blue_Triangle',
 'Green_Triangle',
 'White_Triangle',
 'Purple_Triangle',
 'Brown_Triangle',
 'Orange_Triangle',
 'Black_Semicircle',
 'Red_Semicircle',
 'Blue_Semicircle',
 'Green_Semicircle',
 'White_Semicircle',
 'Purple_Semicircle',
 'Brown_Semicircle',
 'Orange_Semicircle',
 'Black_Quartercircle',
 'Red_Quartercircle',
 'Blue_Quartercircle',
 'Green_Quartercircle',
 'White_Quartercircle',
 'Purple_Quartercircle',
 'Brown_Quartercircle',
 'Orange_Quartercircle',
 'Black_Pentagon',
 'Red_Pentagon',
 'Blue_Pentagon',
 'Green_Pentagon',
 'White_Pentagon',
 'Purple_Pentagon',
 'Brown_Pentagon',
 'Orange_Pentagon',
 'Black_Star',
 'Red_Star',
 'Blue_Star',
 'Green_Star',
 'White_Star',
 'Purple_Star',
 'Brown_Star',
 'Orange_Star',
 'Black_Cross',
 'Red_Cross',
 'Blue_Cross',
 'Green_Cross',
 'White_Cross',
 'Purple_Cross',
 'Brown_Cross',
 'Orange_Cross']
char_arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

#obj_model = YOLO(r"E:\Model Archive\Feb29_2\Feb29RL.pt")
obj_model = YOLO(r"F:\best.pt")
char_model = YOLO(r"C:\Data\Buckeye Vertical\Image Classifier\BuckeyeVerticalObjectDetection\runs\detect\OCR.pt")

counter_arr = []
for i in range(64):
    counter_arr.append(0)

prev_counter_arr = []
for i in range(64):
    prev_counter_arr.append(0)

# Open the video file
video_path = r"C:\Data\Buckeye Vertical\Image Classifier\BuckeyeVerticalObjectDetection\Script Test Data\4xZoomCrop.mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    frame = imutils.resize(frame, width=1280)

    if success:
        # Run YOLOv8 inference on the frame
        results = obj_model(frame)
        
        for r in results:
            for j in range(r.boxes.cls.size(dim=0)):
                index = int(r.boxes.cls[j].item())
                text = cls_arr[index]
                counter_arr[index] += 1

                pos = r.boxes.xyxy[j]

                for i in range(len(counter_arr)):
                    if counter_arr[i] == prev_counter_arr[i]:
                        counter_arr[i] = 0

                if(counter_arr[index] >= 15):
                    results_char = char_model(frame[int(pos[1].item()):int(pos[3].item()), int(pos[0].item()):int(pos[2].item())])
                    for r_char in results_char:
                        if r_char.boxes.cls.size(dim=0) != 0:
                            text += "_" + char_arr[int(r_char.boxes.cls[0].item())]
                            #print("Nothing")

                if(r.boxes.conf[j] > 0.5):
                    cv2.rectangle(frame, (int(pos[0].item()), int(pos[1].item())), (int(pos[2].item()), int(pos[3].item())), (0, 255, 0), 2)
                    cv2.putText(frame, text, (int(pos[0].item()), int(pos[1].item()) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", frame)

        prev_counter_arr = counter_arr.copy()

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        print("Failed")
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()