#! python3
# download_C&H.py - Downloads every single XKCD comic.

import requests
import os
import bs4

url = 'http://explosm.net'  # starting url

os.makedirs('c_and_h', exist_ok=True)  # store comics in ./c_and_h

while not url.endswith('kapplesauce'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features="lxml")

    # Find the URL of the comic image.
    comicElem = soup.select('#comic-short img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status(
        )

    # TODO: Save the image to ./xkcd.
    imageFile = open(os.path.join('c_and_h', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
        imageFile.close()

    # TODO: Get the Prev button's url.
    prevLink = soup.select('Right')
    url = 'https://explosm.net' + prevLink.index(0)

print('Done.')
