from fastapi import HTTPException
from fastapi.responses import JSONResponse 

from app.utils.utils import *
from app.db.conexao_postgres import ConexaoPostgres

class ContaRepository:
    
  def __init__(self, db_connection: ConexaoPostgres):
    self.base = db_connection

  def get_icon_conta(self, icon: dict) -> dict:
    query = "SELECT CODIGO, NOME_BANCO, ICONE_SVG FROM BANCO_ICONE WHERE 1 = 1"

    params = {} 
    if 'codigo_icon' in icon and icon['codigo_icon']:
      query += " AND CODIGO = :nome_banco"
      params['codigo_icon'] = icon['codigo_icon']
    
    query += " ORDER BY CODIGO ASC"

    return self.base.select(query, params)

  def get_tipo_conta(self, user: dict) -> dict:
    query = "SELECT CODIGO, NOME_TIPO FROM TIPO_DE_CONTA WHERE 1 = 1"

    params = {} 
    if 'nome_tipo' in user and user['nome_tipo']:
      query += " AND NOME_TIPO = :nome_tipo"
      params['nome_tipo'] = user['nome_tipo']
    
    query += " ORDER BY NOME_TIPO ASC"
    
    return self.base.select(query, params)

  def select_conta(self, info: dict) -> dict:

    user = UsuarioRepository().get_usuarios({'nome': info['nome']})
    if not user:
      raise HTTPException(status_code=404, detail="Usuário não encontrado")
    info['codigo_usuario'] = user[0]['codigo']

    query = """
      SELECT
        C.CODIGO,
        C.APELIDO,
        C.SALDO_INICIAL,
        C.DATA_SALDO_INICIAL,
        C.OUTRAS_INFORMACOES,
        T.NOME_TIPO AS NOME_TIPO_CONTA,
        U.NOME AS NOME_USUARIO,
        B.NOME_BANCO,
        B.ICONE_SVG
      FROM CONTA C
      JOIN TIPO_DE_CONTA T ON C.CODIGO_TIPO_CONTA = T.CODIGO
      JOIN USUARIO U ON C.CODIGO_USUARIO = U.CODIGO
      JOIN BANCO_ICONE B ON C.CODIGO_ICON = B.CODIGO
      WHERE 1 = 1    
    """
    params = {}

    if 'codigo' in info and info['codigo']:
      query += " AND C.CODIGO = :codigo"
      params['codigo'] = info['codigo']

    if 'apelido' in info and info['apelido']:
      query += " AND C.APELIDO = :apelido"
      params['apelido'] = info['apelido']

    if 'banco' in info and info['banco']:
      query += " AND B.NOME_BANCO = :banco"
      params['banco'] = info['banco']

    if 'saldo_inicial' in info and info['saldo_inicial']:
      query += " AND C.SALDO_INICIAL = :saldo_inicial"
      params['saldo_inicial'] = info['saldo_inicial']

    if 'data_saldo_inicial' in info and info['data_saldo_inicial']:
      query += " AND C.DATA_SALDO_INICIAL = :data_saldo_inicial"
      params['data_saldo_inicial'] = info['data_saldo_inicial']
    
    if 'outras_informacoes' in info and info['outras_informacoes']:
      query += " AND C.OUTRAS_INFORMACOES = :outras_informacoes"
      params['outras_informacoes'] = info['outras_informacoes']
    
    if 'codigo_tipo_conta' in info and info['codigo_tipo_conta']:
      query += " AND C.CODIGO_TIPO_CONTA = :codigo_tipo_conta"
      params['codigo_tipo_conta'] = info['codigo_tipo_conta']
    
    if 'codigo_usuario' in info and info['codigo_usuario']:
      query += " AND C.CODIGO_USUARIO = :codigo_usuario"
      params['codigo_usuario'] = info['codigo_usuario']
    
    query += " ORDER BY C.CODIGO ASC"
    return self.base.select(query, params)