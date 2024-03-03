from datetime import datetime
from typing import List

from sqlalchemy import VARCHAR, DATETIME, TEXT, BIGINT, ForeignKey
from sqlalchemy.sql import func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..app import db


class Article(db.Model):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True, autoincrement=True, nullable=False)
    title: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    body: Mapped[str] = mapped_column(TEXT, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DATETIME, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DATETIME,
                                                 server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    comments: Mapped[List["Comment"]] = relationship(back_populates="article")


class Comment(db.Model):
    __tablename__ = "article_comments"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, unique=True, autoincrement=True, nullable=False)
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"), primary_key=True)
    first_name: Mapped[str] = mapped_column(VARCHAR(64), nullable=False)
    last_name: Mapped[str] = mapped_column(VARCHAR(64), nullable=False)
    body: Mapped[str] = mapped_column(TEXT, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DATETIME, server_default=func.now())

    article: Mapped["Article"] = relationship(back_populates="comments")
