
##iv)Image Reflection
iv)Image Reflection
import cv2
import numpy as np
from matplotlib import pyplot as plt
def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
image_url = r"C:\Users\admin\Downloads\gray .jpg"
image = cv2.imread(image_url)
reflected_image_horizontal = cv2.flip(image, 1)
reflected_image_vertical = cv2.flip(image, 0)
reflected_image_both = cv2.flip(image, -1)
print("Original Image:")
show_image(image)
print("Reflected Horizontally:")
show_image(reflected_image_horizontal)
print("Reflected Vertically:")
show_image(reflected_image_vertical)
print("Reflected Both:")
show_image(reflected_image_both)


##v)Image Rotation :
import cv2
import numpy as np
from matplotlib import pyplot as plt
def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
image_url = r"C:\Users\admin\Downloads\gray .jpg"
image = cv2.imread(image_url)
angle = 45
height, width = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
print("Original Image:")
show_image(image)
print("Rotated Image:")
show_image(rotated_image)

##vi)Image Cropping:

import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_image(image):
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

image_url = r"C:\Users\admin\Downloads\gray .jpg"
image = cv2.imread(image_url)
x = 100  
y = 50  
width = 200 
height = 150  
cropped_image = image[y:y+height, x:x+width]
print("Original Image:")
show_image(image)
print("Cropped Image:")
show_image(cropped_image)

