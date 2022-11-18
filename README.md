# Metamap Client

Simple python API client integration for [Metamap API](https://metamap.com) basic functions.

### Usage

	from metamap_client.mati import MatiClient
	
	client = MatiClient()
	client.auth("client_id", "client_secret")
	
	# Get verification data 
	data = client.verification.get("verification_id")

