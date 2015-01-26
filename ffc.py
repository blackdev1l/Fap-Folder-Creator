#!/usr/bin/python2.7
""" ffc url dir [-w | --watch [-t | --timer (=default 30s)]]"""
#TODO GUI


"""
    errors:
            1. Url is not from 4chan.org
            2. Dir is illegal
            3. Thread is 404
"""

import sys
import contextlib
import json
from urllib import urlretrieve
import urllib2
import haul
from time import sleep
import argparse
import os.path


def watch_thread(time,url,dr):
    print("Watching...")
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

def check_dir(dir):
    # Check whether directory exists and create one 
    if not os.path.isdir(dir):
        print("Destination path ({0}) doesn't exist!".format(dir))
        print("Create folder? [y/n] ")
        req = raw_input()
        if req is 'y':
            os.mkdir(dir)
        else:
            sys.exit(2)
    # Check permission
    if not os.access(dir, os.R_OK):
        print("Destination path {0} is not readable! (Check permissions)".format(dir))
        sys.exit(2)
    elif not os.access(dir, os.W_OK):
        print("Destination path {0} is not writeable! (Check permissions)".format(dir))
        sys.exit(2)

def download(img_url,filename,dr):
    img_url = 'http://i.'+img_url
    obj = dr+'/'+filename
    print("downloading "+img_url)
    urlretrieve(img_url,obj)

def main(url,dir,time):


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

    # OS check, if Windows you can doubleclick the script and it will work
    if sys.platform.startswith('linux'):
        parser = argparse.ArgumentParser(description='Image downloader for 4chan\'s threads with auto watch thread')
        parser.add_argument('url', metavar='URL', type=str,
                            help='Thread\'s URL')
        parser.add_argument('dir', metavar='DIR', type=str,
                            help='Directory where to download the images')
        parser.add_argument('-t', '--timer', metavar='SEC',type=int, default='10', required=False,
                            help='Seconds of pause between a check to thread and another while is in Watch Thread mode')
        parser.add_argument('--version', action='version', version='%(prog)s 0.3')
        args = parser.parse_args()

        check_dir(args.dir)

        main(args.url, args.dir, args.timer)
    else:
        url = raw_input('url: ')
        dir = raw_input('dir: ')
        timer = 10

        check_dir(dir)
        main(url,dir,timer)

