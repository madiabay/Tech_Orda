class TheLastDirectory(Exception):
    message = 'This directory is last'
    
    def __str__(self) -> str:
        return f'{self.message}'


class DirNotFound(Exception):
    message = 'Directory is not exist'
    
    def __str__(self) -> str:
        return f'{self.message}'