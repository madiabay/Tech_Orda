from typing import OrderedDict, Protocol
from api import models


class ProductRepositoriesInterface(Protocol):

    def create_product(self, data: OrderedDict) -> models.Product: ...

    def get_product(self) -> 