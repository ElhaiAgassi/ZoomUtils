import datetime
import sys
import jwt
from config import SDK_KEY, SDK_SECRET

def generate_sdk_jwt(session_name="mysession"):
    print ("The session name is: "+session_name)

    now_utc = datetime.datetime.utcnow()
    token_expiration = now_utc + datetime.timedelta(hours=40)  # 40 hours from now. (limited to 48)

   # Convert datetime to integer timestamps
    iat_timestamp = int(now_utc.timestamp())
    exp_timestamp = int(token_expiration.timestamp())

    # JWT Header
    header = {
	    "typ": "JWT",
        "alg": "HS256"
    }

    # JWT Payload
    payload = {
	    "app_key": SDK_KEY,
        "role_type": 1,  # 1 is an host, 0 is participant
        "tpc": session_name,  # Add session name to the payload as 'tpc'.
	    "version": 1,
        "iat": iat_timestamp, # The token issue timestamp.
        "exp": exp_timestamp , # The JWT expiration timestamp.
        
    }

    # Generating the JWT
    token = jwt.encode(payload, SDK_SECRET, algorithm='HS256', headers=header)

    return token

if __name__ == "__main__":
    session_name = sys.argv[1] if len(sys.argv) > 1 else None
    if session_name is None:
        print("No session name provided. Default - \"mysession\"")
    token = generate_sdk_jwt(session_name)
    print("Key:\n"+token)

