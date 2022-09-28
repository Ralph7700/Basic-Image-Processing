import urllib.request
from PIL import Image

Url = 'https://haqqstorage.blob.core.windows.net/profile-pictures-prod/2d7efbce-553d-488d-9dee-271489c8a1c7blob' \
      '?1664281296123 '
FileName = './InitialImage.jpg'


def DownloadImage(url, path):
    urllib.request.urlretrieve(url, path)


DownloadImage(Url, FileName)
