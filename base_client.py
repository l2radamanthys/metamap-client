from client import ApiClient


class MMBaseClient(ApiClient):
    def __init__(self, base_url, timeout):
        super(MMBaseClient, self).__init__(base_url=base_url, timeout=timeout)
        self.config = {"base_url": base_url}

    @property
    def headers(self):
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        if self.config.get("access_token", False):
            headers["Authorization"] = f"Bearer {self.config.get('access_token')}"
        return headers

    @property
    def is_login(self):
        return self.config.get("access_token", False)

    def update_token(self, token):
        self.config["access_token"] = token


class MatiException(Exception):
    pass
