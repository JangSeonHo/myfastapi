from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL  = sqlite:///./myapi.db
SQLALCHEMY_DATABASE_URL = "postgresql://dbmasteruser:!1q2w3e4r@ls-0580edce363707b39b9d0715e648dd26ca209f78.cy9veup6x4sg.ap-northeast-2.rds.amazonaws.com/fastapi_sunny"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


#engine = create_engine(
#    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
#)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
