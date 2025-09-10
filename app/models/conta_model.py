from datetime import date, Decimal
from pydantic import BaseModel, Field

class ContaBase(BaseModel):
  apelido: str = Field(..., description="Apelido da conta")
  saldo_inicial: Decimal = Field(..., description="Saldo inicial da conta")
  outras_informacoes: Optional[str] = Field(None, description="Informações adicionais")
  codigo_tipo_conta: int = Field(..., description="Código do tipo de conta")
  codigo_usuario: int = Field(..., description="Código do usuário")
  codigo_icon: int = Field(..., description="Código do ícone do banco")