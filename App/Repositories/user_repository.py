from sqlalchemy.orm import Session

from App.Repositories.base_repository import BaseRepository
from App.Http.requests.user_request import UserCreateRequest

from App.Models import User

class UserRepository(BaseRepository):

    _model = User
