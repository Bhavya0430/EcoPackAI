from models.user import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(username, email, password):
    # Check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return None

    hashed_password = generate_password_hash(password)

    user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()
    return user


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        return user

    return None
