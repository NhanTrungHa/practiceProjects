#! python3
# linkVerification.py - Opens up website and downloads every linked page and checks if error.

import bs4
import requests

# TODO: Get URL of page.
url = 'https://automatetheboringstuff.com/'
print("Downloading page %s..." % url)

# TODO: Attempt to download the request of the page
res = requests.get(url)
res.raise_for_status()

# TODO: Go to given url and make list of every link
soup = bs4.BeautifulSoup(res.text, "html.parser")
links = soup.find_all("a")

# TODO: Check if 404 status code or errors
for link in links:
    res = requests.get(link)
    # TODO: If no error, continue. If error, print current url.
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if res.status_code == 404:
            print("Error with link %s" % link)
