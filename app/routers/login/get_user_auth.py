from .login_router import login_router
from ...database import create_session
from ...models.login.login_models import UserModel
import bcrypt
from fastapi.responses import JSONResponse


@login_router.get('/get_user_auth')
async def get_user_auth(username: str, password: str):
    print('username', username)
    session = create_session()
    user = session.query(UserModel).filter(
        UserModel.username == username).first()
    password = password.encode('utf-8')
    stored_hash = user.password.encode('utf-8')
    if bcrypt.checkpw(password, stored_hash):
        return JSONResponse(status_code=200, content={'message': 'Authentication Passed!'})
    else:
        return JSONResponse(content={'message': 'Authentication Failed!'}, status_code=401)
