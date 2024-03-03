from datetime import datetime

import pydantic


class Comment(pydantic.BaseModel):
    first_name: str
    last_name: str
    body: str
    created_at: str


class Article(pydantic.BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime
    updated_at: datetime
    comments: list[Comment]
