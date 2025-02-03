import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# Tải các biến môi trường từ tệp .env
load_dotenv()

# Lấy chuỗi kết nối từ biến môi trường
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Tạo engine kết nối đến cơ sở dữ liệu
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Tạo session để giao tiếp với cơ sở dữ liệu
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tạo Base để định nghĩa các bảng dữ liệu
Base = declarative_base()

# Hàm lấy session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
