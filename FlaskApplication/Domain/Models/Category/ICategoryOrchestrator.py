from abc import ABC, abstractmethod
from typing import List
from .Category import Category


class ICategoryOrchestrator(ABC):
    @abstractmethod
    def get_all_categories(self):
        pass

    @abstractmethod
    def get_category_by_id(self, category_id: int):
        pass

    @abstractmethod
    def create_category(self, category: Category):
        pass

    @abstractmethod
    def update_category(self, category: Category):
        pass

    @abstractmethod
    def delete_category(self, category_id: int):
        pass