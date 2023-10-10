from bs4 import BeautifulSoup
import requests
def get_article():
    try:
        source = requests.get("https://www.python.org/")
        source.raise_for_status()
        soup = BeautifulSoup(source.text,'html.parser')
        news = soup.find('div',class_="shrubbery").find_all('li')
        latest_article=[]
        for x in news:
            article = x.find('a').text
            latest_article.append(article)
        return latest_article

    except Exception as e:
        print(e)

if __name__ == "__main__":
    python_articles= get_article()

    if python_articles:
        print('latest article in the python selection')
        for index,article in enumerate(python_articles,1):
            print(f"{index}. {article}")