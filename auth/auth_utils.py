from config.database import users_collection
from auth.password import hash_password, verify_password


def signup_user(name, email, password):

    existing = users_collection.find_one(
        {"email": email}
    )

    if existing:
        return False, "Email already exists"

    user = {

        "name": name,

        "email": email,

        "password": hash_password(password)

    }

    result = users_collection.insert_one(user)

    user["_id"] = result.inserted_id

    return True, user


def login_user(email, password):

    user = users_collection.find_one(
        {"email": email}
    )

    if user is None:

        return False, "User not found"

    if not verify_password(
        password,
        user["password"]
    ):

        return False, "Incorrect Password"

    return True, user
