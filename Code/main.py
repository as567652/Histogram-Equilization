import cv2 as cv
import matplotlib.pyplot as plt

# Reading Images From Current Folder
im = cv.imread('Code/Images/1.tif')

# Making copy of the image for manipulation
cpy = im.copy()

# Making Histogram of Original Image
histogram = cv.calcHist([im], [0], None, [256], [0, 256])

# Total number of pixels available
total = len(im) * len(im[0])

# Making a temporary buffer to store values of equalized histogram
buff = list()

# initializing first value
buff.append(round(256 * (histogram[0][0] / total)))

# calculating each pixel value based on frequency and previous pixel value
for i in range(1, len(histogram)):
    new_val = 256 * (histogram[i][0] / total) + buff[i - 1]
    buff.append(round(new_val))

# Showing Original Image
plt.figure()
plt.imshow(im)
plt.title('Original Image')
plt.xticks([])
plt.yticks([])
plt.show()

# Making Histogram for original image
plt.figure()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.plot(histogram)
plt.title('Histogram Of Original Image')
plt.xlim([0,255])
plt.show()

# Making Histogram for buffered image
plt.figure()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.plot(buff)
plt.title('Histogram Of Equalized Image')
plt.xlim([0,255])
plt.show()

# Manipulating copied image with values from buffer
for i in range(len(cpy)):
    for j in range(len(cpy[0])):
        for k in range(len(cpy[0][0])):
            cpy[i][j][k] = min(buff[cpy[i][j][k]], 255)

# Showing Equalized Image
plt.figure()
plt.imshow(cpy)
plt.title('Equalized Image')
plt.xticks([])
plt.yticks([])
plt.show()