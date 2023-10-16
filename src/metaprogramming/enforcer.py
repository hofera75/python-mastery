from functools import wraps

def enforce(**args):
    def enf(func):
        @wraps
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return enf