# -*- coding: utf-8 -*-
from datetime import datetime
from PIL import ImageGrab
from PIL import Image
import os

def analyze_current_screen_text(directory=".", compress_level=1):
    """
    capture the android screen now

    :return:
    """
    print("capture time: ", datetime.now().strftime("%H:%M:%S"))
    screenshot_filename = "screenshot.png"
    save_text_area = os.path.join(directory, "text_area.png")
    capture_screen(screenshot_filename, directory)
    parse_answer_area(os.path.join(directory, screenshot_filename), save_text_area, compress_level)
    return get_area_data(save_text_area)


def capture_screen(filename="screenshot.png", directory="."):
    """
    
    :param filename:
    :param directory:
    :return:
    """
    im = ImageGrab.grab()
    im.save(os.path.join(directory, filename))


def parse_answer_area(source_file, text_area_file, compress_level):
    """
    crop the answer area

    :return:
    """

    image = Image.open(source_file)
    if compress_level == 1:
        image = image.convert("L")
    elif compress_level == 2:
        image = image.convert("1")
    wide = image.size[0]
    print("screen width: {0}, screen height: {1}".format(image.size[0], image.size[1]))

    region = image.crop((200, 50, 800, 500))
    region.save(text_area_file)


def get_area_data(text_area_file):
    """

    :param text_area_file:
    :return:
    """
    with open(text_area_file, "rb") as fp:
        image_data = fp.read()
        return image_data
    return ""
