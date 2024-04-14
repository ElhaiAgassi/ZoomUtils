import jwt
import datetime
from config import SDK_KEY,SDK_SECRET

def generate_sdk_jwt():
    # Current UTC time
    now_utc = datetime.datetime.utcnow()
    # Token expiration time
    token_expiration = now_utc + datetime.timedelta(days=30)  # 1 hour from now

    # JWT Header
    header = {
        "alg": "HS256",
        "typ": "JWT"
    }

    # JWT Payload
    payload = {
        "aud": None,  # Set audience to null
        "iss": SDK_KEY,  # Use "iss" for the API key
        "exp": int(token_expiration.timestamp()),
        "iat": int(now_utc.timestamp())
    }

    # Generating the JWT
    token = jwt.encode(payload, SDK_SECRET, algorithm='HS256', headers=header)

    return token
