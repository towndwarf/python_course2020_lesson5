import requests
import lxml
from bs4 import BeautifulSoup
#
import time

__doc__

# source : http://example.webscraping.com/
# learned in youtube video
'''
example: 
        soup = BeautifulSoup(response.text, 'lxml') 
        title = soup.find('title') => find the element and whats in
        print(title) => give the <title>blablabla</title>
        print(title.text) => give only the content of html element
        tds = soup.findAll('td') => give all the td 
        print(len(tds)) => give the number of td element in the html file
        print()
        print()

        title.findAll => 
'''

# <td>
#   <div>
#       <a href="/places/default/view/Antigua-and-Barbuda-10">
#       <img src="/places/static/images/flags/ag.png"/>Antigua and Barbuda</a>
#   </div>
# </td>

links = []
for i in range(26):
    url = 'http://example.webscraping.com/places/default/index/' + str(i)
    response = requests.get(url)
    print(response)
    if response.ok:
        print('Page:' + str(i))
        soup = BeautifulSoup(response.text, 'lxml')
        tds = soup.findAll('td')
        for td in tds:
            a = td.find('a')
            link = a['href']
            links.append('http://example.webscraping.com' + link)
        time.sleep(2)
print(len(links))
with open('urls.txt', 'w') as file:
    for link in links:
        file.write(link + "\n")
with open('urls.txt', 'r') as file:
    for row in file:
        print(row)


url = 'http://example.webscraping.com/places/default/view/Israel-108'