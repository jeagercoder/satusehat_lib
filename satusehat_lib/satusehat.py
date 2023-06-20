from django.conf import settings
from django.core.cache import cache

from urllib.parse import urljoin

from .base import (
    BaseSatuSehat
)
from .utils import generate_token_authorization


class SatuSehat(BaseSatuSehat):

    def get_token_authorization(self):
        token = cache.get('token_satusehat')
        if not token:
            return generate_token_authorization()
        return token

    def get_url(self):
        return urljoin(settings.SATUSEHAT_SERVICE_URL, self.r_route)

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.token_authorization}'
        }

