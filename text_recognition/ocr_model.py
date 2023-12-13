from pathlib import Path

import pytesseract
from paddleocr import PaddleOCR, draw_ocr
import easyocr


class OCRModel:
    def recognize_text(self, image: Path) -> str:
        """
        This method takes an image file as input and returns the recognized text from the image.

        :param image: The path to the image file.
        :return: The recognized text from the image.
        """
        img_path = str(image)
        reader_ = easyocr.Reader(['en', 'ch_sim'], detector='DB', recognizer='transformer')
        text = reader_.readtext(img_path)

        # text = reader.readtext(img_path)
        result_string = ""
        for message in text:
            result_string += message[1] + "\n"
        return result_string  # 0.868
