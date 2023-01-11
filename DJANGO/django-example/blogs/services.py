from typing import OrderedDict, Protocol
from blogs import models
from django.db.models import QuerySet

from blogs.repositories import BlogRepositoriesInterface, BlogRepositoriesV1


class BlogServicesInterface(Protocol):
    repos: BlogRepositoriesInterface

    def create_blog(self, data: OrderedDict) -> models.Blog: ...

    def get_blog(self) -> QuerySet[models.Blog]: ...


class BlogServicesV1:
    repos: BlogRepositoriesInterface = BlogRepositoriesV1()

    def create_blog(self, data: OrderedDict) -> models.Blog:
        print("Create Blog in service layer")
        return self.repos.create_blog(data=data)

    def get_blog(self) -> QuerySet[models.Blog]:
        print("Get Blog in service layer")
        return self.repos.get_blog()
