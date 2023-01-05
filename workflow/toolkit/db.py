import os

import psycopg2

from workflow.config import settings


def exec_sqlfile(filename):
    file = os.path.join(settings.script.sql_dir, filename)

    with psycopg2.connect(settings.app.postgres_uri) as conn:
        with conn.cursor() as curs:
            with open(file, "r") as fp:
                curs.execute(fp.read())
