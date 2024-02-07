# lib/dog.py
from sqlalchemy.orm import Session
from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session: Session, dog: Dog):
    session.add(dog)
    session.commit()

def get_all(session: Session):
    return session.query(Dog).all()

def find_by_name(session: Session, name: str):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session: Session, dog_id: int):
    return session.query(Dog).get(dog_id)

def find_by_name_and_breed(session: Session, name: str, breed: str):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session: Session, dog: Dog, new_breed: str):
    dog.breed = new_breed
    session.commit()

