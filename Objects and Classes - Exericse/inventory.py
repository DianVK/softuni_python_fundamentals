class Inventory:
    def __init__(self, capacity=0):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > 0:
            self.items.append(item)
            self.__capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return len(self.items)

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity}"