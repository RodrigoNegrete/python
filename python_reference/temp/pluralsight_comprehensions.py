import urllib
import requests
from bs4 import BeautifulSoup

url = "http://sitl.diputados.gob.mx/LXIV_leg/iniciativas_con_cclxiv.php?filit=%20&pert=0&edot=P&comt=0"

request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')
table_data = soup.find_all('td')

# for row in table_data:
#     data = row.find_all('a')
#     rows = [i.text.strip() for i in data]
#     print(rows)

for row in table_data:
    data_a = row.find_all('a')
    rows_a = [i_a.text.strip() for i_a in data_a]
    data_b = row.find_all('b')
    rows_b = [i_b.text.strip() for i_b in data_b]
    data_span = row.find_all('span')
    rows_span = [i_span.text.strip() for i_span in data_span]
    print(rows_a, rows_b, rows_span)
