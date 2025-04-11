from fastapi import FastAPI, HTTPException, status
from typing import Optional, Any, Dict
from model import Gods


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




app = FastAPI()

gods_database: Dict[int, dict] ={
    1: {
        "name" : "Hécate",
        "nativename" : "Ἑκάτη Hekátē",
        "atribuition" : ["Moon, Magic, Sorcery, Crossway"],
        "simbols" : ["Keys, Crossways, Dagger "],
        "household" : ["Underworld, Olympus, Sea"],
        "foto" : "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.deviantart.com%2Fnekrosketcher%2Fart%2FHecate-Age-of-mythology-retold-1121145361&psig=AOvVaw0u63RYBvMMqC8SdmAfGJ19&ust=1743255577034000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOD9haLzrIwDFQAAAAAdAAAAABAE"
    },
    2: {
        "name" : "Dioniso",
        "nativename" : "Διόνυσος",
        "atribuition" : ["Vital Cycles, Partys, Wine, Theater, Insanity, Religious Rites"],
        "simbols" : ["Thyrsus, Vine"],
        "household" : ["Olympus"],
        "foto" : "https://www.google.com/url?sa=i&url=https%3A%2F%2Fbr.freepik.com%2Fimagem-ia-premium%2Fdeus-do-deus-grego-dionisio-com-ia-generativa-de-vinho-e-frutas_44478862.htm&psig=AOvVaw3M1EEfxOK8SWFNeXWjrFG7&ust=1743256039592000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMjfvID1rIwDFQAAAAAdAAAAABAm"
    },
    3: {
        "name" : "Atena",
        "nativename" : "Αθηνά",
        "atribuition" : ["Battle strategies, Civilization, Wisdom, Arts, Justice, Skill, Inspiration, Strength and Mathematics"],
        "simbols" : ["Owl, Olive Trees, Snakes"],
        "household" : ["Olympus"],
        "foto" : "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.todamateria.com.br%2Fdeusa-grega-atena%2F&psig=AOvVaw1jvYRSBfh3uuOlopi90FwR&ust=1743256213847000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMi2ja32rIwDFQAAAAAdAAAAABAE"
    },
     4: {
        "name" : "Afrodite",
        "nativename" : "Αφροδίτη",
        "atribuition" : ["Love, Beauty and Sexuality"],
        "simbols" : ["Swan, Rose, Pomegranate, Lime Tree, Pearls, Jewelry"],
        "household" : ["Olympus"],
        "foto" : "https://www.google.com/url?sa=i&url=https%3A%2F%2Fcapeiaarraiana.pt%2F2016%2F02%2F16%2Fafrodite%2F&psig=AOvVaw0-namcT0d9ptlKcflSTD2E&ust=1743256311548000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIC96oL2rIwDFQAAAAAdAAAAABA6"
    },
    }

@app.get('/Gods', description="Retorna os deuses cadastrados")
async def get_gods():
    return gods_database

@app.get('/Gods/{god_id}', description="Retorna o Deus pelo ID trata o erro caso o ID não esteja cadastrado", summary="Retorna um Deus especifíco pelo ID e trata o erro caso o ID nção tenha sido cadastrado ")
async def get_god(god_id : int):
  if god_id not in gods_database:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe nenhum deus com este ID {god_id}")
  return gods_database[god_id]

 
@app.post("/Gods", status_code=status.HTTP_201_CREATED)
async def post_god(god : Gods):
    next_id = max(gods_database.keys(), default=0) + 1
    gods_database[next_id] = god
    return gods_database[next_id]

@app.put("/Gods/{god_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_god(god_id : int, god : Gods):
   if god_id not in gods_database:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=" God not finded.;")
   gods_database[god_id] = god,
   return {"msg": "God updated with sucess", "god": god},

@app.delete("/gods/{god_id}", status_code=status.HTTP_200_OK)
async def delete_god(god_id: int):
    if god_id not in gods_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="God not finded.")
    god_deleted = gods_database[god_id]
    del gods_database[god_id]
    return {"message": "God removed with sucess", "god": god_deleted}
