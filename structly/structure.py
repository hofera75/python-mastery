import sys
import inspect

from structly.validate import Validator, validated
from collections import ChainMap

__all__ = ['Structure']

def validate_attributes(cls):
    validators = []
    expected_types = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
        elif callable(val) and val.__annotations__:
            setattr(cls, name, validated(val))
        
    cls._fields = [val.name for val in validators]

    # Collect type conversions. The lambda x:x is an identity
    # function that's used in case no expected_type is found.
    cls._types = tuple([ getattr(v, 'expected_type', lambda x: x)
                   for v in validators ])
    
    cls.create_init()
    return cls

class StructureException(Exception):
    pass



class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)
        
    @staticmethod
    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)

class Structure(metaclass=StructureMeta):
    _fields = ()
    _types = ()

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)

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

    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)

    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
            
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)


def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls