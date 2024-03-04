from environs import Env

env = Env()
env.read_env()

SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI")
