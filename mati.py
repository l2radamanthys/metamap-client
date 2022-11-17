from client import ApiClient
from utils import encode_base64


class MatiException(Exception):
    pass


class MatiClient(ApiClient):
    def __init__(self, timeout=500):
        super(MatiClient, self).__init__(base_url="https://api.getmati.com", timeout=timeout)
        self.config = {"base_url": "https://api.getmati.com"}

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
        
    def auth(self, client_id, client_secret):
        payload = "grant_type=client_credentials"
        headers = self.headers
        headers["Authorization"] = "Basic " + encode_base64(f"{client_id}:{client_secret}")
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        response = self.post_request("oauth", data=payload, headers=headers)
        response_data = response.json()
        if response.status_code == 200:
            self.config["access_token"] = response_data["access_token"]
        else:
            raise MatiException(f"Error {response.status_code}: {response_data.get('message')}")
        return True

    def get_resource_data(self, id_):
        response = self.get_request(f"/v2/verifications/{id_}", headers=self.headers)
        response_data = response.json()
        if response.status_code == 200:
            return response_data
        else:
            raise MatiException(f"Error {response.status_code}: {response_data.get('message')}")