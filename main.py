import os
from dotenv import load_dotenv
import random
from comics import get_last_comic_number, fetch_random_comics, get_img_extension, save_img
from vk import upload_img_to_vk_server, upload_img_to_wall, post_img_to_wall

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("VK_TOKEN")
    random_comic_number = random.randint(0, get_last_comic_number())
    xkcd_response = fetch_random_comics(random_comic_number)
    img_url, img_name, img_title = xkcd_response["img"], xkcd_response["title"], xkcd_response["alt"]
    img_path = f"{img_name}{get_img_extension(img_url)}"
    save_img(img_url, img_path)
    response_from_server = upload_img_to_vk_server(token, img_path)
    img_object = upload_img_to_wall(token, response_from_server).json()
    photo_id = img_object["response"][0]["id"]
    photo_owner_id = img_object["response"][0]["owner_id"]
    attachment = f"photo{photo_owner_id}_{photo_id}"
    post_img_to_wall(token, img_title, attachment)
    try:
        os.remove(img_path)
    except OSError:
        pass
