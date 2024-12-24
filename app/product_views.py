from fastapi import Path, APIRouter
from typing import Annotated
from pydantic import EmailStr

router = APIRouter(prefix='/product', tags=['products_views'])


@router.get('/{product_id}')
def get_product(product_id: Annotated[int, Path(ge=1, le=999_999)]):
    return {
        'message': f'your product id: {product_id}'
    }


@router.get('/all/')
def get_all_product():
    return {
        'first': '1',
        'second': '2',
        'threes': '3'
    }


@router.post('/set/')
def new_product(email: EmailStr, num: int):
    return {
        'email': email,
        'num': num,
        'success': True,
    }
