from .schemas import CreateUser
from .crud import create_new_user
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users_views"])


@router.post("/create_user")
def create_user(new_user: CreateUser):
    return create_new_user(user_in=new_user)
