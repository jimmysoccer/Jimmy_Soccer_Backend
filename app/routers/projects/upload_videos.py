from .projects_router import projects_router
from sqlalchemy.exc import SQLAlchemyError
from fastapi import File, UploadFile
import shutil

Video_Dir = 'static/videos'


@projects_router.post('/upload_videos')
async def upload_videos(videos: list[UploadFile] = File('videos')):
    print('videos', videos)
    try:
        file_locations = []
        for video in videos:
            file_location = f"{Video_Dir}/{video.filename}"
            with open(file_location, "wb+") as file_object:
                shutil.copyfileobj(video.file, file_object)
            file_locations.append(file_location)
        # Return success message
        return {"message": "upload videos successfully!"}

    except SQLAlchemyError as e:
        # Handle any errors
        print(f"Error occurred: {e}")
        return {"message": 'upload videos failed!'}
