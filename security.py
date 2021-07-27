from werkzeug.security import safe_str_cmp
from model.user import User

users = [
    User( 'user1', 'abcxyz'),
    User( 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    print
    return userid_table.get(user_id, None)
