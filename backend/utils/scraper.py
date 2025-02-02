from bs4 import BeautifulSoup
import requests

def request_site(url : str) -> str:
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    content = soup.find('div', Class='_qcjzh6')
    print(f"the content:{content}")
    return content

def main():
    url = 'https://cplusplus.com/reference/stl/'
    url_2 = 'https://www.khanacademy.org/math/statistics-probability/probability-library'
    request_site(url_2)


if __name__ == '__main__':
    main()