from datetime import datetime

from sqlalchemy import Integer, String, Column, DateTime

from model.base import Base


class Order(Base):
    __tablename__ = 'orders'
    _id = Column("id", Integer, primary_key=True)
    _name = Column("name", String(30))
    _order_item = Column("order_item", String(50))
    _quantity= Column("quantity", Integer)
    _price = Column("price", Integer)
    _order_time = Column("order_time", DateTime, default=datetime.utcnow)

    def __init__(self, id, name,order_item,quantity, price):
        self.id = id
        self.name = name
        self.order_item = order_item
        self.quantity =quantity
        self._price =price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def order_item(self):
        return self._order_item

    @order_item.setter
    def order_item(self, value):
        self._order_item = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price= value

    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value