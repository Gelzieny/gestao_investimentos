from fastapi import APIRouter, Body, HTTPException, Depends

from app.utils.utils import retira_vazios
from app.utils.security import hash_password
from app.db.conexao_postgres import ConexaoPostgres
from app.repository.usuario_repository import UsuarioRepository
from app.models.usuario_model import UsuarioModel, UsuarioCad, UsuarioAlter

usuario_controller = APIRouter()

def get_db_connection():
  return ConexaoPostgres() 
  
def get_user_repository(db: ConexaoPostgres = Depends(get_db_connection)):
  return UsuarioRepository(db)

@usuario_controller.post(
    "/list-usuario",
    tags=["Usuário"],
    summary="Listar usuários",
    description="""
    Retorna uma lista de usuários filtrando opcionalmente por nome.

    ### Regras:
    - O campo nome usuário e opcional.
    
      ### Exemplo de requisição:
      ```json
      {
        "nome_usuario": "Teste",
      }
      ```	

    ### Funcionalidade
    Este endpoint consulta a base de dados e retorna todos os usuários registrados, incluindo:

    - **Nome usuário**
    - **E-mail**

    ### Respostas:
    - **200 OK**: Lista de usuários retornada com sucesso
    - **500 Internal Server Error**: Falha ao buscar usuários
    """,
)
async def list_usuario(user: UsuarioModel = Body(), repo: UsuarioRepository = Depends(get_user_repository)):
  """
    Retorna uma lista de usuários com base no nome fornecido (opcional).

    - **nome_usuario**: nome do usuário (opcional)
  """
  
  return repo.get_usuarios(retira_vazios({'nome': user.nome_usuario}))

@usuario_controller.post(
    "/create-usuario",
    tags=["Usuário"],
    summary="Criar novo usuário",
    description="""
    Cria um novo usuário no sistema com nome e aplicação vinculada.

    ### Regras:
    - Ambos os campos são obrigatórios.

        ### Exemplo de requisição:
        ```json
        {
        "nome_usuario": "Teste,
        "email": "teste@gmail.com",
        "senha_usuario": "12345rtgff"
        }
        ```

    ### Respostas:
    - **201 Created**: Usuário criado com sucesso
    - **400 Bad Request**: Dados inválidos
    - **500 Internal Server Error**: Falha ao criar o usuário
    """,
)
async def create_usuario(user: UsuarioCad = Body(), repo: UsuarioRepository = Depends(get_user_repository)):
    """
      Cria um novo usuário no sistema.

      - **nome**: Nome usuário
      - **email*: email unicos
      - **senha**: senha do usuário
    """
    
    hashed_pw = hash_password(user.senha_usuario)
    
    
    param = {
      'nome_usuario': user.nome_usuario,
      'email_usuario': user.email_usuario,
      "senha_usuario": hashed_pw
    }

    campos_vazios = [campo for campo, valor in param.items() if not valor or str(valor).strip() == '']

    if campos_vazios:
      raise HTTPException(
        status_code=400,
        detail=f"Os seguintes campos são obrigatórios e estão vazios: {', '.join(campos_vazios)}"
      )

    return repo.cadastra_usuario(param)


# @usuario_controller.post(
#     "/alter-usuario",
#     tags=["Usuário"],
#     summary="Alterar usuário",
#     description="""
#     Altera o usuário no sistema com nome e aplicação vinculada.

#     ### Regras:
#     - Ambos os campos são opcionais.

#         ### Exemplo de requisição:
#         ```json
#         {
#         "nome_usuario": "Teste,
#         "email": "teste@gmail.com",
#         "senha_usuario": "12345rtgff"
#         }
#         ```
#     ### Funcionalidade
#     Este endpoint altera o usuário no sistema com nome e aplicação vinculada.

#     - **Nome usuário**
#     - **E-mail**

#     ### Respostas:
#     - **201 OK**: Usuário alterado com sucesso
#     - **400 Bad Request**: Dados inválidos
#     - **500 Internal Server Error**: Falha ao alterar o usuário
#     """,
# )
# async def alter_usuario(user: UsuarioAlter = Body(), repo: UsuarioRepository = Depends(get_user_repository)):
#     """
#       Altera o usuário no sistema.

#       - **nome**: Nome usuário
#       - **email*: email unicos
#       - **senha**: senha do usuário
#     """
#     param = {
#       'email_usuario': user.email_usuario,
#       "senha_usuario": user.senha_usuario
#     }

#     campos_vazios = [campo for campo, valor in param.items() if not valor or str(valor).strip() == '']

#     if campos_vazios:
#       raise HTTPException(
#         status_code=400,
#         detail=f"Os seguintes campos são obrigatórios e estão vazios: {', '.join(campos_vazios)}"
#       )
    
#     hashed_pw = hash_password(user.senha_usuario)
#     param['senha_usuario'] = hashed_pw

#     return repo.alter_usuario(param)

