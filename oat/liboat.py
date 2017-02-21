#!/usr/bin/env python3
import requests
import base64
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from datetime import datetime, timezone


class Session:
    api_user = None
    api_key = None
    api_url = None
    api_auth_url = None
    api_headers = None
    session = None
    session_request = None

    def __init__(self, api_user, api_key, api_url='https://oat.uwaterloo.ca', api_headers=None):
        self.api_user = api_user
        self.api_key = api_key
        self.api_url = api_url
        self.api_auth_url = '{0}/api/v2/authenticate'.format(api_url)
        self.api_headers = api_headers

    def get_credential(self):
        '''
        return a credential object given a client_id and key
        '''
        client_id = self.api_user
        key = self.api_key
        time = datetime.now(timezone.utc).isoformat()
        message = (client_id + "|" + time).encode('utf-8')
        key = RSA.importKey(key)
        signer = PKCS1_v1_5.new(key)
        raw_sha = SHA.new(message)
        signature = signer.sign(raw_sha)
        msgB64 = base64.urlsafe_b64encode(message).decode('utf-8')
        sigB64 = base64.urlsafe_b64encode(signature).decode('utf-8')
        return {'client_id': client_id, 'message': msgB64, 'signature': sigB64}

    def _create_session(self):
        '''
        create new session
        '''
        s = requests.session()
        if self.api_headers:
            s.headers = self.api_headers
        self.session_request = s.post(self.api_auth_url, json=self.get_credential())
        if 'OAT_auth' not in s.cookies:
            raise Exception(self.session_request.content)
        return s

    def get(self, api):
        '''
        Perform a http get. Recreate session if needed
        '''
        r = None
        url = self.api_url + api
        for retries in range(2):
            if not self.session:
                self.session = self._create_session()
            r = self.session.get(url, headers={'Accept': 'application/json'})
            if r.status_code == 200:
                return r
            if 'Appropriate credentials have not been presented' in r.text:
                ## session timed out
                self.session = None
        raise Exception(r.text)


if __name__ == "__main__":
    oat = Session('_mathsocmbrtest', open('keys_and_pws/oat_pkey.pcks8').read())
    import time
    import json
    t = time.time()
    for c in range(200):
        r = oat.get('/api/v2/pps/plan/CSBSE.*')
        print('** request_body:')
        print(r.request.body)
        print('** request_header:')
        print(r.request.headers)
        print(json.dumps(r.json(), indent=4, sort_keys=True))
        time.sleep(1)
