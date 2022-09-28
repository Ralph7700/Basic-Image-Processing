import urllib.request
import cv2
import os
import time

Url = 'https://haqqstorage.blob.core.windows.net/profile-pictures-prod/2d7efbce-553d-488d-9dee-271489c8a1c7blob' \
      '?1664281296123 '
ImagePath = os.getcwd() + '\Images\CVInitialImage.jpg'

Dimension = 320


def DownloadImage(url, path):
    urllib.request.urlretrieve(url, path)


def Resize(path):
    tic = time.perf_counter()
    resizedImage = cv2.imread(path)
    result = cv2.resize(resizedImage, (Dimension, Dimension), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(os.getcwd() + '\Images\CVResizedImage.jpg', result)
    toc = (time.perf_counter() - tic) * 1000
    print("resizing time: " + toc.__str__())


def Blur():
    tic = time.perf_counter()
    blurredImage = cv2.imread(os.getcwd() + '\Images\CVResizedImage.jpg')
    result = cv2.blur(blurredImage, (Dimension, Dimension), cv2.BORDER_DEFAULT)
    cv2.imwrite(os.getcwd() + '\Images\CVBlurredImage.jpg', result)
    toc = (time.perf_counter() - tic) * 1000
    print('blurring time: ' + toc.__str__())


def Process():
    DownloadImage(Url, ImagePath)
    Resize(ImagePath)
    Blur()


Process()
