# Implementation

I've tried a couple of models:

1.1) EasyOCR Base - 0.868
1.2) EasyOCR Base + MedianBlur - 0.860
2.1) Pytesseract Base - 0.76

I chose the EasyOCR model.

Then I decided to fine-tune EasyOCR model for the better quality. Firstly, I generated a synthetic dataset using the next article: https://blog.devgenius.io/generating-a-fine-tuning-dataset-for-an-ocr-engine-3509167bc8a1 (both on Chinese and English). Then I realized the fine-tune using the next article: https://pub.towardsai.net/how-to-fine-tune-easyocr-to-achieve-better-ocr-performance-1540f5076428 and the EasyOCR repository on GitHub: https://github.com/JaidedAI/EasyOCR/tree/master with the instructions. The problem is that I do not have the GPU, so it is nearly impossible to fine-tune the model, but at least I ran the fine-tune and checked that it works. Using the GPU and good real dataset (preferabble not synthetic) it is possible to upgrade the performance of the model.
