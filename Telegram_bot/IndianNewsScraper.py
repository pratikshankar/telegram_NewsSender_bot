import requests
from sys import getsizeof

india_news_url="https://newsapi.org/v2/top-headlines?country=in&apiKey=fc78addbfa644a59a060e7be12adf15a"
business_news_url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=fc78addbfa644a59a060e7be12adf15a"
health_news_url="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=fc78addbfa644a59a060e7be12adf15a"
def IndiaNews():

    news=requests.get(india_news_url).json()['articles']
    i=0;
    result=''
    for new in news:
        i+=1
        if i<=10:
            result+=str(i)+" "+new['title']+" "+new['url']+"\n"
    print(result)
    print("\n"+"\n")
    print(getsizeof(result))
    return(result)

def BusinessNews():
    news=requests.get(business_news_url).json()['articles']
    i=0;
    result=''
    for new in news:
        i+=1
        if i<=10:
            result+=str(i)+" "+new['title']+" "+new['url']+"\n"
    print(result)
    print("\n"+"\n")
    print(getsizeof(result))
    return(result)

def HealthNews():
    news=requests.get(health_news_url).json()['articles']
    i=0;
    result=''
    for new in news:
        i+=1
        if i<=10:
            result+=str(i)+" "+new['title']+" "+new['url']+"\n"
    print(result)
    print("\n"+"\n")
    print(getsizeof(result))
    return(result)
if __name__ == '__main__':
     
    # function call
    HealthNews()