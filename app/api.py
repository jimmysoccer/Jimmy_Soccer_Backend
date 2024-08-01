from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .routers.dev import dev_router
from .routers.dev import login_router

app = FastAPI(openapi_url="/api/openapi.json",docs_url="/api/docs", redoc_url=None)

origins = ['*']

@app.on_event('startup')
async def startup():
    load_dotenv()

app.include_router(dev_router,tags=['dev'],prefix='/api/dev')
app.include_router(login_router,tags=['login'],prefix='/api/login')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
