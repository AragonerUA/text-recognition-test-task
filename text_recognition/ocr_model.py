from pathlib import Path

import pytesseract
import keras_ocr
from paddleocr import PaddleOCR, draw_ocr
import easyocr
import cv2
import numpy as np
import os


class OCRModel:
    def image_prerpocessing(self, img_path: str) -> np.ndarray:
        """
        Preprocess the input image by converting it to grayscale and applying thresholding.

        :param img_path: format - str: Path to the input image.
        :return: format - numpy.ndarray: preprocessed image.
        """
        # Loading the image
        preprocessed_img = cv2.imread(str(img_path))

        # Grayscale convert
        img = cv2.cvtColor(preprocessed_img, cv2.COLOR_BGR2GRAY)

        # Thresholding
        _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

        # medianBlur and equalize histogram
        img = cv2.medianBlur(img, 3)
        img = cv2.equalizeHist(img)
        return img


    def recognize_text(self, image: Path) -> str:
        """
        This method takes an image file as input and returns the recognized text from the image.

        :param image: The path to the image file.
        :return: The recognized text from the image.
        """
        img_path = str(image)
        reader_ = easyocr.Reader(['en', 'ch_sim'], detector='DB', recognizer='transformer')
        text = reader_.readtext(img_path, slope_ths=0.15, add_margin=0.2, width_ths=1, height_ths=1)

        result_string = ""
        for message in text:
            result_string += message[1] + "\n"
        return result_string
