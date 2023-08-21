import jwt
from django_ninja_learn.settings import JWT_SECRET_KEY
from user_app.models import SysUser

# 生成 JWT 令牌
def generate_token(user_id: int):
    payload = {
        'user_id': user_id,
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    return token

def verify_token(token):
    payload = jwt.decode(token, JWT_SECRET_KEY, algorithms='HS256')
    print(payload)
    return payload