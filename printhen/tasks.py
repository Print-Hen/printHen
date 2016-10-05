from __future__ import absolute_import
#from djcelery import celery
from celery.task import periodic_task
from celery.task.schedules import crontab
from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded


@shared_task
@periodic_task(run_every=datetime.timedelta(seconds=2))
def hello():
    print "HELLO"

# @periodic_task(run_every=datetime.timedelta(minutes=55))
# def hello():
#       i = 0
#       print "hello"
#       hello()

@shared_task
def login():
    g = gmail.login('printhen','parvathi12#')
    print g.inbox.mail()

# @celery.task
# def add():
#       return 2+3
