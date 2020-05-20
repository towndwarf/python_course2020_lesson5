import pandas as pd
import requests as rq
from bs4 import BeautifulSoup


def trim_quotes_if_required(book_name: str) -> str:
    if book_name.find(',') < 0:
        book_name = book_name.strip('"')

    ret = book_name.strip('\',\r\n \xa0£')
    if ret.find(',') > 0:
        ret = f'\"{ret}"'
    return ret


def get_data(page_no: str):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    url = 'https://www.waterstones.com/books/bestsellers/sort/bestselling/page/'
    r = rq.get(url + page_no, headers=headers)  # , proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')  # , 'features="lxml"'
    print(soup)
    print(soup.prettify())

    alls = []

    for d in soup.findAll('div',
                          attrs={'class': 'book-preview book-preview-grid-item span3 tablet-span6 mobile-span6'}):
        # print(d)

        # treat NAME
        name = d.find('a', attrs={'class': 'title link-invert dotdotdot'})
        name_is_not_ok = True
        if name is not None:
            name = name.text
            if name.endswith("..."):
                print('NAME was truncated', name)
            else:
                name_is_not_ok = False
                print('NAME was scraped:', name)
        else:
            print('NAME was not OK, taking from image')

        if name_is_not_ok:
            # taking name from image
            n = d.find('img', alt=True)
            if n and len(n.attrs):
                name = n.attrs['alt']
                print('Name from image: ', n.attrs['alt'])
        all1 = []
        if type(name) is str and len(name) > 0:
            # print(n[0]['alt'])
            all1.append(trim_quotes_if_required(name))
        else:
            all1.append("can`t get author")

        author = d.find('span', attrs={'class': 'author'})
        rating = d.find('span', attrs={'class': 'star-rating'})
        price = d.find('span', attrs={'class': 'price'})

        if author is not None:
            # print(author.text)
            all1.append(trim_quotes_if_required(author.text))
        elif author is None:
            author = d.find('span', attrs={'class': 'a-size-small a-color-base'})
            if author is not None:
                all1.append(trim_quotes_if_required(author.text))
            else:
                all1.append('0')

        if rating is not None:
            # print(rating.text)
            all1.append(rating.text)
        else:
            all1.append('-1')

        if price is not None:
            print('PRICE:', price.text)
            all1.append(trim_quotes_if_required(price.text))
        else:
            all1.append('0')
        alls.append(all1)
    return alls


writable_lines = [','.join(['Book Name', 'Author', 'Rating', 'Price']) + "\n"]

no_pages = 2
for i in range(1, no_pages + 1):
    st = get_data(str(i))
    for j in st:
        writable_lines.append(','.join(j) + "\n")

handle = open("books.csv", mode="w", encoding="utf-8")
handle.writelines(writable_lines)
handle.close()

# to read csv file named "books.csv"
a = pd.read_csv("books.csv")

# to save as html file named "Table"
s = a.to_html("Table.htm")

# assign it to a variable (string)
html_file = a.to_html()

print('everything is awesome')
# df = pd.read_csv("books.csv")
# df.shape
# df.head(61)
