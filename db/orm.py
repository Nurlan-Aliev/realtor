from sqlalchemy import select
from db.models import Users, Apartment
from db.database import async_session_factory


class AsyncORM:
    @staticmethod
    async def insert_user(session, id_tg, username):
        user = await AsyncORM.select_user(session, id_tg)
        if not user:

            user = Users(tg_id=id_tg, name=username)
            session.add(user)
            await session.flush()

    @staticmethod
    async def select_user(session, id_tg):
        user_db = select(Users).where(Users.tg_id == id_tg)
        result = await session.execute(user_db)
        user = result.scalars().all()
        return user

    @staticmethod
    async def insert_apartment(id_apartment, name):
        async with async_session_factory() as session:
            user = Apartment(id_apartment=id_apartment, name=name)
            session.add_all(user)
            await session.flush()
            await session.commit()
