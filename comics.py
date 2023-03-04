import requests
import os
from urllib import parse


def get_last_comic_number():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    response_json = response.json()
    return response_json["num"]


def get_img_extension(url):
    img_extension = os.path.splitext(parse.urlsplit(url, allow_fragments=True)[2])[-1]
    return img_extension


def save_img(url, path_to_img):
    response = requests.get(url)
    response.raise_for_status()
    with open(path_to_img, "wb") as image:
        image.write(response.content)


def fetch_random_comics(number):
    url = f"https://xkcd.com/{number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
