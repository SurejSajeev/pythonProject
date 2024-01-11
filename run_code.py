import functools


def authenticate(func):
    @functools.wraps(func)
    def check_it(*args, **kwargs):
        print(f"this is checking {args[0]}")
        func(*args, **kwargs)
        print(f"complete {args[0]}")
    return check_it


@authenticate
def start_it(name):
    print(f"test dec {name}")



start_it('s')

print(start_it.__name__)