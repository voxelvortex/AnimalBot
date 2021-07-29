import requests

BASE_URL = "https://cataas.com"
URL_DATA = {"photo":"/cat",
            "gif":"/cat/gif",
            "text":"/cat/says/{0}"}
APPENDS = {"html":"?html=true"}


def get_photo(url, html=False):
    if html:
        req = requests.get( url + APPENDS["html"] )
    else:
        req = requests.get(url)

    if req.status_code != 200:
        raise Exception("Got an unexpected error when trying "+
                        "to get an image:\n{0}".format(req.status_code))
    return req.raw


def get_cat():
    file = get_photo(BASE_URL + URL_DATA["photo"])
    return file

def get_cat_gif():
    file = get_photo(BASE_URL + URL_DATA["gif"])
    return file

def get_cat_text():
    file = get_photo(BASE_URL + URL_DATA["text"])
    return file
