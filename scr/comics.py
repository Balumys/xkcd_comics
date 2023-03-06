import os
from urllib import parse

import requests
from pydantic import BaseModel, HttpUrl, Field


class Comic(BaseModel):
    img_url: HttpUrl = Field(alias="img")
    title: str
    description: str = Field(alias="alt")
    number: int = Field(alias="num")

    def get_img_extension(self):
        img_extension = os.path.splitext(parse.urlsplit(self.img_url,
                                                        allow_fragments=True)[2])[-1]
        return img_extension

    def save_comic(self):
        response = requests.get(self.img_url)
        response.raise_for_status()
        path_to_save = f"{self.title}{self.get_img_extension()}"
        with open(path_to_save, "wb") as image:
            image.write(response.content)

    def get_comic_path(self):
        return f"{self.title}{self.get_img_extension()}"


def get_last_comic_number():
    url = "https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_random_comics(number):
    url = f"https://xkcd.com/{number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
