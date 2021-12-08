import requests,bs4

def synonyms(word):
    url='https://www.wordhippo.com/what-is/another-word-for/{}.html'.format(word)

    request=requests.get(url)

    soup=bs4.BeautifulSoup(request.text,'html.parser')

    l=[]
    for i in range(5):
        try:
            l.append(soup.find_all('div',{'class':'wb'})[i].find('a').text)
        except:
            pass
    return l


if __name__ == '__main__':
    word=input('Enter a word here: ')
    synonyms(word)
    









