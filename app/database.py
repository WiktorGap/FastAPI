from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:#####@localhost/fastapi'
# 'postgresql://<username>;<password>@<ip-address/hostname>/<database_name>'

enegine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=enegine)

Base = declarative_base()