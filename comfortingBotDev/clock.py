from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime

sched = BlockingScheduler()
@sched.scheduled_job('cron', minute = "*/1")
def scheduled_job():
    print("="*20)
    print(f'{datetime.datetime.now().ctime()}')
    print('this job runs every day every 1 min')
    print("="*20)
    url = "https://treehole-comfortbot.herokuapp.com/"
    conn = urllib.request.urlopen(url)
    
    for key, value in conn.getheader():
        print(key, value) 
sched.start()