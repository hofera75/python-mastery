import sys
import inspect

class StructureException(Exception):
    pass

class Structure():
    _fields = ()


    @classmethod
    def create_init(cls):
        argstr = ','.join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'
        locs = { }
        exec(code, locs)
        cls.__init__ = locs['__init__']

    def __repr__(self) -> str:
        fields = ','.join(field.__repr__() for field in self.__dict__.values())
        return f'{self.__class__.__name__}({fields})'
    
    def  __setattr__(self, name, value):
        if name[0] != '_':
            if name not in self.__class__._fields:
                raise AttributeError(f'Can only set defined attributes {self.__class__._fields}')
        super().__setattr__(name,value)

