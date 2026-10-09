import os
import pyodbc


def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=sql-azure-etl-testing-dev.database.windows.net;"
        "DATABASE=sqldb-azure-etl-testing-dev;"
        "UID=sqladmin;"
        f"PWD={os.getenv('DB_PASSWORD')};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )
