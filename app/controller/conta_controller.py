from fastapi import APIRouter, Body, HTTPException, Depends

from app.db.conexao_postgres import ConexaoPostgres
from app.repository.conta_repository import ContaRepository

conta_controller = APIRouter()

def get_db_connection():
  return ConexaoPostgres() 
  
def get_conta_repository(db: ConexaoPostgres = Depends(get_db_connection)):
  return ContaRepository(db)

@conta_controller.get(
  "/tipos-conta",
  tags=["Conta"],
  summary="Tipos de Conta",
  description="""
  Retorna todos os tipos de conta.
  """,
)
def get_tipo_conta(conta_repo: ContaRepository = Depends(get_conta_repository)):
  return conta_repo.get_tipo_conta({})

@conta_controller.get(
  "/icon-conta",
  tags=["Conta"],
  summary="Icones de Conta",
  description="""
  Retorna todos os icones de conta.
  """,
)
def get_icon_conta(conta_repo: ContaRepository = Depends(get_conta_repository)):
  ret = conta_repo.get_icon_conta({})

  resultado = [
    {
      "codigo": conta["codigo"],
      "nome_banco": conta["nome_banco"]
    }
    for conta in ret
  ]

  return resultado

@conta_controller.get(
  "/contas",
  tags=["Conta"],
  summary="Contas",
  description="""
  Retorna todas as contas.
  
  """,

)
def get_contas(conta_repo: ContaRepository = Depends(get_conta_repository)):
  ret = conta_repo.get_contas({})

  resultado = [
    {
      "codigo": conta["codigo"],
      "apelido": conta["apelido"],
      "saldo_inicial": conta["saldo_inicial"],
      "data_saldo_inicial": conta["data_saldo_inicial"],
      "outras_informacoes": conta["outras_informacoes"],
      "nome_tipo": conta["nome_tipo"],
      "nome_usuario": conta["nome_usuario"],
      "nome_banco": conta["nome_banco"],
      "icone_svg": conta["icone_svg"]
    }
    for conta in ret
  ]

  return resultado