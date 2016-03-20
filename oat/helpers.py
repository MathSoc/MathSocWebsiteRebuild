from __future__ import unicode_literals
from io import open
import logging

from django.conf import settings
from oat import liboat
import json

logger = logging.getLogger(__name__)

oat_base_url = "https://oat.uwaterloo.ca"
api_key = open("./keys_and_pws/oat_pkey.pcks8").read()
api_user = "_mathsocmbrtest"

def is_society_member(userid):
    oat = liboat.Session(api_user, api_key, oat_base_url)
    r = oat.get("/api/v2/student/{userid}/societyMember/MAT.{term}".format(
        userid=userid,
        term=settings.CURRENT_TERM
    ))
    if r.status_code == 200:
        return True
    elif r.status_code != 404:
        logger.error("Got unexpected status code on checking society membership: {}".format(
            json.dumps(r.json())
        ))

    return False

