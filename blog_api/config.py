from environs import Env

env = Env()
env.read_env()

SQLALCHEMY_DATABASE_URL = env.str("SQLALCHEMY_DATABASE_URL")
