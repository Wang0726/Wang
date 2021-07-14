import cv2
import numpy as np

img = cv2.imread("autofish/bar.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread("autofish/template_bar.png", cv2.IMREAD_GRAYSCALE)
w, h = img2.shape

result = cv2.matchTemplate(gray_img, img2, cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.81)

for pt in zip(*loc):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)
    print(pt)

cv2.imshow("img", gray_img)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()