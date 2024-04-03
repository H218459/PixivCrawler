import os

# mysql config
RELATION_DB_PWD = os.getenv("RELATION_DB_PWD", "123456")  # your relation db password
RELATION_DB_URL = f"mysql://root:{RELATION_DB_PWD}@localhost:3306/pixiv_crawler"
