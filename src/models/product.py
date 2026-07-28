from src.models.exceptions import NegativePriceError, InsufficientStockError, InvalidQuantityError, ValidationError


class Product:
    def __init__(self, name, price, quantity):
        self.price = price
        self.name = name
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if(value < 0):
            raise NegativePriceError("Цена не может быть отрицательной")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if(value < 0):
            raise InvalidQuantityError("Количество должно быть больше нуля")
        self._quantity = value

    def sell(self, amount):
        if amount <= 0:
            raise InvalidQuantityError(
                f"Количество должно быть больше нуля, получено: {amount}"
            )
        if self.quantity < amount:
            raise InsufficientStockError(
                f"Товара недостаточно. На складе: {self.quantity}, требуется: {amount}"
            )
        self.quantity -= amount
        return self.quantity

    def set_price(self,price):
        if(price < 0):
            raise ValidationError("Цена не может быть отрицательной")

        self.price = price

    

    def get_total_price(self):
        return self.price * self.quantity

    def get_category():
        pass

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price} руб., Количество: {self.quantity}"

    def __repr__(self):
            return f"Product('{self.name}', {self.price}, {self.quantity})"