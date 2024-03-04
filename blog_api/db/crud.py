from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas
from .models import Article, Comment


async def get_article(db: AsyncSession, article_id: int) -> Article | None:
    statement = select(Article).where(Article.id == article_id).limit(1)
    result = await db.execute(statement)
    return result.scalar_one_or_none()


async def get_articles(db: AsyncSession, limit: int = 0, offset: int = 0) -> list[Article]:
    statement = select(Article).order_by(Article.created_at.desc()).offset(offset)
    if limit:
        statement = statement.limit(limit)

    result = await db.execute(statement)
    return list(result.scalars().all())


async def create_article(db: AsyncSession, article: schemas.ArticleCreate) -> Article:
    new_article = Article(**article.model_dump())
    db.add(new_article)
    await db.commit()
    await db.refresh(new_article)
    return new_article


async def update_article(db: AsyncSession, article_id: int, new_article: schemas.ArticleUpdate) -> Article | None:
    article = await get_article(db, article_id)
    if not article:
        return None
    for k, v in new_article.model_dump(exclude_unset=True).items():
        setattr(article, k, v)
    db.add(article)
    try:
        await db.commit()
    except IntegrityError:
        return None
    await db.refresh(article)
    return article


async def delete_article(db: AsyncSession, article_id: int) -> bool:
    article = await get_article(db, article_id)
    if not article:
        return True
    await db.delete(article)
    try:
        await db.commit()
        return True
    except IntegrityError:
        return False


async def create_comment(db: AsyncSession, article_id: int, comment: schemas.CommentCreate) -> Comment | None:
    new_comment = Comment(article_id=article_id, **comment.model_dump())
    article = await get_article(db, article_id)

    if not article:
        return None

    db.add(new_comment)
    await db.commit()
    await db.refresh(new_comment)

    return new_comment


async def get_comments(db: AsyncSession, article_id: int, limit: int = 0, offset: int = 0) -> list[Comment]:
    statement = (select(Comment)
                 .where(Comment.article_id == article_id)
                 .order_by(Comment.created_at.desc())
                 .offset(offset))
    if limit:
        statement = statement.limit(limit)

    result = await db.execute(statement)
    return list(result.scalars().all())
