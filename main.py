from flickr import get_urls
from downloader import download_images
import os
import time

all_species = ['blue jay', 'northern cardinal', 'american goldfinch']
images_per_species = 10

def download():
    for species in all_species:

        print('Getting urls for', species)
        urls = get_urls(species, images_per_species)

        print('Downlaing images for', species)
        path = os.path.join('data', species)
        
        download_images(urls, path)

if __name__=='__main__':

    start_time = time.time()

    download()

    print('Took', round(time.time() - start_time, 2), 'seconds')