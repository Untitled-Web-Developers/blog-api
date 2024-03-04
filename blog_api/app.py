from fastapi import FastAPI

from .routes import api

app = FastAPI(
    title="blog-api",
    version="1.0.0",
    description="suka blyatb!",
    docs_url="/"
)

app.include_router(api.router)
