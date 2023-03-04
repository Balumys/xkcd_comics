import requests


def get_img_upload_url(token):
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    parameters = {"access_token": token,
                  "v": 5.131,
                  "group_id": 61264413}

    response = requests.get(url, params=parameters)
    response.raise_for_status()
    return response.json()["response"]["upload_url"]


def upload_img_to_vk_server(token, img_path):
    with open(img_path, 'rb') as file:
        url = get_img_upload_url(token)
        files = {"photo": file}
        response = requests.post(url, files=files)
        response.raise_for_status()
    return response.json()


def upload_img_to_wall(token, response_from_server):
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    parameters = {"access_token": token,
                  "v": 5.131,
                  "group_id": 61264413,
                  "server": response_from_server["server"],
                  "hash": response_from_server["hash"],
                  "photo": response_from_server["photo"],
                  }
    response = requests.post(url, params=parameters)
    response.raise_for_status()
    return response


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
