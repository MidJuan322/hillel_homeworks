import requests
from bs4 import BeautifulSoup
import csv

FILE = 'data.csv'

# Получаем html
def get_html(url):
    r = requests.get(url)
    return r.text

# Записываем в .csv формат
def csv_read(data, path):
    with open(path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'ВК', 'ИНСТАГРАМ', 'ЮУТБ', 'ФЕЙСБУК', 'ТВИТЕР', 'ОДНОКЛАССНИКИ', 'ТЕЛЕГРАМ'])
        for item in data:
            writer.writerow([item['name'], item['vk'], item['inst'], item['youtube'], item['facebook'], item['twitter'],
                             item['ok'], item['telegram']])

# Получаем ссылки со страницы, для перехода по ним
def links(html):
    link = []
    soup = BeautifulSoup(html, 'lxml')
    link_block = soup.find_all('div', class_='channel-item')
    for a in link_block:
        link.append('https://zen.yandex.ru' + a.find('a').get('href'))
    return link

# Получаем данные из полученых ссылок
def content(html):
    contents = []
    soup = BeautifulSoup(html, 'lxml')
    info = soup.find('div', class_='channel-header-view-desktop__logo-line')
    info1 = soup.find_all('li', class_='social-links-view__button')
    for inform in info1:
        if inform.find('span', class_='zen-ui-button__content-wrapper').text == 'Youtube':
            youtube = inform.find('a').get('href')
        else:
            youtube = '-'
        if inform.find('span', class_='zen-ui-button__content-wrapper').text == 'Facebook':
            facebook = inform.find('a').get('href')
        else:
            facebook = '-'
        if inform.find('span', class_='zen-ui-button__content-wrapper').text == 'Twitter':
            twitter = inform.find('a').get('href')
        else:
            twitter = '-'
        if inform.find('span', class_='zen-ui-button__content-wrapper').text == 'OK':
            ok = inform.find('a').get('href')
        else:
            ok = '-'
        if inform.find('span', class_='zen-ui-button__content-wrapper').text == 'Telegram':
            telegram = inform.find('a').get('href')
        else:
            telegram = '-'
        if inform.find('span', class_='zen-ui-button__content-wrapper').text == 'VK':
            vk = inform.find('a').get('href')
        else:
            vk = '-'
        if inform.find('span', class_='zen-ui-button__content-wrapper').text == "Instagram":
            inst = inform.find('a').get('href')
        else:
            inst = '-'
        contents.append({
        "vk": vk,
        "inst": inst,
        'youtube': youtube,
        'facebook': facebook,
        'twitter': twitter,
        'ok': ok,
        'telegram': telegram,
        "name": info.find('span', class_='source-page-title-view__text _platform_desktop').text
    })
    return contents

# Делаем парсер многостраничным и объеденяем функционал функций выше
def main():
    info = []
    url = 'https://zen.yandex.ru/media/zen/channels'
    page_part = "?page="
    for i in range(1, 2, 1):
        url_gen = url + page_part + str(i)
        a = links(get_html(url_gen))
        print('Обрабыватываю ссылку №' + str(i) + ' ' + url_gen)
        print(links(get_html(url_gen)))
        for b in a:
            html = content(get_html(b))
            info.extend(html)
    csv_read(info, FILE)

if __name__ == '__main__':
    main()
