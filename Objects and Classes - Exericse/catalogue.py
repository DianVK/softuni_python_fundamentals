class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [product for product in self.products if product[0] == first_letter]

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        sorted_products = sorted(self.products)
        result += "\n".join(sorted_products)
        return result