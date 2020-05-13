from lxml import html
import requests as rq

page = rq.get('https://www.gutenberg.org/wiki/Gutenberg:Contact_Information')
print(page.content)
tree = html.fromstring(page.content)  # use XPath and CSSSelect.
# use http://www.w3schools.com/xml/xpath_intro.asp
print(tree)

# ============
page = rq.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)
# This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')
print(f'Buyers: {buyers}')
print(f'Prices: {prices}')
