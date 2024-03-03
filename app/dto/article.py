from datetime import datetime

import pydantic


class Article(pydantic.BaseModel):
    id: int
    title: str
    body: str
    created_at: datetime
    updated_at: datetime
