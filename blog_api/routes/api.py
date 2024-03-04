from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import schemas, crud
from ..db.engine import make_session

articles = APIRouter()


@articles.put('', response_model=schemas.Article)
async def add_article(article: schemas.ArticleCreate, db: AsyncSession = Depends(make_session)):
    article = await crud.create_article(db, article)
    return article


@articles.get('', response_model=List[schemas.Article])
async def get_all_articles(limit: int = 0, offset: int = 0, db: AsyncSession = Depends(make_session)):
    article_list = await crud.get_articles(db, limit, offset)
    return article_list


@articles.get('/{article_id}', response_model=schemas.Article)
async def get_article(article_id: int, db: AsyncSession = Depends(make_session)):
    article = await crud.get_article(db, article_id)
    if not article:
        raise HTTPException(404, "Article not found!")
    return article


@articles.post('/{article_id}')
async def edit_article(article_id: int, new_article: schemas.ArticleUpdate, db: AsyncSession = Depends(make_session)):
    article = await crud.update_article(db, article_id, new_article)
    if not article:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Failed to update article (NOT_EXIST OR INTEGRITY ERROR)")
    return article


@articles.delete('/{article_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(article_id: int, db: AsyncSession = Depends(make_session)):
    ok = await crud.delete_article(db, article_id)
    if not ok:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Failed to remove article (NOT_EXIST OR INTEGRITY ERROR)")
    return


@articles.put('/{article_id}/comments')
async def add_comment(article_id: int, comment: schemas.CommentCreate, db: AsyncSession = Depends(make_session)):
    article = await crud.get_article(db, article_id)
    if not article:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Article not found!")

    comment = await crud.create_comment(db, article_id, comment)
    return comment


@articles.get('/{article_id}/comments')
async def get_comments(article_id: int, limit: int = 0, offset: int = 0, db: AsyncSession = Depends(make_session)):
    article = await crud.get_article(db, article_id)
    if not article:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Article not found!")

    comment = await crud.get_comments(db, article_id, limit, offset)
    return comment


router = APIRouter()
router.include_router(articles, prefix="/articles", tags=["Articles"])
