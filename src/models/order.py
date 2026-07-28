from src.models.exceptions import InvalidOrderError

class Order:
    def __init__(self,order_id, products: list, user):
        self.products = products
        self.order_id = order_id
        self.user = user

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self,values):
        if not isinstance(values, list) or len(values) == 0:
            raise InvalidOrderError("Ошибка при получении заказа")
        self._products = values.copy()

    def __str__(self):
        return f"Заказ #{self.order_id} на сумму {self.calculate_total()} руб. (Пользователь: {self.user})"

    def calculate_total(self):
        return sum(product.get_total_price() for product in self.products)