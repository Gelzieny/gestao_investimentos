from pydantic import BaseModel, Field

class PermsResponse(BaseModel):
  mensagem: str = Field(description="Exemplo de Mensagem", default='Valor Default')
  cod_retorno: int = Field(description="Exemplo de Cod Retorno", default=0)
  tipo_retorno: str = Field(description="Exemplo de Tipo Retorno", default='success')
