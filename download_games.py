from helpers.url_extractor import UrlExtractor
from helpers.downloader import UrlDownloader
from collections import namedtuple
import os


file_info = namedtuple('file_info', 'url file_name num_games')


if __name__ == "__main__":
    extractor = UrlExtractor(web_url='http://u-go.net/gamerecords/')
    extractor.get_from_web()
    urls = extractor.extract('https://', '-.zip')
    print(len(urls))
    fi = []
    for u in urls:
        fname = os.path.basename(u)
        split_fname = fname.split('-')
        num_games = int(split_fname[len(split_fname) - 2])
        fi.append(file_info(u, fname, num_games))

    d = UrlDownloader(fi, '/data')
    with d:
        d.download_files()
    
    

