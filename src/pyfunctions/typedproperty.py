def typedproperty(expected_type):
    private_name = '_' + expected_type.__class__.__name__

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)
   
    return value


def Integer():
    return typedproperty(int)

def Float():
    return typedproperty(float)

def String():
    return typedproperty(str)