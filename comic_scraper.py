from bs4 import BeautifulSoup
import requests, urllib.request

import time

start = time.time()

websites = {'Popeye':'https://www.comicskingdom.com/popeye',
            'Hagar the horrible':'https://www.comicskingdom.com/hagar-the-horrible',
            'Blondie':'https://www.comicskingdom.com/blondie',
            'Marvin':'https://www.comicskingdom.com/marvin',
            'Moose and Molly':'https://www.comicskingdom.com/moose-and-molly',
            'Beetle Bailey':'https://www.comicskingdom.com/beetle-bailey-1',
            'Tiger':'https://www.comicskingdom.com/tiger'}

for key in list(websites.keys()):
    source = requests.get(websites[key]).text
    soup = BeautifulSoup(source, 'lxml')
    image = soup.find('slider-image')['image-url']

    #r = requests.get(image)#Throws an SSL:certificate verify failed error, don't know how to fix it
    #Use urllib library to open the page and read the contents, somehow this doesn't throw the verification error
    r = urllib.request.urlopen(image)

    with open('{}.png'.format(key), 'wb') as f:
        #f.write(r.content)
        f.write(r.read())
    print(key)

websites2 = {'Calvin and Hobbes':'https://www.gocomics.com/calvinandhobbes',
             'Peanuts':'https://www.gocomics.com/peanuts',
             'Pooch cafe':'https://www.gocomics.com/poochcafe',
             'Pearls before swine':'https://www.gocomics.com/pearlsbeforeswine',
             'Garfield':'https://www.gocomics.com/garfield',
             'Wumo':'https://www.gocomics.com/wumo'}

for key in list(websites2.keys()):
    source = requests.get(websites2[key]).text
    soup = BeautifulSoup(source, 'lxml')
    image = soup.find('div', class_ = "row").picture.img['data-srcset']
    image = image.split(' ')[0]

    r = requests.get(image)

    with open('{}.png'.format(key), 'wb') as f:
        f.write(r.content)
    print(key)

##The wumo website's a little shady, ads and stuff. Takes too long to load, something's wrong with the site.
##wumo = requests.get('http://wumo.com/wumo').text
##soup = BeautifulSoup(wumo, 'lxml')
##image = soup.find('div', class_ = "main-container").img['src']
##r = requests.get('https://wumo.com{}'.format(image))#image above gives everything but 'https://wumo.com'
##with open('WuMo.png', 'wb') as f:
##    f.write(r.content)
##print("Wumo")

dilbert = requests.get('https://dilbert.com').text
soup = BeautifulSoup(dilbert, 'lxml')
image = soup.find('div', class_ = "img-comic-container").img['src']
r = requests.get(image)#later edit: it now gives https:
#r = requests.get('https:{}'.format(image))#image above gives everything but 'https:'
with open('Dilbert.png', 'wb') as f:
    f.write(r.content)
print("Dilbert")

xkcd = requests.get('https://xkcd.com').text
soup = BeautifulSoup(xkcd, 'lxml')
image = soup.find('div', id = "comic").img
r = requests.get('https:{}'.format(image['src']))
with open('xkcd.png', 'wb') as f:
    f.write(r.content)
print(image['alt'])
print(image['title'])

end = time.time()
print(end-start)
input("My work here is done")#so it doesn't close immediately
