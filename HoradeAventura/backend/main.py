from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Reinos
@app.post("/reinos/", response_model=schemas.Reino)
def criar_reino(reino: schemas.ReinoCreate, db: Session = Depends(get_db)):
    db_reino = models.Reino(nome=reino.nome)
    db.add(db_reino)
    db.commit()
    db.refresh(db_reino)
    return db_reino

@app.get("/reinos/", response_model=list[schemas.Reino])
def listar_reinos(db: Session = Depends(get_db)):
    return db.query(models.Reino).all()

# CRUD Personagens
@app.post("/personagens/", response_model=schemas.Personagem)
def criar_personagem(p: schemas.PersonagemCreate, db: Session = Depends(get_db)):
    db_p = models.Personagem(**p.dict())
    db.add(db_p)
    db.commit()
    db.refresh(db_p)
    return db_p

@app.get("/personagens/", response_model=list[schemas.Personagem])
def listar_personagens(db: Session = Depends(get_db)):
    return db.query(models.Personagem).all()

@app.delete("/personagens/{id}", status_code=204)
def deletar_personagem(id: int, db: Session = Depends(get_db)):
    p = db.query(models.Personagem).get(id)
    if not p:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    db.delete(p)
    db.commit()
    return
