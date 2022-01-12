import requests
import bs4
import pandas as pd



def listToString(s): 
    str1 = " " 

    return (str1.join(s))
        



def get(category):
    
    url= f'https://www.tesco.com/groceries/en-GB/shop/{category}/all?include-children=true'
    headers = {'User-Agent': 'Mozilla/5.0'}
    request_result=requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    products=soup.find_all('div',{'class':'tile-content'})
    
    Name, Total_Price, Unit_Price=[],[], []
    for prod in products:
        name=prod.find('a',{'class':'ui__StyledLink-sc-18aswmp-0 eYySMn'}).text
        try:
            total_price=prod.find('div',{'class':'price-control-wrapper'}).find('span',{'data-auto':'price-value', 'class':'value'}).text
            per_unit_price= prod.find('div',{'class':'price-per-quantity-weight'}).find('span',{'data-auto':'price-value', 'class':'value'}).text
        except:
            total_price=None
            per_unit_price= None
        Name.append(name)
        Total_Price.append(total_price)
        Unit_Price.append(per_unit_price)
    df={'name':Name, 'Total Price':total_price, 'Unit Price': Unit_Price}
    df=pd.DataFrame(df)
    return df


# scraping drinks products       
bakery=get('bakery')

print(bakery)

print('\n\n')

#scraping bakery products
drinks=get('drinks')

print(drinks)
