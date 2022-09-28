import urllib.request
from PIL import Image, ImageFilter
import time

Url = 'https://haqqstorage.blob.core.windows.net/profile-pictures-prod/2d7efbce-553d-488d-9dee-271489c8a1c7blob' \
      '?1664281296123 '
ImagePath = './Images/PILInitialImage.jpg'
Dimension = 320

def DownloadImage(url, path):
    urllib.request.urlretrieve(url, path)

def Resize(path):
    tic = time.perf_counter()
    resizedImage = Image.open(path)
    resizedImage.resize((Dimension,Dimension)).save('./Images/PILResized.jpg')
    toc = (time.perf_counter() - tic)*1000
    print("resizing time: " + toc.__str__())


def Blur():
    tic = time.perf_counter()
    blurredImage = Image.open('./Images/PILResized.jpg')
    blurredImage.filter(ImageFilter.BoxBlur(4)).save('./Images/PILBlurred.jpg')
    toc = (time.perf_counter() - tic)*1000
    print('blurring time: '+toc.__str__())


DownloadImage(Url, ImagePath)
Resize(ImagePath)
Blur()