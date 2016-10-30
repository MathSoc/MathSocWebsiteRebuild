from __future__ import unicode_literals
from io import open
import logging
import os

from django.conf import settings
from oat import liboat
import json

logger = logging.getLogger(__name__)

oat_base_url = "https://oat.uwaterloo.ca"
api_key = open("./keys_and_pws/oat_pkey.pcks8").read()
api_user = os.environ['OAT_USER']

def is_society_member(userid):
    oat = liboat.Session(api_user, api_key, oat_base_url)
    try:
        r = oat.get("/api/v2/student/{userid}/societyMember/MAT.{term}".format(
            userid=userid,
            term=settings.CURRENT_TERM
        ))
        if r.status_code == 200:
            logger.debug("{} is society member".format(userid))
            return True
    except Exception as e:
        if len(e.args) and e.args[0]:
            e_dict = json.loads(e.args[0])
            if e_dict['error']['status'] == 404:
                logger.debug("{} is not a society member".format(userid))
            logger.error("Got unexpected response: {}".format(e_dict))
        else:
            raise e

    return False

