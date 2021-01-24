
import cv2
import numpy as np
import matplotlib.pyplot as plt % matplotlib
inline

# path of segementation features of vehicles,doors, stairs and animals
stairs_cascade = cv2.CascadeClassifier('C:\Users\Maliks\Desktop\haar_feature_segmentation_for_vehicles\cascade.xml')
vehicles_cascade = cv2.CascadeClassifier('C:\Users\Maliks\Desktop\haar_feature_segmentation_for_stairs\cascade.xml')
doors_cascade = cv2.CascadeClassifier('C:\Users\Maliks\Desktop\haar_feature_segmentation_for_doors\cascade.xml')
animals_cascade = cv2.CascadeClassifier('C:\Users\Maliks\Desktop\haar_feature_segmentation_for_animals\cascade.xml')


#  function for stair segmentation
def adjusted_segmentation_stairs(img):
    stairs_img = img.copy()

    stairs_rect = stairs_cascade.detectMultiScale(stairs_img,scaleFactor=1.4,minNeighbors=6)

    for (x, y, w, h) in stairs_rect:
        cv2.rectangle(stairs_img, (x, y),(x + w, y + h), (255, 255, 255), 10) \
\
                return stairs_img


# function for vehicles segmentation
def adjusted_segmentation_vehicles (img):
    vehicles_img = img.copy()
    vehicles_rect = vehicles_cascade.detectMultiScale(vehicles_img,scaleFactor=1.4,minNeighbors=6)
    for (x, y, w, h) in vehicles_rect:
        cv2.rectangle(vehicles_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)
    return vehicles_img

def adjusted_segmentation_animals (img):
    animals_img = img.copy()
    animals_rect = animals_cascade.detectMultiScale(animals_img,scaleFactor=1.4,minNeighbors=6)
    for (x, y, w, h) in animals_rect:
        cv2.rectangle(animals_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)
    return animals_img
#  function for stair segmentation
def adjusted_segmentation_doors(img):
    doors_img = img.copy()

    doors_rect = doors_cascade.detectMultiScale(doors_img,scaleFactor=1.4,minNeighbors=6)

    for (x, y, w, h) in doors_rect:
        cv2.rectangle(doors_img, (x, y),
                      (x + w, y + h), (255, 255, 255), 10)
     return doors_img



# testing image for stairs
testimg = cv2.imread('C:\Users\Maliks\Desktop\haar_feature_segmentation_for_stairs\p\image_1')
img_copy1 = testimg.copy()
img_copy2 = testimg.copy()
img_copy3 = testimg.copy()

# Detecting the stairs
stairs = adjusted_segmentation_stairs(img_copy3)
plt.imshow(stairs)



# testing image for vehicles
testimg1 = cv2.imread('C:\Users\Maliks\Desktop\haar_feature_segmentation_for_vehicles\p\image_38')
img_copy11 = testimg1.copy()
img_copy22 = testimg1.copy()
img_copy33 = testimg1.copy()

# Detecting the vehicles
vehicles = adjusted_segmentation_vehicles(img_copy33)
plt.imshow(vehicles)

# testing image for animals
testimg2 = cv2.imread('C:\Users\Maliks\Desktop\haar_feature_segmentation_for_animals\p\image_31')
img_copy111 = testimg2.copy()
img_copy222 = testimg2.copy()
img_copy333 = testimg2.copy()

# Detecting the animals
animals = adjusted_segmentation_animals(img_copy333)
plt.imshow(animals)

# testing image for doors
testimg3 = cv2.imread('C:\Users\Maliks\Desktop\haar_feature_segmentation_for_doors\p\image_18')
img_copy1111 = testimg3.copy()
img_copy2222 = testimg3.copy()
img_copy3333 = testimg3.copy()

# Detecting the doors
doors = adjusted_segmentation_doors(img_copy3333)
plt.imshow(doors)
