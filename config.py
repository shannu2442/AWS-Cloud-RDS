SECRET_KEY = "cloud_rds_secret_key"

DB_USER = "admin"

DB_PASSWORD ="admin2424"

DB_HOST = "database-1.c5e84okugbgp.ap-south-1.rds.amazonaws.com"

DB_NAME = "employeedb"

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False