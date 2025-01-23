from pydantic import BaseModel, Field
from typing import Optional

class MovieBase(BaseModel):
    titulo: str = Field(
        ..., 
        min_length=1, 
        max_length=100, 
        description="Título do filme",
        example="Interestelar"
    )
    genero: str = Field(
        ..., 
        min_length=1, 
        max_length=50, 
        description="Gênero do filme",
        example="Ficção Científica"
    )
    ano: int = Field(
        ..., 
        gt=1800, 
        lt=2100, 
        description="Ano de lançamento do filme",
        example=2014
    )

class MovieCreate(MovieBase):
    """Schema para criação de um novo filme"""
    pass

class Movie(MovieBase):
    """Schema para representação completa de um filme"""
    id: int = Field(
        ..., 
        description="Identificador único do filme",
        example=1
    )

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "titulo": "Interestelar",
                "genero": "Ficção Científica", 
                "ano": 2014
            }
        }
