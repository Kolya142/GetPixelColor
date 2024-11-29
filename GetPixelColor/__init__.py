# python module for getting the color of a pixel on screen

# import the necessary modules
from io import BytesIO
import os
import platform
from typing import Tuple, Union  
from PIL import Image
from sys import platform
import pyautogui
import numpy as np

if platform == "win32":
    import win32gui




def _checkForIssues(num: Union[int, any]):
    if type(num) != int:
        raise TypeError("x, y, width, and height must be integers")
    if num < 0:
        raise ValueError("x, y, width, and height must be positive")




# platform functions
def _do_win32_pixel(x: int, y: int) -> Tuple[int, int]:
    im = win32gui.GetPixel(win32gui.GetDC(win32gui.GetDesktopWindow()), x, y)
    return im.getpixel((0, 0))

def _do_linux_pixel(x: int, y: int) -> Tuple[int, int]:
    im = pyautogui.screenshot('/tmp/screenshot.png', region=(x, y, 1, 1))
    return im.getpixel((0, 0))

def _do_darwin_pixel(x: int, y: int) -> Tuple[int, int]:
    path = os.path.dirname(os.path.abspath(__file__)) + "/static/get-pixel-color"

    if not os.access(path, os.X_OK):
        os.chmod(path, 0o755)

    return tuple(int(i) for i in os.popen(path + " " + str(x) + " " + str(y)).read().replace("\n", "").strip('( )').split(','))
# end platform functions



# crossplatform functions
def pixel(x: int, y: int) -> Union[None, Tuple[int, int]]:
    _checkForIssues(x)
    _checkForIssues(y)
    if platform == "darwin":
        return _do_darwin_pixel(x, y)
    elif platform == "win32" or platform == "linux" or platform == "linux2":
        if platform == "win32":
            return _do_win32_pixel(x, y)

        elif platform == "linux" or platform == "linux2":
            return _do_linux_pixel(x, y)
    else:
        raise OSError("Error: Unsupported operating system.")


# remove local functions
del _do_darwin_pixel, _do_linux_pixel, _do_win32_pixel, _checkForIssues

# def average(x, y, width, height):
#     checkForIssues(x)
#     checkForIssues(y)
#     checkForIssues(width)
#     checkForIssues(height)
#     if (platform == "darwin"):
#         from pasteboard import TIFF, Pasteboard
#         os.system('/usr/sbin/screencapture -R ' + str(x) + ',' + str(y) + ',' + str(width) + ',' + str(height) + ' -c')
#         im = Pasteboard().get_contents(TIFF)
#         im = Image.open(BytesIO(im))
#         return (tuple(np.average(np.array(im), axis=(0,1)).astype(int)))
#     elif (platform == "win32" or platform == "linux" or platform == "linux2"):
#         # screenshot the area, saving to a temporary folder based on the OS
#         if (platform == "win32"):
#             im = pyautogui.screenshot('C:\\Windows\\Temp\\screenshot.png', region=(x, y, width, height))
#         elif (platform == "linux" or platform == "linux2"):
#             im = pyautogui.screenshot('/tmp/screenshot.png', region=(x, y, width, height))
#         return (tuple(np.average(np.array(im), axis=(0,1)).astype(int)))
#     else:
#         return ("Error: Unsupported operating system.")

# def area(x, y, width, height):
#     checkForIssues(x)
#     checkForIssues(y)
#     checkForIssues(width)
#     checkForIssues(height)
#     if (platform == "darwin"):
#         from pasteboard import TIFF, Pasteboard
#         os.system('/usr/sbin/screencapture -R ' + str(x) + ',' + str(y) + ',' + str(width) + ',' + str(height) + ' -c')
#         im = Pasteboard().get_contents(TIFF)
#         im = Image.open(BytesIO(im))
#         return (np.array(im).tolist())
#     elif (platform == "win32" or platform == "linux" or platform == "linux2"):
#         # screenshot the area, saving to a temporary folder based on the OS
#         if (platform == "win32"):
#             im = pyautogui.screenshot('C:\\Windows\\Temp\\screenshot.png', region=(x, y, width, height))
#         elif (platform == "linux" or platform == "linux2"):
#             im = pyautogui.screenshot('/tmp/screenshot.png', region=(x, y, width, height))
#         return (np.array(im).tolist())
#     else:
#         return ("Error: Unsupported operating system.")