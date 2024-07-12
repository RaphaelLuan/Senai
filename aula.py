from bs4 import BeautifulSoup
import requests

url = 'https://playful-cendol-eb7d4c.netlify.app/'

requisicao = requests.get(url)
soup = BeautifulSoup(requisicao.text, 'html.parser')
dado = soup.find('table')
x = soup.find_all('tr')
lista = []
lista += (x)
for n in lista:
    print(n.get_text())

if '@' in n:

# texto = soup.find('p')
# tabela = soup.find('table')
# array = []
# if tabela:
#     table_head = soup.find('table').get_text()
#     array.append(table_head)

# print(lista)
