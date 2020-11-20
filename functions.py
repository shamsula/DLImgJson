import os
import urllib.request
from urllib.parse import urlparse
import json


def download_img(url, dest):
    filename = url.split('/')[-1]
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7')]
    urllib.request.install_opener(opener)
    if not os.path.exists("img"):
        os.makedirs("img")
    basename = os.path.basename(urlparse(filename).path)
    if ".jpg" in basename or ".png" in basename:
        urllib.request.urlretrieve(url, dest + "/" + basename)


def process_list(li):
    for item in li:
        download_img(item, 'img')


# Check Bo Sunesen @
# https://stackoverflow.com/questions/21028979/recursive-iteration-through-nested-json-for-specific-key-in-python
def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if lookup_key in k and not isinstance(v, dict):
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)


def process_json(filename):
    try:
        with open(filename) as j:
            data = json.load(j)
            url_list = []
            for url in item_generator(data, "url"):
                if isinstance(url, list):
                    for it in url:
                        url_list.append(it)
                else:
                    url_list.append(url)

            process_list(url_list)
            print("Done. Find files in img/")
    except OSError:
        print("Couldn't find file named data.json in res folder. \nExiting.")
