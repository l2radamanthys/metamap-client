
from base_client import MatiException, MMBaseClient


class VerificationComponent(MMBaseClient):
    def __init__(self, timeout):
        super(VerificationComponent, self).__init__(
            base_url="https://api.getmati.com", timeout=timeout
        )

    def get(self, id_):
        response = self.get_request(f"/v2/verifications/{id_}", headers=self.headers)
        response_data = response.json()
        if response.status_code == 200:
            return response_data
        else:
            raise MatiException(f"Error {response.status_code}: {response_data.get('message')}")

    def get_media(self, media_auth):
        response = self.get_request(f"/file?location={media_auth}", headers=self.headers)
        return response.json()

    def download_results(self, ids):
        pass