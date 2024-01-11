def convert_int(number: int) -> "Book":
    return float(number)


class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Name is {self.name !r} and age {self.age}'

    @classmethod
    def new_name(cls, name, age):
        return cls(name, age+10)


class CatError(ValueError):
    pass


if __name__ == '__main__':
    emp = Employee("su", 10)
    print(emp)
    emp = emp.new_name('js', 15)
    print(emp)
    from run_code import *
    print_hi()
    raise CatError