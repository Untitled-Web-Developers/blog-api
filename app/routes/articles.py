from flask import Blueprint

from ..dto import Article, Comment
from ..db import Article

router = Blueprint("articles", __name__, url_prefix="/articles")


@router.get("/")
def get_articles() -> list[Article]:
    articles = Article.query.all()
    print(articles)
    return "ok"


@router.get("/<int:article_id>")
def get_article() -> Article:
    pass


@router.put("/")
def create_article() -> Article:
    pass


@router.post("/<int:article_id>")
def update_article(article_id: int) -> Article:
    pass


@router.delete("/<int:article_id>")
def delete_article(article_id: int) -> Article:
    pass


@router.put("/<int:article_id>/comments")
def add_comment(article_id: int) -> Comment:
    pass
