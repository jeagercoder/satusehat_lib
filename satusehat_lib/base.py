import requests


class BaseSatuSehat:

    def __init__(self,
                 route,
                 data=None,
                 json=None,
                 files=None,
                 params=None):
        self.r_route = route
        self.r_data = data
        self.r_json = json
        self.r_files = files
        self.r_params = params

        self.token_authorization = self.token_authorization = self.get_token_authorization()

        self.__resp = None

    def get_token_authorization(self):
        raise NotImplementedError('`.get_token_authorization()` must be implemented.')

    def get_url(self):
        raise NotImplementedError('`.get_token_authorization()` must be implemented.')

    def get_headers(self):
        raise NotImplementedError('`.get_headers()` must be implemented.')

    def get_kwargs(self):
        return {
            'data': self.r_data,
            'json': self.r_json,
            'files': self.r_files,
            'params': self.r_params,
            'headers': self.get_headers()
        }

    @staticmethod
    def __do_request(method, url, **kwargs):
        request = requests.request(method=method, url=url, **kwargs)
        return request

    def get(self):
        req = self.__do_request(method='get', url=self.get_url(), **self.get_kwargs())
        self.__resp = req

    def post(self):
        req = self.__do_request(self, method='post', url=self.get_url(), **self.get_kwargs())
        self.__resp = req

    def put(self):
        req = self.__do_request(self, method='put', url=self.get_url(), **self.get_kwargs())
        self.__resp = req

    def delete(self):
        req = self.__do_request(self, method='delete', url=self.get_url(), **self.get_kwargs())
        self.__resp = req

    @property
    def data(self):
        if self.__resp is None:
            raise ValueError('You must call `.get()`, `.post()`, or .`put()` before access `.response`')
        return self.__resp.json()

    @property
    def status_code(self):
        if self.__resp is None:
            raise ValueError('You must call `.get()`, `.post()`, or .`put()` before access `.status_code`')
        return self.__resp.status_code








