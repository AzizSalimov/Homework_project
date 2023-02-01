class Hotel:
    def __init__(self, name, full_name,price):
        self.name = name
        self.full_name = full_name
        self.price = price

    def get_attr(self, as_dict):
        pass


def get_attrs(self, as_dict=False):
    if as_dict:
        return {
            "Name": self.name,
            'Full name': self.full_name,
            "Price": self.price,
        }
    return [
        self.name,
        self.full_name,
        self.price

    ]


