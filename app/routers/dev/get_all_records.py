from fastapi import Depends
from .dev_router import dev_router
from ...database import get_db
from ...models.dev.dev_models import DevModel
from sqlalchemy.orm import Session

@dev_router.get('/get_all_records')
async def get_all_records(db:Session = Depends(get_db)):
    return db.query(DevModel).all()
