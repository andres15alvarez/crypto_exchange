from fastapi import HTTPException, status
from models.user import User


def is_same_user(user_request: User, user_db: User) -> bool:
    if user_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if user_db.id != user_request.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User has not permission."
        )
    return True
