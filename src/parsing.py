import pytz
from datetime import datetime
import requests
from bs4 import BeautifulSoup as Bs4
from tkinter import *
from ui import *

def launch_parser(text_widget):
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/119.0.0.0 Safari/537.36'
    }

    url = "https://www.championat.com/news/football/1.html?utm_source=button&utm_medium=news"
    session = requests.Session()

    try:
        push_req = session.get(url, headers=headers)
        if push_req.status_code == 200:
            soup = Bs4(push_req.content, 'html.parser')
            divs = soup.find_all('div', attrs={'class': 'news-item'})
            results = ""
            for div in divs:
                date_today = str(datetime.now(pytz.timezone('Europe/Moscow'))).split()[0]
                time = str(div.find('div', attrs={'class': 'news-item__time'}).text)
                title = div.find('a').text
                link = 'https://championat.com/' + str(div.find('a')['href'])

                # Добавляем заголовок как гиперссылку
                results += f"Дата: {date_today}, Время: {time}, "
                results += f"{title}\n\n"

                # Добавляем тег для гиперссылки
                text_widget.insert(END, f"{title}\n", 'link')
                text_widget.insert(END, f"Дата: {date_today}, Время: {time}\n\n")

                # Добавляем ссылку
                text_widget.tag_bind('link', '<Button-1>', lambda e, url=link: open_link(url))

            text_widget.insert(END, results)
        else:
            text_widget.insert(END, "Error: Unable to fetch the webpage.\n")

    except Exception as e:
        text_widget.insert(END, f"An error occurred: {e}\n")
        print(e)

def open_link(url):
    import webbrowser
    webbrowser.open(url)

def main():
    window()

    text_widget = Text(root, wrap='word', height=20, width=80, bg= '#2f2f2f', fg= 'white',
    font= ('Helvetica', 12 ))
    text_widget.pack(expand=True, fill='both')

    fetch_button = Button(root, text="Fetch News", command=lambda: launch_parser(text_widget))
    fetch_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()