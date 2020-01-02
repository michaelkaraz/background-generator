import requests
from bs4 import BeautifulSoup
from pprint import pp

def get_links_pages_for(numberOfPages):
    uri = ''
    hackerNews = []
    for page in range(numberOfPages):
        if(page == 0):
            uri = 'https://news.ycombinator.com/news'
        else:
            uri = f'https://news.ycombinator.com/news?p={page+1}'
        res = requests.get(uri)
        soup = BeautifulSoup(res.text,'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        hackerNews.extend(create_custom_hn(links,subtext))
    return sort_stories_by_votes(hackerNews)

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse = True)

def create_custom_hn(links,subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title':title, 'link':href,'votes':points})
    return hn
def main():
    pp(get_links_pages_for(10))
    
if __name__ == '__main__': main()
