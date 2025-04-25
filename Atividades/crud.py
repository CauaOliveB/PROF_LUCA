from sqlalchemy.orm import Session
from models import God
from schemas import GodCreate, GodUpdate

def get_gods(db: Session):
    return db.query(God).all()

def get_god(db: Session, god_id: int):
    return db.query(God).filter(God.id == god_id).first()

def create_god(db: Session, god: GodCreate):
    db_god = God(**god.dict())
    db.add(db_god)
    db.commit()
    db.refresh(db_god)
    return db_god

def update_god(db: Session, db_god: God, god_update: GodUpdate):
    for field, value in god_update.dict(exclude_unset=True).items():
        setattr(db_god, field, value)
    db.commit()
    db.refresh(db_god)
    return db_god

def delete_god(db: Session, db_god: God):
    db.delete(db_god)
    db.commit()
