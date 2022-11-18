from base_client import MatiException, MMBaseClient


class ArgCreditCheckComponent(MMBaseClient):
    def __init__(self, timeout):
        super(ArgCreditCheckComponent, self).__init__(
            base_url="https://api.getmati.com/creditchecks/v1", timeout=timeout
        )

    def get(self, cuit, callbackUrl):
        payload = {"cuit": cuit, "callbackUrl": callbackUrl}
        response = self.post_request(
            "/ar/credit-fidelitas", 
            data=payload, 
            headers=self.headers
        )
        return response