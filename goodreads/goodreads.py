import requests
import bs4
import pandas as pd

def listToString(s): 
    str1 = " " 

    return (str1.join(s))
        


def get(url):
  request_result=requests.get( url )
  soup = bs4.BeautifulSoup(request_result.text, "html.parser")
  lst=soup.find_all('div',{'class':'quote'})

  Quotes, Author, Tags, Likes=[], [], [] ,[]

  for info in lst:
    tags= []
    print()
    for i in info.findChildren('div',{'class':'greyText smallText left'}):
      for tag in i.find_all('a'):
        tags.append(tag.text)
    tags= listToString(tags)
    quote=info.find('div',{'class':'quoteText'}).text
    quote=quote[ quote.index('“')+1 : quote.index('”') ]
    author= info.find('span',{'class':'authorOrTitle'}).text.strip().replace(',', '')
    likes= info.find('a',{'class':'smallText'}).text[:-5].strip()

    Quotes.append(quote)
    Author.append(author)
    Tags.append(tags)
    Likes.append(likes)

    print('\nquote: ', quote, '\nauthor: ', author, '\ntags: ', tags ,'\nlikes: ', likes, '\n')

  return Quotes, Author, Tags, Likes



def get_all():
  url= input('enter goodread url: ')
  max_page= int(input('number of pages: '))
  file_name= url[url.rfind('.')+1:]
  QUOTES, AUTHOR, TAGS, LIKES=[], [], [], []
  
  for i in range(1,max_page):
    url_= f'{url}?page={i}'
    q,a,t,l= get(url_)
    QUOTES.extend(q)
    AUTHOR.extend(a)
    TAGS.extend(t)
    LIKES.extend(l)

  pd.DataFrame({'quote':QUOTES, 'author':AUTHOR, 'tags': TAGS, 'likes': LIKES}).to_csv(file_name+'.csv', index=False)

  print('.............................................\nDone\n')



get_all()

