from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .routers.dev import dev_router
from .routers.login import login_router
from .routers.projects import projects_router
from .routers.contact import contact_router
import os
from fastapi.responses import FileResponse

app = FastAPI(openapi_url="/api/openapi.json",
              docs_url="/api/docs", redoc_url=None)

origins = ['*', 'https://www.sh-haimin.cn']

Image_Dir = '/home/ubuntu/backend/static/images'
Video_Dir = '/home/ubuntu/backend/static/videos'


@app.on_event('startup')
async def startup():
    load_dotenv()

app.include_router(dev_router, tags=['dev'], prefix='/api/dev')
app.include_router(login_router, tags=['login'], prefix='/api/login')
app.include_router(projects_router, tags=['projects'], prefix='/api/projects')
app.include_router(contact_router, tags=['contact'], prefix='/api/contact')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/api/images/{image_name}')
async def get_image(image_name: str):
    # Construct the full path to the image
    file_path = os.path.join(Image_Dir, image_name)
    # Check if the file exists
    if not os.path.isfile(file_path):
        return {"error": "File not found"}
    # Return the image file
    return FileResponse(file_path)


@app.get('/api/videos/{video_name}')
async def get_video(video_name: str):
    # Construct the full path to the image
    file_path = os.path.join(Video_Dir, video_name)
    # Check if the file exists
    if not os.path.isfile(file_path):
        return {"error": "File not found"}
    # Return the image file
    return FileResponse(file_path)
