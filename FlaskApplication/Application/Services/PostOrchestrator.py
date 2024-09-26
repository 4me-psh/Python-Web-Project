from FlaskApplication.Domain.Models.Post.IPostOrchestrator import IPostOrchestrator
from FlaskApplication.Domain.Models.Post.IPostRepository import IPostRepository
from FlaskApplication.Domain.Models.Post.Post import Post


class PostOrchestrator(IPostOrchestrator):
    def __init__(self, repository: IPostRepository):
        self.repository = repository

    def create_post(self, post: Post):
        return self.repository.create_post(post)

    def get_all_posts(self):
        return self.repository.get_all_posts()

    def get_post_by_id(self, post_id: int):
        return self.repository.get_post_by_id(post_id)

    def update_post(self, post: Post):
        return self.repository.update_post(post)

    def delete_post(self, post_id: int):
        deleted_post = self.get_post_by_id(post_id)
        self.repository.delete_post(post_id)
        return deleted_post

