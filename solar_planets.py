import cv2
import numpy as np

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            'Sun',
            (20,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color =(0, 0, 0),
            thickness= 2)


cv2.putText(img,
            'Mercury',
            (115,250),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color =(173, 173, 169),
            thickness= 1)


cv2.putText(img,
            'Venus',
            (180,180),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color =(93, 176, 222),
            thickness= 1)


cv2.putText(img,
            'Earth',
            (295,270),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color =(86, 181, 60),
            thickness= 1)


cv2.putText(img,
            'Moon',
            (310,150),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color =(255,255,255),
            thickness= 1)

cv2.putText(img,
            'Mars',
            (380,260),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color =(78, 119, 251),
            thickness= 1)

cv2.putText(img,
            'Saturn',
            (780,115),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color =(163, 161, 157),
            thickness= 1)

cv2.putText(img,
            'Uranus',
            (990,290),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color =(244, 243, 206),
            thickness= 1)

cv2.putText(img,
            'Neptune',
            (1150,150),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color =(189, 56, 35),
            thickness= 1)


cv2.putText(img,
            'Jupitar',
            (610,365),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.5,
            color =(37, 181, 237),
            thickness= 1)


cv2.imshow("output",img)
cv2.waitKey(0)