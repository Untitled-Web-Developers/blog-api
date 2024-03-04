import pydantic
from pydantic import Field


class AddArticleInput(pydantic.BaseModel):
    title: str = Field(max_length=255)
    body: str


class CommentResponse(pydantic.BaseModel):
    pass


class ArticleResponse(pydantic.BaseModel):
    pass
