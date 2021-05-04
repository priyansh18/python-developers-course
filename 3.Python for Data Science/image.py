
import cv2

# Cv2 reads image in default format while matplotlib converts it from BGR to RGB while reading the image
image = cv2.imread('bulbasaur.jpg')
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Dog Image', image)
cv2.imshow('Grey Dog Image', grey_image)

cv2.waitKey(0)  # Program will stopped when any key is pressed
cv2.destroyAllWindows()
