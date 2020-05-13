import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
'''
url_2 = f'https://www.giropharm.fr/trouver-ma-pharmacie/resultats/resultat/dpt-75-paris/9.html?giropharm=0'
# you can see that the url 2 have '/9' => one page contains 9 pharma info i need to find a way to do a for loop to get
# all the all_page for all the pages
url = 'https://www.giropharm.fr/trouver-ma-pharmacie/resultats/resultat/dpt-75-paris.html?giropharm=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
bloc = soup.find(class_='pharmacie_bloc_resultat contenu_vert_clair')

all_page = bloc.get_text()

print(all_page)
stuff = pd.DataFrame({
})
'''
url_base = 'https://www.giropharm.fr/trouver-ma-pharmacie/resultats/resultat/dpt-75-paris'
url_suffix = '.html?giropharm=0'


for i in range(0, 28, 9):
    url_ins = ''
    if i > 1:
        url_ins = f'/{i - 1}'
    url = url_base + url_ins + url_suffix
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    bloc = soup.find(class_='pharmacie_bloc_resultat contenu_vert_clair')
    all_page = bloc.get_text()
    print(all_page)
