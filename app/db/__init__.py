from flask_sqlalchemy import SQLAlchemy

from .base_model import BaseModel

db = SQLAlchemy(model_class=BaseModel)

