
'''

    *-------------------------------------------------------------------------------*
    |                                  FastAPI                                      |
    |   Date: 28/03/2025                                                            |
    |   Instructor(s) : Wilson Ferreira / Luca Dias                                 |
    |   Aula 1 : CRUD                                                               |
    |   Atividade : Criar uma API                                                   |
    |                                                                               |
    * ------------------------------------------------------------------------------*

    *------------------------*
    | Tema : Mitologia Grega |
    *------------------------*

'''

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
import crud, schemas
from fastapi.staticfiles import StaticFiles
import models

app = FastAPI()


Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/gods", response_model=list[schemas.GodOut])
def read_gods(db: Session = Depends(get_db)):
    return crud.get_gods(db)

@app.get("/gods/{god_id}", response_model=schemas.GodOut)
def read_god(god_id: int, db: Session = Depends(get_db)):
    god = crud.get_god(db, god_id)
    if not god:
        raise HTTPException(status_code=404, detail="God don't finded")
    return god

@app.post("/gods", response_model=schemas.GodOut)
def create_god(god: schemas.GodCreate, db: Session = Depends(get_db)):
    return crud.create_god(db, god)

@app.put("/gods/{god_id}", response_model=schemas.GodOut)
def update_god(god_id: int, new_data: schemas.GodCreate, db: Session = Depends(get_db)):
    db_god = db.query(models.God).filter(models.God.id == god_id).first()
    if not db_god:
        raise HTTPException(status_code=404, detail="God don't finded")
    
    for field, value in new_data.dict().items():
        setattr(db_god, field, value)

    db.commit()
    db.refresh(db_god)
    return db_god


@app.patch("/gods/{god_id}", response_model=schemas.GodOut)
def patch_god(god_id: int, god_update: schemas.GodUpdate, db: Session = Depends(get_db)):
    db_god = db.query(models.God).filter(models.God.id == god_id).first()
    if not db_god:
        raise HTTPException(status_code=404, detail="God don't finded")
    
    for field, value in god_update.dict(exclude_unset=True).items():
        setattr(db_god, field, value)

    db.commit()
    db.refresh(db_god)
    return db_god


@app.delete("/gods/{god_id}")
def delete_god(god_id: int, db: Session = Depends(get_db)):
    db_god = crud.get_god(db, god_id)
    if not db_god:
        raise HTTPException(status_code=404, detail="God don't finded")
    crud.delete_god(db, db_god)
    return {"message": "God removed with sucess"}

@app.get("/gods-page", response_class=HTMLResponse)
def show_gods(request: Request, db: Session = Depends(get_db)):
    gods = crud.get_gods(db)
    return templates.TemplateResponse("gods.html", {"request": request, "gods": gods})


app.mount("/static", StaticFiles(directory="static"), name="static")
