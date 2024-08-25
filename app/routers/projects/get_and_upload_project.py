from .projects_router import projects_router
from sqlalchemy.exc import SQLAlchemyError
from ...database import create_session
from ...models.projects.project_models import Project, ProjectModel
from pydantic import BaseModel


@projects_router.post('/upload_project')
async def upload_project(project: ProjectModel):
    session = create_session()
    payload = Project(title=project.title, place=project.place,
                      start_date=project.start_date,
                      end_date=project.end_date, description=project.description,
                      images=project.images, videos=project.videos)
    try:
        session.add(payload)
        session.commit()

        # Return success message
        return {"message": "project upload successfully!"}

    except SQLAlchemyError as e:
        # Handle any errors
        session.rollback()
        print(f"Error occurred: {e}")

    finally:
        session.close()


@projects_router.get('/get_projects')
async def get_projects():
    try:
        session = create_session()
        projects = session.query(Project).all()

        for project in projects:
            if project.images == '':
                project.images = []
            else:
                image_names = project.images.split(',')
                base_url = 'https://www.sh-haimin.cn/api/images/'
                image_urls = [
                    base_url+image_name for image_name in image_names]
                project.images = image_urls

            if project.videos == '' or project.videos is None:
                project.videos = []
            else:
                video_names = project.videos.split(',')
                base_url = 'https://www.sh-haimin.cn/api/videos/'
                video_urls = [
                    base_url+video_name for video_name in video_names]
                project.videos = video_urls

        # Return success message
        return {
            'status_code': 200,
            'projects': projects
        }

    except SQLAlchemyError as e:
        # Handle any errors
        session.rollback()
        print(f"Error occurred: {e}")

    finally:
        session.close()


@projects_router.post('/edit_project')
async def edit_projects(project: ProjectModel):
    try:
        id = project.id
        session = create_session()
        db_project = session.query(Project).filter(Project.id == id).first()

        if project is None:
            return {'status_code': 404}

        db_project.title = project.title
        db_project.place = project.place
        db_project.start_date = project.start_date
        db_project.end_date = project.end_date
        db_project.description = project.description
        db_project.images = project.images
        db_project.videos = project.videos

        session.commit()
        session.refresh(db_project)

        # Return success message
        return {
            'status_code': 200,
            "message": 'successfully edit record',
            'project': db_project
        }

    except SQLAlchemyError as e:
        # Handle any errors
        session.rollback()
        print(f"Error occurred: {e}")

    finally:
        session.close()


class DeleteModel(BaseModel):
    id: int


@projects_router.post('/delete_project')
async def delete_projects(delete: DeleteModel):
    try:
        id = delete.id
        session = create_session()
        project = session.query(Project).filter(Project.id == id).first()

        if project is None:
            return {'status_code': 404}

        session.delete(project)
        session.commit()

        # Return success message
        return {
            'status_code': 200,
            "message": 'successfully delete record'
        }

    except SQLAlchemyError as e:
        # Handle any errors
        session.rollback()
        print(f"Error occurred: {e}")

    finally:
        session.close()
