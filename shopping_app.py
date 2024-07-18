from customer import Customer
from item import Item
from seller import Seller

seller = Seller("Tienda DIC")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria", 13880, seller)
    Item("Placa base", 28980, seller)
    Item("Unidad de alimentación", 8980, seller)
    Item("Caja para PC", 8727, seller)
    Item("HDD de 3.5 pulgadas", 10980, seller)
    Item("SSD de 2.5 pulgadas", 13370, seller)
    Item("SSD M.2", 12980, seller)
    Item("Enfriador de CPU", 13400, seller)
    Item("Tarjeta gráfica", 23800, seller)

print("🤖 ¿Cuál es tu nombre?")
customer = Customer(input())

print("🏧 Ingresa la cantidad de dinero a cargar en la billetera")
customer.wallet.deposit(int(input()))

print("🛍️ Comenzando la compra")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Ingresa el número del producto")
    number = int(input())

    print("⛏ Ingresa la cantidad del producto")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Monto total: {customer.cart.total_amount()}")

    print("😭 ¿Deseas finalizar la compra? (yes/no)")
    end_shopping = input() == "yes"

print("💸 ¿Confirmas la compra? (yes/no)")
if input() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ Posesiones de {customer.name}")
customer.show_items()
print(f"😱👛 Saldo de la billetera de {customer.name}: {customer.wallet.balance}")

print(f"📦 Inventario de {seller.name}")
seller.show_items()
print(f"😻👛 Saldo de la billetera de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Monto total: {customer.cart.total_amount()}")

print("🎉 Finalizado")
