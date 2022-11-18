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
            raise MatiException(
                f"Error {response.status_code}: {response_data.get('message')}"
            )

    def get_media(self, media_auth):
        response = self.get_request(
            f"/file?location={media_auth}", headers=self.headers
        )
        return response.json()

    def download_results(self, ids):
        raise MatiException("Don't implement")

    def start(self, flow_id, metadata):
        raise MatiException("Don't implement")

    def send_inputs(self, *args, **argvs):
        raise MatiException("Don't implement")

    def update_status(self, status):
        raise MatiException("Don't implement")

    def skip_upload_wait_time(self, id_):
        raise MatiException("Don't implement")