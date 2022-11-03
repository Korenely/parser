import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = 'https://home-club.com.ua'
URL = urljoin(BASE_URL, 'ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE')


def main():
    page = requests.get(URL).content
    soup = BeautifulSoup(page, 'html.parser')

    elementsList = soup.select('.additional-details > div > span.value')
    vendorCode, deliveryAvailability, deliveryAvailabilityPoland, deliveryDate, availabilityLviv = [el.text for el in elementsList]
    
    with open('data.txt' , 'w', encoding='utf-8') as file:
        file.write(f'{vendorCode}\n{deliveryAvailability.strip()}\n{deliveryAvailabilityPoland.strip()}\n{availabilityLviv.strip()}')
        


if __name__ == '__main__':
    main()
