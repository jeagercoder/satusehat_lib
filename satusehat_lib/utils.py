from django.conf import settings
from django.core.cache import cache

import requests
from urllib.parse import urljoin

from .exceptions import (
    GenerateTokenError
)


def generate_token_authorization():
    url = urljoin(settings.SATUSEHAT_SERVICE_URL, 'oauth2/v1/accesstoken')
    params = {'grant_type': 'client_credentials'}
    data = {
        'client_id': settings.SATUSEHAT_CLIENT_KEY,
        'client_secret': settings.SATUSEHAT_SECRET_KEY
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    req = requests.post(url, data=data, params=params, headers=headers)
    if 200 <= req.status_code <= 299:
        token = req.json().get('access_token')
        expired_in = int(req.json().get('expires_in')) - 10
        cache.set('token_satusehat', token, expired_in)
        return token
    raise GenerateTokenError(f'Failed get token, \nstatus_code: {req.status_code}, \nresponse: {req.text}')
