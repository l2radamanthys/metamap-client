import base64


def require_keys(d, keys):
    if isinstance(keys, str):
        keys = [keys]
    for k in keys:
        if k not in d:
            raise ValueError(f"'{k}' must be set".format(k))
    return True

def encode_base64(text):
    message_bytes = text.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode("ascii")

def calculate_identity_id(verification_id):
    identity_id = hex(int(verification_id, 16) - 2)[2:]
    return identity_id