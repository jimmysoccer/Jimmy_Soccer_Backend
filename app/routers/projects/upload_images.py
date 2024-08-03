from .projects_router import projects_router
from sqlalchemy.exc import SQLAlchemyError
from fastapi import File, UploadFile
import shutil

Image_Dir = 'static/images'


@projects_router.post('/upload_images')
async def upload_images(images: list[UploadFile] = File('image')):
    try:
        file_locations = []
        for image in images:
            file_location = f"{Image_Dir}/{image.filename}"
            with open(file_location, "wb+") as file_object:
                shutil.copyfileobj(image.file, file_object)
            file_locations.append(file_location)
        # Return success message
        return {"message": "upload images successfully!"}

    except SQLAlchemyError as e:
        # Handle any errors
        print(f"Error occurred: {e}")
        return {"message": 'upload images failed!'}
