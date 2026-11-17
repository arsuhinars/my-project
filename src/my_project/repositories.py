from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from my_project.models import User


class UserRepository:
    def __init__(self): ...

    async def save(self, user: User, session: AsyncSession):
        session.add(user)
        await session.commit()

    async def get_by_id(self, id: int, session: AsyncSession) -> User | None:
        return await session.get(User, id)

    async def get_all(self, session: AsyncSession) -> list[User]:
        q = select(User).order_by(User.id)
        s = await session.execute(q)
        return list(s.scalars().all())
