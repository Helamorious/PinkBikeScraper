import lxml.html
import requests

url2019 = 'https://www.pinkbike.com/news/2019-photo-of-the-year-32-finalists-announced-and-round-1-voting-open.html'
url2018 = 'https://www.pinkbike.com/news/2018-photo-of-the-year-32-finalists-announced-and-round-1.html'
url2017 = 'https://www.pinkbike.com/news/2017-photo-of-the-year-32-finalists-announced-round-1-voting-open.html'
url2016 = 'https://www.pinkbike.com/news/2016-photo-of-the-year-10000-cash-prizing-round-1.html'
url2015 = 'https://www.pinkbike.com/news/2015-photo-of-the-year-round-1-trek-sram.html'

urlxpath = '//*[@id="blog-container"]/div[3]/div/div/div[*]/a/div/div/img/@src'

urls = [url2015, url2016, url2017, url2018, url2019]

for url in urls:
    page = requests.get(url)                            # Open the website
    tree = lxml.html.fromstring(page.content)           # Parse the website
    images = tree.xpath(urlxpath)                       # Scrape the website to get all the images

    for image in images:
        id = image.split('/')[-1].split('.')[0][4:]     # Identify the ID number from the image URLs
        imgurl = 'https://ep1.pinkbike.org/p0pb' + id + '/p0pb' + id + '.jpg' # Craft a new URL with p0pb to indicate original size
        imgfn = id + '.jpg'                             # Generate the filename
        print("Downloading: " + imgurl)                 # Debug data
        dl = requests.get(imgurl, allow_redirects=True) # Open the new image
        open(imgfn, 'wb').write(dl.content)             # Write the image out to file
