from abc import ABC, abstractmethod
from typing import List
from .Post import Post

class IPostRepository(ABC):
    @abstractmethod
    def get_all_posts(self):
        pass

    @abstractmethod
    def get_post_by_id(self, post_id: int):
        pass

    @abstractmethod
    def create_post(self, post: Post):
        pass

    @abstractmethod
    def update_post(self, post: Post):
        pass

    @abstractmethod
    def delete_post(self, post_id: int):
        pass
