from fastapi import FastAPI
from .database import engine
from . import models
from .routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="🎬 Movie CRUD API",
    description="""

## 📝 Descrição Geral

API robusta para gerenciamento completo de filmes, oferecendo operações CRUD intuitivas e eficientes.

## 🚀 Recursos Principais

- **Criação de Filmes**: Adicione novos filmes com facilidade
- **Listagem Completa**: Recupere todos os filmes cadastrados
- **Busca Precisa**: Encontre filmes específicos por ID

## 🔧 Especificações Técnicas

### Tecnologias
- Framework: FastAPI
- ORM: SQLAlchemy
- Banco de Dados: SQLite

### Detalhes do Projeto
- **Versão da API**: 1.0.0
- **Tipo de Aplicação**: REST API
- **Compatibilidade**: Python 3.9+
""",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(router, prefix="/api/v1", tags=["Filmes"])