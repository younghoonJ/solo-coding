from collections import namedtuple
import os
from multiprocessing import Pool, cpu_count
from urllib.request import urlopen, urlretrieve
import abc


def download_file(url_path):
    url, path = url_path
    try:
        print('Download from ', url)
        urlretrieve(url, path)
    except Exception as e:
        print('Terminate child process. ', e)


file_info = namedtuple('file_info', 'url file_name')


class UrlDownloader:
    def __init__(self, file_info, to_dir, n_workers=None):
        self.file_info = file_info
        self.to_dir = to_dir
        self.n_workers = n_workers

    def download_files(self):
        if not os.path.isdir(self.to_dir):
            os.makedirs(self.to_dir)
        targets = [(i.url, f'{self.to_dir}/{i.file_name}')
                   for i in self.file_info]
        if self.n_workers is None:
            self.n_workers = cpu_count()
        try:
            with Pool(processes=self.n_workers) as p:
                it = p.imap(download_file, targets)
                for _ in it:
                    pass
        except Exception as e:
            print('Exception occures.',  e)
