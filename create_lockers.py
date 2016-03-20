from __future__ import unicode_literals

import logging
import os

logger = logging.getLogger(__name__)


def populate():
    for i in range(10):
        logger.debug(i)
        add_locker(str(i*111111), 0)


def add_locker(combo, num):
    p = Locker.objects.get_or_create(
        current_combo=combo,
        combo_number=num,
        combo0=combo,
        combo1=combo,
        combo2=combo,
        combo3=combo,
        combo4=combo
    )[0]
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting Locker population script..."
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mathsocwebsite.settings')
    django.setup()
    from services.models import Locker
    populate()


# locker_number = models.IntegerField(unique=True)
# current_combo = models.CharField(max_length=6)
# combo_number = models.IntegerField()
#
# combo0 = models.CharField(max_length=6)
# combo1 = models.CharField(max_length=6)
# combo2 = models.CharField(max_length=6)
# combo3 = models.CharField(max_length=6)
# combo4 = models.CharField(max_length=6)
