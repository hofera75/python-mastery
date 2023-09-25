import sys
import inspect

class StructureException(Exception):
    pass

class Structure():
    _fields = ()

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters)

    def __repr__(self) -> str:
        fields = ','.join(field.__repr__() for field in self.__dict__.values())
        return f'{self.__class__.__name__}({fields})'
    
    def  __setattr__(self, name, value):
        if name[0] != '_':
            if name not in self.__class__._fields:
                raise AttributeError(f'Can only set defined attributes {self.__class__._fields}')
        super().__setattr__(name,value)

