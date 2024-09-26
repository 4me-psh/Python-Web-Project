from FlaskApplication.Domain.Models.User.IUserOrchestrator import IUserOrchestrator
from FlaskApplication.Domain.Models.User.IUserRepository import IUserRepository
from FlaskApplication.Domain.Models.User.User import User

class UserOrchestrator(IUserOrchestrator):
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def create_user(self, user: User):
        return self.repository.create_user(user)

    def get_all_users(self):
        return self.repository.get_all_users()

    def get_user_by_id(self, user_id: int):
        return self.repository.get_user_by_id(user_id)

    def update_user(self, user: User):
        return self.repository.update_user(user)

    def delete_user(self, user_id: int):
        deleted_user = self.get_user_by_id(user_id)
        self.repository.delete_user(user_id)
        return deleted_user

    def get_user_by_username(self, username: str):
        return self.repository.get_user_by_username(username)