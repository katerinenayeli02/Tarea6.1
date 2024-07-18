class Cart:
    from item_manager import show_items
    from ownable import set_owner

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
        #    pass    # Al codificar el método check_out, elimine pass.
        # Requisitos
        #   - El monto total de la compra de todos los artículos en el carrito (Cart#items) se transfiere de la billetera del dueño del carrito a la billetera del dueño del artículo.
        #   - Todos los derechos de propiedad de los artículos en el carrito (Cart#items) se transfieren al dueño del carrito.
        #   - El carrito (Cart#items) queda vacío.
        # Sugerencias
        #   - Billetera del dueño del carrito ==> self.owner.wallet
        #   - Billetera del dueño del artículo ==> item.owner.wallet
        #   - Transferencia de dinero ==> Retirar la cantidad de (?) del saldo de la billetera de (?), y depositar esa cantidad en la billetera de (?)
        #   - Transferencia de derechos de propiedad de los artículos al dueño del carrito ==> Cambiar el dueño (item.owner = ?)
                # Verifica si el saldo de la billetera del dueño del carrito es suficiente para cubrir el monto total de la compra
            print("Saldo insuficiente en la billetera para completar la compra.")
            return

        # Recorre todos los artículos en el carrito
        for item in self.items:
            # Transfiere el monto del precio del artículo de la billetera del dueño del carrito a la billetera del dueño del artículo
            self.owner.wallet.withdraw(item.price)
            item.owner.wallet.deposit(item.price)

            # Cambia la propiedad del artículo al dueño del carrito
            item.owner = self.owner

        # Vacía el carrito después de completar la compra
        self.items = []

        print("Compra completada con éxito.")
        print("El carrito está ahora vacío.")
