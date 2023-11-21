from pathlib import Path
from paddleocr import PaddleOCR
import easyocr


class OCRModel:
    def recognize_text(self, image: Path) -> str:
        """
        This method takes an image file as input and returns the recognized text from the image.

        :param image: The path to the image file.
        :return: The recognized text from the image.
        """
        img_path = str(image)
        # img_path = "/Users/aragonerua/Documents/GitHub/text-recognition-test-task/data/public_data/1.png"
        # ocr = PaddleOCR(use_angle_cls=True)
        # result = ocr.ocr(img_path)
        reader = easyocr.Reader(['en', 'ch_sim'])
        text = reader.readtext(img_path)
        result_string = ""
        for message in text:
            result_string += message[1] + "\n"
        return result_string
        # return text[0][1]


# model = OCRModel()
# print(model.recognize_text(Path("/Users/aragonerua/Documents/GitHub/text-recognition-test-task/data/public_data/5.png")))