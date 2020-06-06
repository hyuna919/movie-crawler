import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

url='http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200525'
bot = telegram.Bot(token = '1218021692:AAEiz5oi3qjrSPniksysazIe10JTo-V-gOI')
id = 1157929440

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    cine = soup.select_one('span.cine')

    if (cine):
        cine = cine.find_parent('div', class_='col-times')
        title = cine.select_one('div.info-movie > a > strong').text.strip()
        # print(cine.select_one('a > strong').text.strip())
        # print(title+' 열림')
        msg = title + ' 씨네 영화 예매 가능'
        bot.sendMessage(chat_id=id, text=msg)
        sched.pause()


sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=3)
sched.start()