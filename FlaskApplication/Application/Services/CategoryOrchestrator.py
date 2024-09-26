from FlaskApplication.Domain.Models.Category.ICategoryOrchestrator import ICategoryOrchestrator
from FlaskApplication.Domain.Models.Category.ICategoryRepository import ICategoryRepository
from FlaskApplication.Domain.Models.Category.Category import Category


class CategoryOrchestrator(ICategoryOrchestrator):
    def __init__(self, repository: ICategoryRepository):
        self.repository = repository

    def create_category(self, category: Category):
        return self.repository.create_category(category)

    def get_all_categories(self):
        return self.repository.get_all_categories()

    def get_category_by_id(self, post_id: int):
        return self.repository.get_category_by_id(post_id)

    def update_category(self, category: Category):
        return self.repository.update_category(category)

    def delete_category(self, category_id: int):
        deleted_category = self.get_category_by_id(category_id)
        self.repository.delete_category(category_id)
        return deleted_category

