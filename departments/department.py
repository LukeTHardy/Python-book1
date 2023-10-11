class Department:

    def __init__(self, name, description):
        self.department_name = name
        self.description = description
        self.clothes = []

    def add_article(self, article):
        self.clothes.append(article)

    def remove_article(self, article):
        self.clothes.remove(article)

    def __str__(self):
        return f"This is the {self.department_name}, {self.description} and it has {self.__len__} uniques pieces of clothing"

    def __len__(self):
        return len(self.clothes)
