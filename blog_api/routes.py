from flask import Blueprint, request, jsonify
from flask_pydantic import validate

from .db import db
from .db.models import Article
from .dto import AddArticleInput

router = Blueprint("main", __name__)


@router.route("/")
def index() -> str:
    return "<h1>Welcome to blog-api</h1><span>made with <3 by untitled.arts</span>"


@router.get("/articles")
@validate()
def get_all_articles():
    page = request.args.get("page", 0, int)
    limit = request.args.get("limit", 0, int)

    if page and limit:
        articles = Article.query.order_by(Article.created_at.desc()).paginate(page=page, per_page=limit)
    elif limit:
        articles = Article.query.order_by(Article.created_at.desc()).limit(limit).all()
    else:
        articles = Article.query.order_by(Article.created_at.desc()).all()

    return [
        {
            "id": article.id,
            "title": article.title,
            "body": article.body,
            "updated_at": article.updated_at,
            "created_at": article.created_at,
            "comments": [
                {
                    "id": comment.id,
                    "first_name": comment.first_name,
                    "last_name": comment.last_name,
                    "body": comment.body,
                    "created_at": comment.created_at
                }
                for comment in article.comments
            ]
        }
        for article in articles
    ]


@router.get("/articles/<int:article_id>")
def get_article(article_id: int):
    article = Article.query.filter(Article.id == article_id).first()

    if not article:
        return {"error": {"text": "An article with this ID could not be found!"}}, 404

    return {
        "id": article.id,
        "title": article.title,
        "body": article.body,
        "updated_at": article.updated_at,
        "created_at": article.created_at,
        "comments": [
            {
                "id": comment.id,
                "first_name": comment.first_name,
                "last_name": comment.last_name,
                "body": comment.body,
                "created_at": comment.created_at
            }
            for comment in article.comments
        ]
    }


@router.put("/articles")
@validate()
def add_article(body: AddArticleInput) -> dict:
    article = Article(title=body.title, body=body.body)
    db.session.add(article)
    db.session.commit()
    db.session.refresh(article)
    return {
        "id": article.id,
        "title": article.title,
        "body": article.body,
        "updated_at": article.updated_at,
        "created_at": article.created_at,
        "comments": [
            {
                "id": comment.id,
                "first_name": comment.first_name,
                "last_name": comment.last_name,
                "body": comment.body,
                "created_at": comment.created_at
            }
            for comment in article.comments
        ]
    }


@router.delete("/articles/<int:article_id>")
def delete_article(article_id: int):
    return None, 204
