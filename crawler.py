import urllib.request
from bs4 import BeautifulSoup
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.tripadvisor.com/Hotels-g60893-Richmond_Virginia-Hotels.html'
# customized url

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

# print(soup.find('div', {'class': 'ProfileHeaderCard'}).find('p').text)
# for link in soup.findAll('a'):
#     print(link.get('href'))

for pics in soup.findAll('div', {'class': 'inner'}):
    print(pics)
