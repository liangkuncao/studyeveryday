class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Foo(Singleton):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Foo(object):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)
print(foo1 == foo2)