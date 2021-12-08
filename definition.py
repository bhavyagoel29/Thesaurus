import requests,bs4

def definition(word):
    url='https://www.wordhippo.com/what-is/the-meaning-of-the-word/{}.html'.format(word)

    request=requests.get(url)

    soup=bs4.BeautifulSoup(request.text,'html.parser')

    ans=soup.find_all('ol',{'class':'topleveldefinition'})[0].find('li').text
    return ans

if __name__ =='__main__':
    word=input('Enter a word here: ')
    definition(word)