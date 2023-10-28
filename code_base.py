import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/Users/danielsarmiento/Downloads/Untitled 1.png')
print(img.shape)
img = img[300:1200,350:3000,::]
cv2.imwrite("./resistencia.jpeg", img)
plt.imshow(img)
plt.axis(False)
plt.show()