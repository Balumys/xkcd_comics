import os
import sys
import requests
from dotenv import load_dotenv
import random
from comics import get_last_comic_number, fetch_random_comics, Comic
from vk import upload_comic_to_vk_server, save_img_to_wall, post_img_to_wall, \
    ResponseFromServer, SavedComicToWall

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("VK_TOKEN")
    try:
        last_comic = Comic(**get_last_comic_number())
        random_comic_number = random.randint(0, last_comic.number)
        random_comic = Comic(**fetch_random_comics(random_comic_number))
        random_comic.save_comic()
    except requests.exceptions.HTTPError as err:
        sys.exit(err)

    try:
        server_response = ResponseFromServer(**upload_comic_to_vk_server(token, random_comic.get_comic_path()))
        saved_comic_to_wall = SavedComicToWall(**save_img_to_wall(token, server_response))
        post_img_to_wall(token, random_comic.title, saved_comic_to_wall.get_media_attachment())
    except requests.exceptions.RequestException as err:
        sys.exit(err)
    finally:
        os.remove(random_comic.get_comic_path())

