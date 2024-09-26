import FlaskApplication.Infrastructure.DB as DB
from FlaskApplication.Domain.Models import Category
from FlaskApplication.Domain.Models.Category.ICategoryRepository import ICategoryRepository


class CategoryRepository(ICategoryRepository):

    def create_category(self, category: Category):
        db = DB.get_db()
        db.execute('INSERT INTO categories (name, description) VALUES (?, ?)',
                (category.name, category.description))
        db.commit()

    def get_all_categories(self):
        db = DB.get_db()
        return db.execute('SELECT * FROM categories').fetchall()

    def get_category_by_id(self, category: Category):
        db = DB.get_db()
        return db.execute('SELECT * FROM categories WHERE id = ?', (category.category_id,)).fetchone()

    def delete_category(self, category: Category):
        db = DB.get_db()
        db.execute('DELETE FROM categories WHERE id = ?', (category.category_id,))
        db.commit()

    def update_category(self, category: Category):
        db = DB.get_db()
        db.execute('UPDATE categories SET name = ?, description = ? WHERE id = ?',(category.name,category.description,category.category_id))
        db.commit()
