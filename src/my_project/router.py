from typing import Annotated

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from my_project.schemas import StatusResponse, UserCreate, UserResponse
from my_project.services import UserService

router = APIRouter()


def get_user_service(request: Request) -> UserService:
    return request.app.state.user_service


type UserServiceDep = Annotated[UserService, Depends(get_user_service)]


async def get_session(request: Request):
    session: async_sessionmaker[AsyncSession] = request.app.state.session
    async with session.begin() as sess:
        yield sess


type SessionDep = Annotated[AsyncSession, Depends(get_session)]


@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
)
async def signup(user: UserCreate, user_service: UserServiceDep, session: SessionDep):
    await user_service.signup(user, session)


@router.get("/users/{id}")
async def get_user_by_id(
    id: int, user_service: UserServiceDep, session: SessionDep
) -> UserResponse:
    user = await user_service.get_by_id(id, session)
    return UserResponse(
        name=user.name,
        email=user.email,
    )
