#! python3
# imageDownloader.py - Downloads 10 images from a given search on imgur

import requests, os, bs4, sys

os.chdir('D:\Python\practiceProjects')
os.makedirs('imgur', exist_ok=True)
# TODO: Download the page.
url = 'https://imgur.com/search?q=' + ' '.join(sys.argv[1:])
res = requests.get(url)
res.raise_for_status()
print("Downloading page %s..." % url)
soup = bs4.BeautifulSoup(res.text, "html.parser")
# TODO: Find the URL of the image.
imageElem = soup.find_all("img")
if not imageElem:
    print("No results")
else:
    for link in imageElem:
        imageUrl = "https:" + link.get('src')
        print("Downloading image at.... " + imageUrl)
        res = requests.get(imageUrl)
        res.raise_for_status()
        # TODO: Save Image.
        imageFile = open(os.path.join('imgur', os.path.basename(imageUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
            imageFile.close()
    print("Program complete!")

