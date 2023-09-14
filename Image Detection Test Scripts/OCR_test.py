import cv2
import numpy as np
from easyocr import Reader
from matplotlib import pyplot as plt
import imutils

def cleanup_text(text):
	# strip out non-ASCII text so we can draw the text on the image
	# using OpenCV
	return "".join([c if ord(c) < 128 else "" for c in text]).strip()

img = cv2.imread("Image Detection Test Scripts/OCR7.png")

#img = imutils.rotate(img, 90)

reader = Reader(['en'], gpu=True)
#   detect the text from the license plate
detection = reader.readtext(img)
print(detection)

# loop over the results
for (bbox, text, prob) in detection:
	# display the OCR'd text and associated probability
	print("[INFO] {:.4f}: {}".format(prob, text))
	# unpack the bounding box
	(tl, tr, br, bl) = bbox
	tl = (int(tl[0]), int(tl[1]))
	tr = (int(tr[0]), int(tr[1]))
	br = (int(br[0]), int(br[1]))
	bl = (int(bl[0]), int(bl[1]))
	# cleanup the text and draw the box surrounding the text along
	# with the OCR'd text itself
	text = cleanup_text(text)
	cv2.rectangle(img, tl, br, (0, 255, 0), 2)
	cv2.putText(img, text, (tl[0], tl[1] - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
# show the output image
plt.imshow(img)
plt.show()
cv2.waitKey(0)

