def add_custom(name):
    return 'custom_' + name


class CustomMeta(type):
    def __init__(cls, name, bases, class_dict):
        super().__init__(name, bases, class_dict)
        class_dict['__init__'](cls)
        buf = {}
        for attr in cls.__dict__.keys():
            if not attr.startswith('__'):
                buf[attr] = super().__getattribute__(attr)
        for attr, val in buf.items():
            super().__delattr__(attr)
            super().__setattr__('custom_' + attr, val)

    def __call__(cls, *args, **kwargs):
        my_class = super(CustomMeta, cls).__call__()
        my_class.__dict__.clear()
        return my_class


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100
