from datetime import datetime

from pydantic import BaseModel as PydanticBaseModel, ConfigDict


class CommentBase(PydanticBaseModel):
    first_name: str
    last_name: str | None
    email: str
    body: str


class Comment(CommentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    article_id: int


class CommentCreate(CommentBase):
    pass


class ArticleBase(PydanticBaseModel):
    title: str
    image_url: str | None
    body: str


class Article(ArticleBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
    comments: list[Comment] = []


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(ArticleBase):
    title: str | None = None
    image_url: str | None = None
    body: str | None = None
