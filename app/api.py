from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .routers.dev import dev_router
from .routers.login import login_router
from .routers.projects import projects_router
import os
from fastapi.responses import FileResponse

app = FastAPI(openapi_url="/api/openapi.json",
              docs_url="/api/docs", redoc_url=None)

origins = ['*']

Image_Dir = 'static/images'


@app.on_event('startup')
async def startup():
    load_dotenv()

app.include_router(dev_router, tags=['dev'], prefix='/api/dev')
app.include_router(login_router, tags=['login'], prefix='/api/login')
app.include_router(projects_router, tags=['projects'], prefix='/api/projects')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/{image_name}')
async def get_image(image_name: str):
    # Construct the full path to the image
    file_path = os.path.join(Image_Dir, image_name)

    # Check if the file exists
    if not os.path.isfile(file_path):
        return {"error": "File not found"}

    # Return the image file
    return FileResponse(file_path)
