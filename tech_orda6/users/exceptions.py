class ChildrenNotFound(Exception):
    'Children not found in dict'
    
    message = 'Children not found XDXDXDXDXDXDXDXDXDXD'

    def __str__(self) -> str:
        return self.message

class PasswordIsTooShort(Exception):
    message = 'Password Is Too Short XDXDXDXDXDXDXDXDXDXD'

    def __str__(self) -> str:
        return self.message