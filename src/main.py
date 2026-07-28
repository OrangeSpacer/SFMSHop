from src.models.order import Order
from src.models.product import Product
from src.models.user import User
from src.models.exceptions import NegativePriceError,SFMShopException,BusinessLogicError,DatabaseError,ValidationError, InvalidOrderError, InsufficientStockError, InvalidQuantityError

# products = [
#     Product(1500, 20, "Мышь"),
#     Product(3000, 15, "Клавиатура"),
#     Product(50000, 10, "Ноутбук")
# ]

# products.sort()

# for product in products:
#     print(product)


# order = Order(
#     1,
#     products,
#     "Иван"
# )

# print(order)



try:
    product = Product(-1000, 1, "Мышь")

except ValidationError as e:
    print(f"Ошибка валидации: {e}")


# Проверка склада
try:
    product = Product(1000, 10, "Мышь")

    product.sell(100)

except BusinessLogicError as e:
    print(f"Ошибка бизнес-логики: {e}")


# Проверка заказа
try:
    order = Order(1,[],"Иван")

except BusinessLogicError as e:
    print(f"Ошибка бизнес-логики: {e}")