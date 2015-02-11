from mkmsdk.api import Api


class SimpleResolver:
    def __init__(self):
        self.url = ''
        self.method = ''
        self.api = Api()

    def setup(self, api_map=None, url_entry=None):

        url, method = api_map['url'], api_map['method']
        url_entry = url_entry or {}

        url = url.format(**url_entry)
        self.url = url
        self.method = method

    def resolve(self, api_map=None, url_entry=None, **kwargs):
        self.setup(api_map=api_map, url_entry=url_entry)

        return self.api.request(url=self.url, method=self.method, **kwargs)
