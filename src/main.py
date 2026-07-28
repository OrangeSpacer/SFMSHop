from src.models.order import Order
from src.models.product import Product
from src.models.user import User
from src.models.payment import CardPayment, PayPalPayment
from src.models.exceptions import BusinessLogicError,ValidationError



# try:
#     product = Product(-1000, 1, "Мышь")

# except ValidationError as e:
#     print(f"Ошибка валидации: {e}")


# # Проверка склада
# try:
#     product = Product(1000, 10, "Мышь")

#     product.sell(100)

# except BusinessLogicError as e:
#     print(f"Ошибка бизнес-логики: {e}")


# # Проверка заказа
# try:
#     order = Order(1,[],"Иван")

# except BusinessLogicError as e:
#     print(f"Ошибка бизнес-логики: {e}")

def process_order_system():
    user = User("Иван", "ivan@test.com")
    product1 = Product("Ноутбук", 50000, 2)
    product2 = Product("Мышь", 1500, 3)
    order = Order(1, [product1, product2], user)


    total = order.calculate_total()
    print("Общая стоимость заказа:", total)

    payments = [
        CardPayment(1000, "1234 5678 9012 3456"),
        PayPalPayment(2000, "test@paypal.com")
    ]
    for payment in payments:
        print(payment.process_payment())

    sorted_products = sorted([product1, product2])
    for product in sorted_products:
        print(product)

    try:
        product1.set_price(-1000) # Вызовет ValidationError
    except ValidationError as e:
        print("Ошибка валидации:", e)

process_order_system()