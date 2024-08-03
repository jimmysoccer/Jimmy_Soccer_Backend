from .login_router import login_router
from ...database import create_session
from ...models.login.login_models import UserModel
from sqlalchemy.exc import SQLAlchemyError
import bcrypt


@login_router.post('/post_new_user')
async def post_new_user(username: str, password: str):
    session = create_session()
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    new_user = UserModel(username, hashed)

    try:
        session.add(new_user)
        session.commit()

        # Return success message
        return {"message": "User created successfully"}

    except SQLAlchemyError as e:
        # Handle any errors
        session.rollback()
        print(f"Error occurred: {e}")

    finally:
        session.close()
