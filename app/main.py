from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.conexao_postgres import ConexaoPostgres
from app.controller.conta_controller import conta_controller
from app.controller.usuario_controller import usuario_controller

app = FastAPI(
  title="Gestão de Investimentos",
  description=(
    "API para gerenciamento de investimentos pessoais. "
    "Permite cadastro de usuários, registro de investimentos, "
    "consultas de histórico e autenticação segura."
  ),
  version="1.0.0"
)

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
  return RedirectResponse(url="/docs")


@app.get(
  "/teste",
  tags=["Utilitários"],
  summary="Verifica se a API está funcionando"
)
async def teste():
  """
  Endpoint para checar o status da API.

  Retorna um objeto JSON com a confirmação de que o sistema está no ar.
  """
  conexao = ConexaoPostgres()
  conexao.teste()
  
  return {"status": "success", "resultado": "Teste bem-sucedido"}

app.include_router(usuario_controller)
app.include_router(conta_controller)