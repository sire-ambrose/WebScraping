import requests
import bs4
import pandas as pd

def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
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
QUOTES, AUTHOR, TAGS, LIKES=[], [], [], []
###you can change the first url to the url of the quotes of your choice
### you can also change the max_page to change the amount of pages to scrape
max_page= 46
for i in range(1,max_page):
  url='https://www.goodreads.com/quotes/tag/christmas'
  url= f'{url}?page={i}'
  q,a,t,l= get(url)
  QUOTES.extend(q)
  AUTHOR.extend(a)
  TAGS.extend(t)
  LIKES.extend(l)


pd.DataFrame({'quote':QUOTES, 'author':AUTHOR, 'tags': TAGS, 'likes': LIKES}).to_csv('christmas_quotes.csv', index=False)
