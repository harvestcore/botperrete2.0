from apscheduler.schedulers.blocking import BlockingScheduler
from toot import Toot
import random, string

sched = BlockingScheduler(timezone='Europe/Madrid')

# @sched.scheduled_job('interval', minutes=100)
# def timed_job():
#     tw = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
#     Toot.commit_tweet(tw)

@sched.scheduled_job('interval', minutes=1)
def boterino():
    Toot.boterino()

sched.start()