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

  // Process each frame of the video
  while (true) {
    // Capture the next frame
    Mat frame;
    capture >> frame;

    // Check if the frame is empty
    if (frame.empty()) {
      break;
    }

    // Display the frame
    imshow("Frame", frame);

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