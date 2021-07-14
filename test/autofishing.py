import cv2 as cv
import numpy as np

img = cv.imread("test/test.png", cv.IMREAD_UNCHANGED)
img2 = cv.imread("test/bar2.png", cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(img, img2, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print("Best match top left position:%s" % str(max_loc))
print("Beat match cconfidence: %s" % max_val)

threshold = 0.8
if max_val >= threshold:
    print("Found needle")

    needle_w = img2.shape[1]
    needle_h = img2.shape[0] 

    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(img, top_left, bottom_right,
                  color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    #cv.imwrite("test.png", result)
    cv.imshow("Result", img)
    cv.waitKey(0)

else:
    print("Needle not found")
