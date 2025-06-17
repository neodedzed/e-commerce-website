from database.models.user_model import User
from routes.schemas.user_schema import UserRegister


def create_user(db, user: UserRegister):
    new_user_register = User(**user.dict())
    print(user)
    try:
        db.add(new_user_register)
    except Exception as e:
        print(e)
    print('Added User')
    db.commit()