import cv2
img = cv2.imread("butterfly.jpg")
cv2.putText(img, "Butterfly is blue", (20,300), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1.42, color=(250,0,34))
cv2.imshow("This is a butterfly: ", img)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Now butterfly is grey: ", grey)
cv2.waitKey(0)