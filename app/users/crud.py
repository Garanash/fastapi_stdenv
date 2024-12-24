from .schemas import CreateUser

"""
Create
Read
Update
Delete
"""

def create_new_user(user_in: CreateUser):
    return {
        'success': True,
        'user': user_in.email
    }