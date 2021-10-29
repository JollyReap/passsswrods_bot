from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

import models
from models import Users, Password


class Database:
    def __init__(self, db_url):
        engine = create_engine(db_url, pool_pre_ping=True)
        models.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)
        self.connection = engine.connect()

    def get_or_create(self, session, model, filter_field, data):
        instance = session.query(model).filter_by(**{filter_field: data[filter_field]}).first()
        if not instance:
            instance = model(**data)
        return instance

    def add_user(self, data, model, filter_field):
        session = self.maker()
        user = self.get_or_create(session, model, filter_field, data)

        session.add(user)
        try:
            session.commit()
        except Exception as err:
            print(err)
            session.rollback()
        finally:
            session.close()

    def select_usr(self, data):
        session = self.maker()
        select_user = select(Users).where(Users.tg_id == data)


if __name__ == '__main__':
    db = Database('sqlite:///database.db')
    get_info = {'tg_id': 1242121}

    db.add_user(data=get_info, model=Users, filter_field="tg_id")
    # db.select_usr(get_info)