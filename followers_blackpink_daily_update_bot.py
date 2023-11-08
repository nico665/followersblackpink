from bs4 import BeautifulSoup
import requests
import schedule


def bot_send_text(bot_message):
    
    bot_token = '6839151829:AAHVlnILAZmPZrZBp4tf9D-5Me5xXYnP490'
    bot_chatID = '5512330690'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def jennieinsta_scraping():
    url = requests.get('https://www.instagram.com/jennierubyjane/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('span', {'class': 'html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs'})
    format_result = result.text

    return format_result


def report():
    seguidores_Jennie = f'Seguidores en Instagram {jennieinsta_scraping()}'
    bot_send_text(seguidores_Jennie)


if __name__ == '__main__':
        
    schedule.every().day.at("12:34").do(report)

    while True:
        schedule.run_pending()