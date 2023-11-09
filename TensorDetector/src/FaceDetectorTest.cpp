#include <opencv2/opencv.hpp>

using namespace cv;

int main() {
  const string rtspStreamURL = "rtsp://192.168.1.100:554/stream1";
  // Load the video file
  VideoCapture capture(rtspStreamURL);

  // Check if the video file was opened successfully
  if (!capture.isOpened()) {
    return -1;
  }

  // Create a cascade classifier for face detection
  CascadeClassifier faceCascade;
  if (!faceCascade.load("haarcascade_frontalface_default.xml")) {
    return -1;
  }

  // Process each frame of the video
  while (true) {
    // Capture the next frame
    Mat frame;
    capture >> frame;

    // Check if the frame is empty
    if (frame.empty()) {
      break;
    }

    // Convert the frame to grayscale
    Mat grayscaleFrame;
    cvtColor(frame, grayscaleFrame, COLOR_BGR2GRAY);

    // Detect faces in the frame
    vector<Rect> faces;
    faceCascade.detectMultiScale(grayscaleFrame, faces, 1.1, 4, 0 | CASCADE_SCALE_IMAGE, Size(30, 30));

    // Draw a bounding box around each detected face
    for (Rect face : faces) {
      rectangle(frame, face, Scalar(0, 255, 0), 2);
    }

    // Display the frame
    imshow("Face Detection", frame);

    // Check if the user wants to quit
    if (waitKey(1) == 27) {
      break;
    }
  }

  // Close the video file
  capture.release();

  // Destroy all windows
  destroyAllWindows();

  return 0;
}