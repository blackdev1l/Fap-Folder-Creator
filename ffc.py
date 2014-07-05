""" ffc url dir [-w | --watch [-t | --timer (=default 30s)]]"""
#TODO CLI interface
#TODO watch thread
#TODO handling error (404)
#TODO GUI
#TODO mkdir

"""
    errors:
            1. Url is not from 4chan.org
            2. Dir is illegal
            3. Thread is 404
"""

import contextlib
import json
from urllib import urlretrieve
import urllib2
import haul
from time import sleep


def watch_thread(time,url,dr):
    urljson = url_to_json(url)

    with contextlib.closing(urllib2.urlopen(urljson)) as j:
        j_obj = json.load(j)

    img_number = j_obj["posts"][0]["images"]

    while True:
        sleep(time)
        try:
            with contextlib.closing(urllib2.urlopen(urljson)) as j:
                j_obj = json.load(j)
        except urllib2.HTTPError:
            print("Thread went 404\n Total image downloaded: " + str(img_number+1))
            exit(3)
        else:
            new_img_number = j_obj["posts"][0]["images"]
            if img_number != new_img_number:
                new_list = get_images(url)
                filename = new_list[-1].split('/')[-1]
                download(new_list[-1],filename,dr)
                img_number = new_img_number
            else:
                pass
    return True


def get_images(url):
    result = haul.find_images(url, extend=True)

    out = []

    for item in result.image_urls:
        if 'i.4cdn' in item:
            out.append(item[4:])
        else:
            pass
    return out

def url_to_json(url):
    return 'http://a.4cdn.org/'+url[24:]+'.json'

def download(img_url,filename,dr):
    img_url = 'http://i.'+img_url
    obj = dr+'/'+filename
    print("downloading "+img_url)
    urlretrieve(img_url,obj)

def main():
    time = 10
    url = raw_input("url: ")

    if 'boards.4chan.org/' in url:
        pass
    else:
        exit(1)
    dir = raw_input("dir: ")
    urljson = url_to_json(url)

    try:
        with contextlib.closing(urllib2.urlopen(urljson)) as j:
            j_obj = json.load(j)
    except urllib2.HTTPError:
        print("Thread is 404")
        exit(3)

    img_list = get_images(url)
    for item in img_list:
        filename = item.split('/')[-1]
        download(item,filename,dir)

    print("Watching Thread....")
    watch_thread(time,url,dir)

if __name__ == '__main__':
    main()
