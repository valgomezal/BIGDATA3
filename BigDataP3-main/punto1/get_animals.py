from bs4 import BeautifulSoup
def get_animals(f2):
    soup = BeautifulSoup(f2.read(), 'html.parser')
    images = soup.find_all("img")
    return images
