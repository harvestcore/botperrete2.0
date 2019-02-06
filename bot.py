from apscheduler.schedulers.blocking import BlockingScheduler
from toot import Toot

scheduler = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def job():
    Toot.commit_tweet("XD")


scheduler.start()