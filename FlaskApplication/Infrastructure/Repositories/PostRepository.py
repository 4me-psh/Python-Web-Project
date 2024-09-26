import FlaskApplication.Infrastructure.DB as DB
from FlaskApplication.Domain.Models import Post
from FlaskApplication.Domain.Models.Post.IPostRepository import IPostRepository


class PostRepository(IPostRepository):


    def create_post(self, post: Post):
        db = DB.get_db()
        db.execute('INSERT INTO posts (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (post.title, post.body, post.author_id))
        db.commit()
        return post

    def get_all_posts(self):
        db = DB.get_db()
        return db.execute('SELECT p.id, title, body, created, author_id, username'
        ' FROM posts p JOIN users u ON p.author_id = u.id'
        ' ORDER BY created DESC').fetchall()

    def get_post_by_id(self, post_id: int):
        db = DB.get_db()
        return db.execute('SELECT p.id, title, body, created, author_id, username'
                          ' FROM posts p JOIN users u ON p.author_id = u.id WHERE p.id = ?', (post_id,)).fetchone()

    def update_post(self, post: Post):
        db = DB.get_db()
        db.execute('UPDATE posts SET title = ?, body = ?'
                ' WHERE id = ?',
                (post.title, post.body, post.post_id))
        db.commit()
        return post

    def delete_post(self, post_id: int):
        db = DB.get_db()
        db.execute('DELETE FROM posts WHERE id = ?', (post_id,))
        db.commit()


