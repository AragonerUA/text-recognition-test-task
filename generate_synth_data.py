import codecs
from trdg.generators import (
    GeneratorFromStrings,
)
from tqdm.auto import tqdm
import os
import pandas as pd
import numpy as np
import random
from faker import Faker


fake = Faker(["en_US", "zh_CN"])
list_of_generated_data = list()
for _ in range(160000):
    sent = fake.sentence()
    if len(sent) >= 5:
        list_of_generated_data.append(sent)
print(list_of_generated_data, len(list_of_generated_data))

NUM_IMAGES_TO_SAVE = 100000

# english_font_path = "deep_text_recognition_benchmark/fonts/english_font.ttf"
# english_font_path = "deep_text_recognition_benchmark/fonts/english_regular.ttf"
english_font_path = "deep_text_recognition_benchmark/fonts/en.ttf"

# chinese_font_path = "deep_text_recognition_benchmark/fonts/chinese_font.ttf"
# chinese_font_path = "deep_text_recognition_benchmark/fonts/ch_en_font.ttf"
# chinese_font_path = "deep_text_recognition_benchmark/fonts/traditional_chinese_font.ttf"
# chinese_font_path = "deep_text_recognition_benchmark/fonts/ch_full.ttf"
# chinese_font_path = "deep_text_recognition_benchmark/fonts/chinese_font_.ttf"
chinese_font_path = "deep_text_recognition_benchmark/fonts/NotoSans.ttf"


#generate the images
generator = GeneratorFromStrings(
    random.sample(list_of_generated_data, 10000),
    fonts=[english_font_path, chinese_font_path],
    # fonts=font,

    # uncomment the lines below for some image augmentation options
    # blur=6,
    # random_blur=True,
    # random_skew=True,
    # skewing_angle=20,
    # background_type=1,
    # text_color="red",
)

# save images from generator
# if output folder doesn't exist, create it
if not os.path.exists('deep_text_recognition_benchmark/output'):
    os.makedirs('deep_text_recognition_benchmark/output')
# if labels.txt doesn't exist, create it
if not os.path.exists('deep_text_recognition_benchmark/output/labels.txt'):
    f = codecs.open("deep_text_recognition_benchmark/output/labels.txt", "w")
    f.close()

# open txt file
current_index = len(os.listdir('deep_text_recognition_benchmark/output')) - 1  # all images minus the labels file
f = codecs.open("deep_text_recognition_benchmark/output/labels.txt", "a")

for counter, (img, lbl) in tqdm(enumerate(generator), total = NUM_IMAGES_TO_SAVE):
    if (counter >= NUM_IMAGES_TO_SAVE):
        break
    # img.show()
    # save pillow image
    if current_index % 2 != 0:
        try:
            img.save(f'deep_text_recognition_benchmark/output/image{current_index}.png')
            f.write(f'image{current_index}.png {lbl}\n')
        except:
            continue
    # f.write(f'image{current_index}.png {lbl}\n')
    current_index += 1
    # Do something with the pillow images here.
f.close()
