from database.models.user_model import User
from routes.schemas.user_schema import UserLogin, UserRegister


def create_user(db, user: UserRegister):
    new_user_register = User(**user.dict())
    print(user)
    try:
        db.add(new_user_register)
    except Exception as e:
        print(e)
    print('Added User')
    db.commit()

def user_login(db, credentials: UserLogin):
    user = read_user_by_username(db, credentials.username)
    if not user.password == credentials.password:
        return False
    return True

def read_user_by_username(db, username: str):
    user = db.query(User).filter(User.username==username).first()
    return user