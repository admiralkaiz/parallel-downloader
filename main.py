import requests 
import threading 
import time

download_list = [
    {'url': 'http://google.com/favicon.ico', 'filename': 'googlefacivon.ico'},
    {'url': 'http://facebook.com/favicon.ico', 'filename': 'facebookfacivon.ico'},
    {'url': 'http://youtube.com/favicon.ico', 'filename': 'youtubefacivon.ico'},
]

class Downloader(threading.Thread):
    def __init__(self, url, filename):
        threading.Thread.__init__(self)
        self.url = url
        self.filename = filename 

    def run(self):
        r = requests.get(self.url, allow_redirects=True)
        open(self.filename, 'wb').write(r.content)

def download_multiple_files():
    workers = []
    for download in download_list:
        worker = Downloader(download['url'], download['filename'])
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

if __name__ == '__main__':
    download_multiple_files()
