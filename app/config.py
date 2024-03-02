from environs import Env

env = Env()

# Читаем .env, если он есть
env.read_env()

HOST = env.str("HOST", "0.0.0.0")
PORT = env.int("PORT", 80)
DEBUG = env.bool("DEBUG", 0)
