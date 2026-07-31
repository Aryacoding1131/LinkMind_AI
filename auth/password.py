import bcrypt
def hash_password(password):
    password = password.encode("utf-8")
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed

def verify_password(password, hashed_password):
    password = password.encode("utf-8")
    return bcrypt.checkpw(password, hashed_password)