# xkcd_comics
xkcd_comics is a console script that allows you to download a random xkcd comic from [xkcd Python Comics](https://xkcd.com/353/)
and posted it into your VK community.

## How to install
### Pre-requests
1. You need to create your VK community first. [Small guide here](https://www.youtube.com/watch?v=hUFxulrSOq0)
2. Create standalone VK application and get API token [Guide](https://www.youtube.com/watch?v=ZMWlgHg73D4)


### Installation
Python3 should be already installed

You need **3** additional libraries: python-dotenv, pydantic, requests.

To install them use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```
Place API token in **.env** file and specify the programming languages you want to get information from.

```
VK_TOKEN==YourToken
```

## Usage
xkcd_comics contains 3 scripts **main.py**,**comics.py**,**vk.py** for fetching random comic and 
posted it to your community.

### main.py
Download and save a random comic from [xkcd Python Comics](https://xkcd.com/353/) to root directory.
Publish the comic to a VK community, and once it has been published, remove it from the root directory.

Example: 

```python3 main.py ```


### Additional files
#### comics.py
Contain functions and class to get data from [xkcd Python Comics](https://xkcd.com/353/)
#### vk.py
Contain functions and class to publish a comic to a VK community. 

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
