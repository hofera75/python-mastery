class StructureException(Exception):
    pass

class Structure():
    _fields = ()

    def __init__(self, *args):
        if (len(self.__class__._fields) != len(args)):
            raise AttributeError(f'Number of arguments must be {len(self.__class__._fields)}')
        for field, argument in zip(self.__class__._fields, args):
            self.__dict__[field] = argument

    def __repr__(self) -> str:
        fields = ','.join(field.__repr__() for field in self.__dict__.values())
        return f'{self.__class__.__name__}({fields})'
    
    def  __setattr__(self, name, value):
        if name[0] != '_':
            if name not in self.__class__._fields:
                raise AttributeError(f'Can only set defined attributes {self.__class__._fields}')
        super().__setattr__(name,value)

