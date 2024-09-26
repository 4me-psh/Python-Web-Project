import FlaskApplication.Infrastructure.DB as DB
from FlaskApplication.Domain.Models import PostCategory


class PostCategoryRepository:

    def add_post_category(self, post_category: PostCategory):
        db = DB.get_db()
        db.execute('INSERT INTO post_categories (id_post, id_category)'
                ' VALUES (?, ?)',
                (post_category.post_id, post_category.category_id))
        db.commit()

    def get_post_category_by_id(self, post_category: PostCategory):
        db = DB.get_db()
        return db.execute('SELECT * FROM post_categories WHERE id_post = ?', (post_category.post_id,)).fetchone()

    def get_all_post_categories(self):
        db = DB.get_db()
        return db.execute('SELECT * FROM post_categories').fetchall()

    def delete_post_category(self, post_category: PostCategory):
        db = DB.get_db()
        db.execute('DELETE FROM post_categories WHERE id_post = ?', (post_category.post_id,))
        db.commit()


    def update_post_category(self, post_category: PostCategory):
        db = DB.get_db()
        db.execute('UPDATE post_categories SET id_post = ?, id_category = ?'
                   ' WHERE id = ?',
                   (post_category.post_id, post_category.category_id, post_category.id_post_category))
        db.commit()
