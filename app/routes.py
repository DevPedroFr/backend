from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import get_db

router = APIRouter()

@router.post("/filmes", 
             response_model=schemas.Movie, 
             summary="Criar um novo filme", 
             description="Endpoint para adicionar um novo filme ao banco de dados")
def create_movie(
    movie: schemas.MovieCreate, 
    db: Session = Depends(get_db)
):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.get("/filmes", 
            response_model=List[schemas.Movie], 
            summary="Listar todos os filmes")
def read_movies(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    movies = db.query(models.Movie).offset(skip).limit(limit).all()
    return movies

@router.get("/filmes/{movie_id}", 
            response_model=schemas.Movie, 
            summary="Buscar filme por ID")
def read_movie(
    movie_id: int, 
    db: Session = Depends(get_db)
):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return movie
