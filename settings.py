"""File with settings and configs for the project"""
from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@127.0.0.1:5434/postgres",
)  # connect string for the real database
APP_PORT = env.int("APP_PORT", default=8080)

SECRET_KEY: str = env.str("SECRET_KEY", default="secret_key")
ALGORITHM: str = env.str("ALGORITHM", default="HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
SENTRY_URL: str = env.str("SENTRY_URL", default="https://66dba833d09692b645e909b0d5692814@o4508884051361792.ingest.us.sentry.io/4508884054966272")

TEST_DATABASE_URL = env.str(
    "TEST_DATABASE_URL",
    default="postgresql+asyncpg://postgres_test:postgres_test@127.0.0.1:5433/postgres_test",
)  # connect string for the test database


# APP_PORT = env.int("APP_PORT")

# SECRET_KEY: str = env.str("SECRET_KEY", default="secret_key")
# ALGORITHM: str = env.str("ALGORITHM", default="HS256")
# ACCESS_TOKEN_EXPIRE_MINUTES: int = env.int("ACCESS_TOKEN_EXPIRE_MINUTES", default=30)
# SENTRY_URL: str = env.str("SENTRY_URL")

# # test envs
# TEST_DATABASE_URL = env.str(
#     "TEST_DATABASE_URL",
#     default="postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5433/postgres_test",
# )  # connect string for the test database
