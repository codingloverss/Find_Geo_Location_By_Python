import requests
from bs4 import BeautifulSoup
def Geo_Location():
    page=requests.get("https://ipinfodb.com/").text
    soup=BeautifulSoup(page,'html.parser')
    data=soup.find('table',{'class':'table'})
    result=[]
    for rows in data.find_all('tr'):
        cols=rows.find_all('td')
        if len(cols)>=2:
            try: 
                result.append([cols[0].text,cols[1].text,cols[2].text])
            except:
                result.append([cols[0].text,cols[1].text])
    address={}
    ip=soup.find('h1',{'class':'pull-left'}).strong.text.split('-')
    address[ip[0].strip()]=ip[1].strip()
    for k in range(len(result)):
        for i in result[k]:
            address[i.split('\n')[1]]=i.split('\n')[2]
    return address
if __name__ == "__main__":
    print(Geo_Location())
