import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def my_download(file_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(file_name, "wb") as f:
        f.write(img_content)

def main():
    gevent.joinall([
            gevent.spawn(my_download, '1.jpg', 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/04/07/3559600_20190407203557_small.jpg'),
            gevent.spawn(my_download, '2.jpg', 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/04/13/278227_20190413171449_small.jpg')
        ])

if __name__ == "__main__":
    main()