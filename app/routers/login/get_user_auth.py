from fastapi import Depends
from .login_router import login_router
from ...database import get_db
from ...models.dev.dev_models import DevModel
from sqlalchemy.orm import Session

@login_router.get('/get_user_auth')
async def get_user_auth(db:Session = Depends(get_db)):
    return db.query(DevModel).all()
