import jwt
import datetime
from config import API_KEY, API_SECRET


def generate_api_jwt():
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
        "iss": API_KEY,  # Use "iss" for the API key
        "exp": int(token_expiration.timestamp()),
        "iat": int(now_utc.timestamp())
    }

    # Generating the JWT
    token = jwt.encode(payload, API_SECRET, algorithm='HS256', headers=header)
    return token
