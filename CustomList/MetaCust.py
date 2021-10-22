def add_custom(name):
    return 'custom_' + name


class CustomMeta(type):
    def __new__(mcs, name, bases, class_dict):
        new_dict = {attr if attr.startswith("__") else add_custom(attr): val
                    for attr, val in class_dict.items()}
        return super().__new__(mcs, name, bases, new_dict)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100
