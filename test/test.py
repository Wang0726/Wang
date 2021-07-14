import cv2 as cv
import numpy as np
import os

from win32ui import debug


def find(needle_img_path, min_img_path, threshold=0.8, debug_mode=None):


    min_img = cv.imread("min_img_path", cv.IMREAD_UNCHANGED)
    needle_img = cv.imread("needle_img_path", cv.IMREAD_UNCHANGED)

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

#min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(min_img, needle_img, method)
#print("Best match top left position:%s" % str(max_loc))
#print("Beat match cconfidence: %s" % max_val)
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    #print(rectangles)

    points = []
    if len(rectangles):
        print("Found needle")

        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        for (x, y, w, h) in rectangles:

            center_x = x + int(w/2)
            center_y = y + int(h/2)

            points.append((center_x, center_y))

            if debug_mode == "rectangles":
                top_left = (x, y)
                bottom_right = (x + w, y + h)

                cv.rectangle(min_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

            elif debug_mode == "points":
                cv.drawMarker(min_img, (center_x, center_y), marker_color)

        if debug_mode:
            cv.imshow("Result", min_img)
            cv.waitKey(0)
    
    
    return points

points = find("test/test.py", "test/bar2.py", debug_mode="points")
print(points)

