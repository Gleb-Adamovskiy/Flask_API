from flask import request
from implemented import auth_service
# декоратор, в котором мы будет проверять переданный токен
def check_autorization(func):
    def check(*args, **kwargs):
        auth_header = request.headers.get('Autorization')

        if auth_header:
            token = auth_header.split(" ")[1]
        else:
            token = ""
        uid = auth_service.decode_auth_token(token.encode())
        user = auth_service.get_by_id(uid)
        if user:
            return func(*args, **kwargs)
        else:
            return "Not autorized", 403
    return check
