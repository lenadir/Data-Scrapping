import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = ''


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table', {'id':'result-research'}).find('tbody').find_all('tr')

activity = []
for row in rows:
    dic = {}
    dic['activities'] = row.find_all('td')[1].text.replace('\n','').replace(' ','')
    dic['domain'] = row.find_all('td')[2].text.replace('\n','').replace(' ','')
    activity.append(dic)


df = pd.DataFrame(activity)
df.to_excel('activities.xlsx', index=False)