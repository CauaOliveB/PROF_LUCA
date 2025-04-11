'''
    *-------------------------------------------------------------------------------*
    |                                  FastAPI                                      |
    |   Date: 28/03/2025                                                            |
    |   Instructor(s): Wilson Ferreira / Luca Dias                                  |
    |   Aula 1 : CRUD                                                               |
    |                                                                               |
    * ------------------------------------------------------------------------------*

'''

from fastapi import FastAPI, HTTPException, status, Response, Depends
from typing import Optional, Any
from Aula.ew import Pato


app = FastAPI(title="API de Patos da DS14", version="0.0.1", description="API de Patos desenvolvido pelos alunos da DS14")

def fake_db():
    try:
        print("Conectando no Bmanco de Dados")
    finally:
        print("Fechando a conexão com o Banco de Dados")

patos = {
    1:{
    "nome" : "Luca",
    "especie" : "Pato Canadense",
    "idade" : 25,
    "cor" : "Verde e Cinza ",
    "foto" : "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flickr.com%2Fphotos%2Fjcspl%2F547458037&psig=AOvVaw3H3sF2afQ5cMDKx2gYHkf1&ust=1743248290602000&source=images&cd=vfe&opi=89978449&ved=2ahUKEwio-JmK2KyMAxUzuJUCHX-gC7wQjRx6BAgAEBk"
},
    2:{
    "nome" : "Perry",
    "especie" : "Ornitorinco",
    "idade" : 5,
    "cor" : "Turquesa",
    "foto" : "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2Fphineasandferb%2Fcomments%2F19dxne0%2Frealistic_perry_the_platypus%2F&psig=AOvVaw2fbIBYwyO-JjeURTPCAl5Q&ust=1743248655997000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPjr17rZrIwDFQAAAAAdAAAAABAE" 
    },
}

@app.get("/")
async def raiz():
    return {"mensagem" : "Vai Corinthias"}

@app.get("/patos", description="Retorna todos os patos que estão no banco", summary="Retorna todos os Patos")
async def get_patos(db : Any = Depends(fake_db)):
    return patos

@app.get("/patos/{patos_id}", description="Retorna o Pato selecionado pelo ID e trata o erro caso o ID não esteja cadastrado", summary="Retorna um Pato especifíco pelo ID e trata o Pato não tenaha sido cadastrado")
async def get_pato(pato_id : int):
    try:
        pato = patos[pato_id]
        return pato
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe nenhum pato com este ID {pato_id}")
    

@app.post("/patos", status_code=status.HTTP_201_CREATED)
async def post_pato(pato : Optional[Pato] = None):
    next_id = len(patos) + 1
    patos[next_id] = pato
    del pato.id
    return pato    

@app.put("/patos/{pato_id}", status_code=status.HTTP_202_ACCEPTED, description="")
async def put_pato(pato_id : int, pato : Pato):
    if pato_id in patos:
        patos[pato_id] = pato
        pato.id = pato_id
        del pato.id
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe nenhum pato com este ID {pato_id}")

@app.delete("/patos/{pato_id}")
async def delete_patos(pato_id : int):
    if pato_id in patos: 
        del patos[pato_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe nenhum pato com este ID {pato_id}")


@app.get("/calculadora")
async def calcular( num1 : int, num2 : int):
    soma = num1 + num2
    return soma

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
    