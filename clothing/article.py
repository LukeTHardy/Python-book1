from datetime import date


class Article:
    def __init__(self, name, size, material, category, sku_num):
        self.name = name
        self.material = material
        self.size = size
        self.category = category
        self.date_added = date.today()
        self.__sku_number = sku_num

    def __str__(self):
        return f"{self.name} is a {self.size}, {self.material} {self.category}"

    @property
    def sku_number(self):
        return self.__sku_number

    @sku_number.setter
    def chip_num(self):
        pass
