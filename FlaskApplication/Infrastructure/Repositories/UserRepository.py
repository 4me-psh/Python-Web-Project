from werkzeug.security import generate_password_hash
import FlaskApplication.Infrastructure.DB as DB
from FlaskApplication.Domain.Models import User
from FlaskApplication.Domain.Models.User.IUserRepository import IUserRepository


class UserRepository(IUserRepository):

    def create_user(self, user: User):
        db = DB.get_db()
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                    (user.username, generate_password_hash(user.password)),)
        db.commit()
        return user

    def get_user_by_id(self, user_id: int):
        db = DB.get_db()
        return db.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()

    def get_all_users(self):
        db = DB.get_db()
        return db.execute("SELECT * FROM users").fetchall()

    def delete_user(self, user_id: int):
        db = DB.get_db()
        db.execute("DELETE FROM users WHERE id = ?", (user_id,))
        db.commit()

    def update_user(self, user: User):
        db = DB.get_db()
        db.execute("UPDATE users SET username = ?, password = ? WHERE id = ?", (user.username, generate_password_hash(user.password),user.user_id))
        db.commit()
        return user

    def get_user_by_username(self, username: str):
        db = DB.get_db()
        return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()