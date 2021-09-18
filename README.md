# Histogram Equilization

Code snippet to adjust image contrast using Histogram Equalization with the help of **OpenCV** and **Matplotlib** library in python 3.

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Setup](#setup)
* [Launch](#launch)
* [Working](#working)
* [Illustrations](#illustrations)
* [Status](#status)
* [Sources](#sources)
* [Other](#other)


## Introduction
Histograms are the basis for numerous spatial domain processing techniques. Histogram manipulation can be used for image enhancement. Information inhereted from histogram is quite useful in other image processing applications, such as image compression and segmentation. Histograms are simple to calculate in software and also lend themselves to economic hardware implementations, thus making them a popular tool for real-time image processing.
<br>
In this code i have tried to implement histogram equilization where image with low contrast or high contrast can be modified to look like new and refreshing image just by application of simple mathematics.
<br>
<br>
**Histograms of an image before and after equalization.**
<p align = 'center'>
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/Histogrammeinebnung.png" width=50%>
</p>


## Technologies
  #### Software Used :
  * VS Code 1.60.1
  #### Languages Used :
  * Python 3
  #### OS used :
   * Ubuntu 20.04.3 LTS 64-bit


## Setup
First you must have these libraries and languages installed on your system -
  * [Python 3](https://www.python.org/)
  * [OpenCV](https://opencv.org/)
  * [Matplotlib](https://matplotlib.org/)


## Launch
To run the code, run this commands in terminal with main.py as in current directory and images in Images folder along with main.py
```
$ python3 main.py
```
Window will pop-up with resultant images and their histograms.


## Working
Modified image is obtained by mapping each pixel in the input image with intensity r k into a corresponding pixel with level *sk* in the output image.
Using this formula we can calculate new intensity of image based on intensities of whole image.
<br>
<p align = 'center'>
  <img src="Readme Images/formula_used.png" width=50% title="Formula Used">
</p>
<br>
Here,
MN is the total number of pixels in the image, nk is the number of pixels that have intensity rk and L is the number of possible intensity levels in the image

<br>
Source :- Digital Image Processing (Third Edition) by Rafael C. Gonzalez and Richard E. Woods Topic - 3.3.1 (Pg 120)

## Illustrations

### Test-0

Image Type - Low Contrast Image

<p>
  <img src="Readme Images/Test-0/Original.png" width=48% title="Original Image">
  <img src="Readme Images/Test-0/Hist_Original.png" width=48% title="Histogram Of Original Image">
</p>
<p>
  <img src="Readme Images/Test-0/Equalized.png" width=48% title="Equalized Image">
  <img src="Readme Images/Test-0/Hist_Equalized.png" width=48% title="Histogram Of Equalized Image">
</p>

### Test-1

Image Type - High Contrast Image

<p>
  <img src="Readme Images/Test-1/Original.png" width=48% title="Original Image">
  <img src="Readme Images/Test-1/Hist_Original.png" width=48% title="Histogram Of Original Image">
</p>
<p>
  <img src="Readme Images/Test-1/Equalized.png" width=48% title="Equalized Image">
  <img src="Readme Images/Test-1/Hist_Equalized.png" width=48% title="Histogram Of Equalized Image">
</p>

## Project status
  ***Completed***


## Sources
  * Images used in this project may be subject to copyright.
  * [Digital Image Processing (Third Edition) by Rafael C. Gonzalez and Richard E. Woods](https://www.amazon.com/Digital-Image-Processing-Rafael-Gonzalez/dp/013168728X)
  * [OpenCV Documentation](https://docs.opencv.org/2.4/opencv_tutorials.pdf)
  * [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
  

## Other
  This code was contributed by Abhinav Sharma.

