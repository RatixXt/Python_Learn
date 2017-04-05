import time
import urllib.request
import bs4

def log_duration(f):
    def wrapper(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: {}".format(time.time()-t))
        return res

    return wrapper


@log_duration
def current_time_in_the_world():
    html_str = urllib.request.urlopen('https://time100.ru/')
    soup = bs4.BeautifulSoup(html_str, 'html.parser')
    tags = soup.select('div.time')
    [print('{}: {}'.format(tag['data-tz'], tag.text)) for tag in tags]

current_time_in_the_world()