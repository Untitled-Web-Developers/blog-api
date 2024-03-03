from datetime import datetime

from sqlalchemy import VARCHAR, DATETIME, TEXT, BIGINT
from sqlalchemy.sql import func, text
from sqlalchemy.orm import Mapped, mapped_column

from ...app import db


class Article(db.Model):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    body: Mapped[str] = mapped_column(TEXT, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DATETIME, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DATETIME,
                                                 server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
