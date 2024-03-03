from flask import Blueprint

from ..dto import Article

router = Blueprint("articles", __name__, url_prefix="/articles")


@router.get("/")
def list_articles() -> list[Article]:
    return "111"


@router.get("/<int:article_id>")
def get_article(article_id: int) -> Article:
    return "1111"
