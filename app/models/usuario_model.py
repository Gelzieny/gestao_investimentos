from typing import Optional
from pydantic import BaseModel, Field

class UsuarioModel(BaseModel):
  nome_usuario: Optional[str] = Field(default=None, description="Nome do usuário")
  email_usuario: Optional[str] = Field(default=None, description="Email do usuário")


class UsuarioCad(UsuarioModel):
  nome_usuario: str = Field(default=None, description="Nome do usuário")
  email_usuario: str = Field(default=None, description="Email do usuário")
  senha_usuario: str = Field(..., description="Senha do usuário") 

class UsuarioAlter(UsuarioModel):
  nome_usuario: Optional[str] = Field(default=None, description="Nome do usuário")
  email_usuario: Optional[str] = Field(default=None, description="Email do usuário")
  senha_usuario: Optional[str] = Field(default=None, description="Senha do usuário")