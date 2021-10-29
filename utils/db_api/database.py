from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from models import Users, Password
import models

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
        select_user = select(Users).where(Users.tg_id == data)
        print(select_user)

#TEST
if __name__ == '__main__':
    db = Database('sqlite:///database.db')
    info = {'tg_id': 12345678}
    # db.add_user(data={'tg_id': '1244212234152314534615232451624567426355462'}, model=Users, filter_field="tg_id")
    # sel = db.select_usr(45311)

    # db.add_user(data=info, model=Users, filter_field="tg_id")
    # if not db.select_usr(info.values()):
    #     db.add_user(info, Users, filter_field="tg_id")
