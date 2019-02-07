from apscheduler.schedulers.blocking import BlockingScheduler
from toot import Toot

sched = BlockingScheduler(timezone='Europe/Madrid')

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    Toot.commit_tweet("XD")


sched.start()