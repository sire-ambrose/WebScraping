import requests
import bs4
import time
import pandas as pd
url = 'https://www.vidal.fr/medicaments/gammes/liste-0-9.html'

def get_alpha_link(link):
  alpha_link=[]
  alpha_request=requests.get( link )
  soup = bs4.BeautifulSoup(alpha_request.text, "html.parser")
  
  for children in soup.findChildren('div',{'class':'list'}):
    for child in children.find_all('a'):
      alpha_link.append('https://www.vidal.fr/'+child['href'])
  return alpha_link

def last_link(link):
  request=requests.get( i )
  soup = bs4.BeautifulSoup(request.text, "html.parser")
  links=[]
  for children in soup.findChildren('div',{'class':'products'}):
    for child in children.find_all('a',{'class':""}):
      links.append('https://www.vidal.fr/'+child['href'])
  return links

def name_cip(j):
  request=requests.get( j )
  soup = bs4.BeautifulSoup(request.text, "html.parser")
  for children in soup.findChildren('div',{'class':'description'}):
    try:
      name=children.find(class_="name").text
    except:
      name= None

    try:
      cip=children.find(class_="cip13").text
    except:
      cip= ''


  return name, cip
# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
request_result=requests.get( url )
  
# Creating soup from the fetched request
soup = bs4.BeautifulSoup(request_result.text, "html.parser")
links=[]
lst=soup.find_all( 'a' )


alphabets= ['a', 'b', 'c', 'd']
for info in lst:
    if info.getText() in alphabets:
        link= 'https://www.vidal.fr/'+info['href']
        links.append(link)

NAME, CIP= [], []

g= 0

for link in links:
  alpha_link= get_alpha_link(link)
  for i in alpha_link:
    last=last_link(i)
    for j in last:
      name, cip= name_cip(j)
      print('name: ', name, '     ','cip: ', cip)
      NAME.append(name)
      CIP.append(cip)

  pd.DataFrame({'name': NAME, 'CIP':CIP}).to_excel('product_A.xlsx', index= False)
  print('\n\n\ndone')
  break
          

pd.DataFrame({'name': NAME, 'CIP':CIP}).to_excel('products.xlsx', index= False)
#print()


#print(soup)
