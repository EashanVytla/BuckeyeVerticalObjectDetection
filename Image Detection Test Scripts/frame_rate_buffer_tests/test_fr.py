import cv2

cap = cv2.VideoCapture('rtsp://<ip_address>:<port>/<stream_name>')

# Set the frame rate
cap.set(cv2.CAP_PROP_FPS, 10)

# Read the next frame
ret, frame = cap.read()

# Display the frame
cv2.imshow('frame', frame)

# Press any key to quit
cv2.waitKey(0)

# Release the capture
cap.release()