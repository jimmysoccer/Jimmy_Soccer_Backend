from ...database import create_session
from .contact_router import contact_router
from sqlalchemy.exc import SQLAlchemyError
from ...models.contact.contact_models import ContactDBModel, ContactModel
from datetime import datetime

@contact_router.post('/send_messages')
async def send_messages(message:ContactModel):
    session = create_session()
    payload = ContactDBModel(title=message.title,content=message.content,email=message.email,
                                sent_date = datetime.now())

    try:
        session.add(payload)
        session.commit()
        # Return success message
        return {"message": "message sent successfully!"}

    except SQLAlchemyError as e:
        # Handle any errors
        session.rollback()
        print(f"Error occurred: {e}")

    finally:
        session.close()

@contact_router.get('/get_messages')
async def get_messages():
    session = create_session()

    messages = session.query(ContactDBModel).all()

    session.close()
    
    return{
        'messages':messages
    }
