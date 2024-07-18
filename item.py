class Item:
    from ownable import set_owner
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Al crear una instancia de Item, esta instancia de Item (self) se almacena en la variable de clase instances.
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # Devuelve instances ==> Item.item_all() devuelve todas las instancias de Item creadas hasta ahora.
        return Item.instances
