from typing import OrderedDict, Protocol
from blogs import models
from django.db.models import QuerySet


class BlogRepositoriesInterface(Protocol):

    def create_blog(self, data: OrderedDict) -> models.Blog: ...

    def get_blog(self) -> QuerySet[models.Blog]: ...


class BlogRepositoriesV1:
    model = models.Blog

    def create_blog(self, data: OrderedDict) -> models.Blog:
        return self.model.objects.create(**data)

    def get_blog(self) -> QuerySet[models.Blog]:
        return self.model.objects.all()
