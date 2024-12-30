from sqlalchemy_utils import create_database, drop_database, database_exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model.base import Base

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"

# اگر دیتابیس وجود دارد
if database_exists(connection_string):
    # دیتابیس را حذف کن
    drop_database(connection_string)

# دیتابیس را از اول بساز
create_database(connection_string)

# مسئول اتصالات به دیتابیس
engine = create_engine(connection_string)



def get_session():
    # همه ی کلاسهایی که از base به ارث برده اند برایشان جدول بساز
    Base.metadata.create_all(engine)

    # مسئول انجام عملیات افزودن و ویرایش و حذف و جستجو در دیتابیس
    # به جای ما دستورات sql تولید می کند

    Session = sessionmaker(bind=engine)

    session = Session()
    return session