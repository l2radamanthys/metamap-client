from base_client import MatiException, MMBaseClient
from verification_component import VerificationComponent
from arg_components import ArgCreditCheckComponent
from utils import encode_base64


class MatiClient(MMBaseClient):
    def __init__(self, timeout=500):
        super(MatiClient, self).__init__(
            base_url="https://api.getmati.com", timeout=timeout
        )
        self.verification = VerificationComponent(timeout)
        self.ar_credit_check = ArgCreditCheckComponent(timeout)

    def auth(self, client_id, client_secret):
        payload = "grant_type=client_credentials"
        headers = self.headers
        headers["Authorization"] = "Basic " + encode_base64(
            f"{client_id}:{client_secret}"
        )
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        response = self.post_request("oauth", data=payload, headers=headers)
        response_data = response.json()
        if response.status_code == 200:
            self.update_token(response_data["access_token"])
        else:
            raise MatiException(
                f"Error {response.status_code}: {response_data.get('message')}"
            )
        return True

    def update_token(self, token):
        super().update_token(token)
        self.verification.update_token(token)
        self.ar_credit_check.update_token(token)
