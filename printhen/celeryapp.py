"""set the default Django settings module for the 'celery' program."""

from __future__ import absolute_import

import os
from django.conf import settings  # noqa
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'printhen.settings')
APP = Celery('printhen')


# Using a string here means the worker will not have to
# pickle the object when using Windows.
APP.config_from_object('django.conf:settings')
APP.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@APP.task(bind=True)
def debug_task(self):
    """Debug Task """
    print ('Request: {0!r}'.format(self.request))
