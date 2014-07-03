
#TODO CLI interface
""" ffc url dir [-w | --watch [-t | --timer (=default 30s)]]"""
#TODO watch thread


import haul
import click
from urllib import urlretrieve

#TODO handling error (404)
def get_images(url):
    result = haul.find_images(url, extend=True)

    out = []

    for item in result.image_urls:
        if 'i.4cdn' in item:
            out.append(item[4:])
        else:
            pass
    return out


def download(img_url,filename,dr):
    img_url = 'http://i.'+img_url
    obj = dr+'/'+filename
    #print"downloading "+img_url
    urlretrieve(img_url,obj)

@click.command()
@click.option('--Watch',default = 0)
@click.argument('url')
@click.argument('dir')
def main(url,dir,Watch):
    img_list = get_images(url)
    for item in img_list:
        filename = item.split('/')[-1]
        download(item,filename,dir)

if __name__ == '__main__':
    main()
