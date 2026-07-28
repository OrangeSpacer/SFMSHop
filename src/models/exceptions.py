class SFMShopException(Exception):
    pass


class ValidationError(SFMShopException):
    pass

class NegativePriceError(ValidationError):
    """Цена не может быть отрицательной"""
    pass

class InvalidQuantityError(ValidationError):
    """количество ≤ 0"""
    pass


class BusinessLogicError(SFMShopException):
    """Ошибка бизнес-логики"""
    pass


class InsufficientStockError(BusinessLogicError):
    """нехватка товара"""
    pass


class InvalidOrderError(BusinessLogicError):
    """пустой список товаров"""
    pass



class DatabaseError(SFMShopException):
    """Ошибка базы данных"""
    pass