from fastapi import HTTPException
from fastapi.responses import JSONResponse 

from app.utils.utils import *
from app.db.conexao_postgres import ConexaoPostgres

class UsuarioRepository:
    
  def __init__(self, db_connection: ConexaoPostgres):
    self.base = db_connection

  def get_usuarios(self, user: dict) -> dict:
    """
    Retorna todos os usuários.
    """
    query = "SELECT CODIGO, NOME, EMAIL from USUARIO WHERE 1 = 1"


    params = {} 
    if 'nome' in user and user['nome']:
      query += " AND nome = :nome"
      params['nome'] = user['nome']
    
    query += " ORDER BY nome ASC"
    
    return self.base.select(query, params)

  def cadastra_usuario(self, info: dict) -> dict:
    user = self.get_usuarios({'email': info['email_usuario']})

    if user:
      raise HTTPException(status_code=400, detail="Email já cadastrado")

    query = "INSERT INTO USUARIO (NOME, EMAIL, SENHA) VALUES (:nome, :email, :senha)"
    params = {
      'nome': info['nome_usuario'],
      'email': info['email_usuario'],
      'senha': info['senha_usuario']
    }
    ret = self.base.insert(query, params)

    sucesso = ret.get('success') and ret.get('rows_affected') == 1

    return {
      'codigo': 1 if sucesso else 99,
      'message': (
        f"Usuário '{info['nome_usuario']}' cadastrado com sucesso."
        if sucesso else ret.get('error', f"Erro ao cadastrar usuário: '{info['nome_usuario']}'.")
      )
    }

  def alter_usuario(self, info: dict) -> dict:
    user = self.get_usuarios({'email': info['email_usuario']})

    if not user:
      raise HTTPException(status_code=400, detail="Email não cadastrado")
    
    query = "UPDATE USUARIO SET SENHA = :senha WHERE CODIGO = :codigo"
    params = {
      'senha': info['senha_usuario'],
      'codigo': user[0]['codigo']
    }
    ret = self.base.update(query, params)

    sucesso = ret.get('success') and ret.get('rows_affected') == 1

    return {
      'codigo': 1 if sucesso else 99,
      'message': (
        f"Usuário '{info['nome_usuario']}' alterado com sucesso."
        if sucesso else ret.get('error', f"Erro ao alterar usuário: '{info['nome_usuario']}'.")
      )
    }