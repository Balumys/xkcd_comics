import requests
from pydantic import BaseModel, Field


class ResponseFromServer(BaseModel):
    server: int
    photo: str
    hash: str


class SavedComicToWall(BaseModel):
    owner_id: int
    media_id: int = Field(alias='id')

    def get_media_attachment(self):
        return f"photo{self.owner_id}_{self.media_id}"


def get_img_upload_url(token):
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    parameters = {"access_token": token,
                  "v": 5.131,
                  "group_id": 61264413}
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    if "error" in response.json():
        raise requests.exceptions.RequestException(response.json()["error"]["error_msg"])
    return response.json()["response"]["upload_url"]


def upload_comic_to_vk_server(token, img_path):
    with open(img_path, 'rb') as file:
        url = get_img_upload_url(token)
        files = {"photo": file}
        response = requests.post(url, files=files)
    response.raise_for_status()
    if response.json()["photo"] == "[]":
        raise requests.exceptions.RequestException("Photo wasn't upload, check photo parameters")
    return response.json()


def save_img_to_wall(token, server_response):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    parameters = {"access_token": token,
                  "v": 5.131,
                  "group_id": 61264413,
                  "server": server_response.server,
                  "hash": server_response.hash,
                  "photo": server_response.photo,
                  }
    response = requests.post(url, params=parameters)
    response.raise_for_status()
    saved_comic = response.json()
    if "error" in saved_comic:
        raise requests.exceptions.RequestException(response.json()["error"]["error_msg"])
    return saved_comic["response"][0]


def post_img_to_wall(token, img_title, attachment):
    url = "https://api.vk.com/method/wall.post"
    parameters = {"access_token": token,
                  "v": 5.131,
                  "owner_id": -219173167,
                  "from_group": 1,
                  "message": img_title,
                  "attachments": attachment}
    response = requests.post(url, params=parameters)
    response.raise_for_status()
    posted_comic = response.json()
    if "error" in posted_comic:
        raise requests.exceptions.RequestException(response.json()["error"]["error_msg"])
