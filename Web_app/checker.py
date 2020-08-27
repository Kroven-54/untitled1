from functools import wraps

from flask import session


def check_logged_in(func):
    @wraps(func)
    def wrapper(args: dict, kwargs: dict) -> object:
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in.'
    return wrapper
