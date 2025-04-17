from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Produto(BaseModel):
    id: int
    nome: str
    preco: float

# Banco de dados falso
banco_de_produtos = []

@app.post("/produtos/", response_model=Produto)
def criar_produto(produto: Produto):
    banco_de_produtos.append(produto)
    return produto

@app.get("/produtos/", response_model=List[Produto])
def listar_produtos():
    return banco_de_produtos

@app.get("/produtos/{produto_id}", response_model=Produto)
def pegar_produto(produto_id: int):
    for produto in banco_de_produtos:
        if produto.id == produto_id:
            return produto
    return {"erro": "Produto não encontrado"}

@app.put("/produtos/{produto_id}", response_model=Produto)
def atualizar_produto(produto_id: int, produto_atualizado: Produto):
    for i, produto in enumerate(banco_de_produtos):
        if produto.id == produto_id:
            banco_de_produtos[i] = produto_atualizado
            return produto_atualizado
    return {"erro": "Produto não encontrado"}

@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int):
    for produto in banco_de_produtos:
        if produto.id == produto_id:
            banco_de_produtos.remove(produto)
            return {"mensagem": "Produto deletado"}
    return {"erro": "Produto não encontrado"}
