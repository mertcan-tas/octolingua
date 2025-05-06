from cryptography.fernet import Fernet
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from datetime import datetime, timedelta, UTC
from decouple import config
import json

FERNET_SECRET_KEY = config("FERNET_SECRET_KEY", default=Fernet.generate_key(), cast=str) 
EMAIL_VERIFICATION_TOKEN_TTL=config("EMAIL_VERIFICATION_TOKEN_TTL", default=900, cast=int) # 900 => 15 MIN

fernet = Fernet(FERNET_SECRET_KEY.encode())

def generate_token(user_id: int, expiry_second: int = EMAIL_VERIFICATION_TOKEN_TTL) -> str:
    payload = {
        'user_id': user_id,
        'exp': (datetime.now(UTC) + timedelta(seconds=expiry_second)).timestamp()
    }
    json_data = json.dumps(payload).encode()
    token = fernet.encrypt(json_data) 
    return urlsafe_base64_encode(token) 


def verify_token(token: str):
    try:
        token_bytes = urlsafe_base64_decode(token)  # str -> bytes -> çözülmüş token
        decrypted = fernet.decrypt(token_bytes)  # bytes -> çözümlenmiş bytes
        payload = json.loads(decrypted.decode())  # bytes -> str -> dict
        exp = payload.get('exp')
        if exp and datetime.now(UTC).timestamp() > exp:
            return None  # Süresi geçmiş
        return payload.get('user_id')  # Doğruysa kullanıcı ID'sini döndür
    except Exception as e:
        print("Token doğrulama hatası:", e)
        return None



# token = generate_token(232323)
# print("Token:", token)

# print()

# user_id = verify_token(token)
# print("Doğrulanan User ID:", user_id)